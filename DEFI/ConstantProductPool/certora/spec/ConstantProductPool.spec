/***
This example explains the many features of the Certora Verification Language. 
See https://docs.certora.com for a complete guide.
***/

// reference from the spec to additional contracts used in the verification 
using DummyERC20A as _token0;
using DummyERC20B as _token1;
using ConstantProductPool as _pool;


/*
    Declaration of methods that are used in the rules. `envfree` indicates that
    the method is not dependent on the environment (`msg.value`, `msg.sender`).
    Methods that are not declared here are assumed to be dependent on the
    environment.
*/

methods{
    function token0() external returns (address) envfree;
    function token1() external returns (address) envfree;
    function allowance(address,address) external returns (uint256) envfree;
    function totalSupply() external returns (uint256)  envfree;
    function swap(address tokenIn, address recipient) external returns (uint256) envfree;
    
    //calls to external contracts  
    function _token0.balanceOf(address account) external returns (uint256) envfree;
    function _token1.balanceOf(address account) external returns (uint256) envfree;
    function _token0.allowance(address owner, address spender) external returns (uint256) envfree;
    function _token1.allowance(address owner, address spender) external returns (uint256) envfree;
    function _token0.transfer(address, uint) external;
    function _token1.transfer(address, uint) external;

    //external calls to be resolved by dispatcher - taking into account all available implementations 
    function _.transferFrom(address sender, address recipient, uint256 amount) external => DISPATCHER(true);
    function _.balanceOf(address) external => DISPATCHER(true);
    
}

// a cvl function for precondition assumptions 
function setup(env e){
    address zero_address = 0;
    uint256 MINIMUM_LIQUIDITY = 1000;
    require totalSupply() == 0 || currentContract._balances[zero_address] == MINIMUM_LIQUIDITY, "Either pool is empty or minimum liquidity is locked";
    require currentContract._balances[zero_address] + currentContract._balances[e.msg.sender] <= totalSupply(), "Sum of balances does not exceed total supply, rule sumFunds";
    require _token0 == token0(), "Token0 reference must match contract's token0";
    require _token1 == token1(), "Token1 reference must match contract's token1";
}


/*
Property: For all possible scenarios of swapping token1 for token0, the balance of the recipient is updated as expected. 

This property is implemented as a unit-test style rule. It checks one method but on all possible scenarios.
Note:
 It also takes into account if the recipient is the contract itself, in which case this property does not hold since the balance is unchanged.
As a result, we add a requirement that the recipient is not the currentContract.

This property catches a bug in which there is a switch between the token and the recipient:
        transfer( recipient, tokenOut, amountOut);

Formula:
        { b = _token0.balanceOf(recipient) }
            amountOut := swap(_token1, recipient);
        { _token0.balanceOf(recipient) = b + amountOut }
*/

rule integrityOfSwap(address recipient) {
    env e; /* represents global solidity variables such as msg.sender, block.timestamp */
    setup(e);
    uint256 balanceBefore = _token0.balanceOf(recipient);
    uint256 amountOut = swap(_token1, recipient);
    uint256 balanceAfter = _token0.balanceOf(recipient);
    assert (recipient != currentContract) => balanceAfter == balanceBefore + amountOut; 
}

/*
Property: Only the user  or an allowed spender can decrease the user's LP balance.

This property is implemented as a parametric rule - it checks all public/external methods of the contract.

This property catches a bug when there is a switch between the token and the recipient in burnSingle:
        transfer( recipient, tokenOut, amountOut);

Formula:
        { b = balanceOf(account), allowance = allowance(account, e.msg.sender) }
            op by e.msg.sender;
        { balanceOf(account) < b =>  (e.msg.sender == account  ||  allowance >= (before-balanceOf(account)) }
*/

rule noDecreaseByOther(method f, address account) {
    env e;
    setup(e);
    require e.msg.sender != account, "Sender must be different from account to test unauthorized access";
    require account != currentContract, "Account must not be the pool contract to properly test balance changes"; 
    uint256 allowance = allowance(account, e.msg.sender); 
    
    uint256 before = currentContract._balances[account];
    calldataarg args;
    f(e,args); /* check on all possible arguments */
    uint256 after = currentContract._balances[account];
    /* logic implication : true when: (a) the left hand side is false or (b) right hand side is true  */
    assert after < before =>  (e.msg.sender == account  ||  allowance >= (before-after))  ;
}


/*
Property: For both token0 and token1 the balance of the system is at least as much as the reserves.

This property is implemented as an invariant. 
Invariants are defined as a specification of a condition that should always be true once an operation is concluded.
In addition, the invariant also checks that it holds immediately after the constructor of the code runs.

This invariant also catches the bug in which there is a switch between the token and the recipient in burnSingle:
        transfer( recipient, tokenOut, amountOut);

Formula:
    getReserve0() <= _token0.balanceOf(currentContract) &&
    getReserve1() <= _token1.balanceOf(currentContract)
*/

invariant balanceGreaterThanReserve()
    (currentContract.reserve0 <= _token0.balanceOf(currentContract))&&
    (currentContract.reserve1 <= _token1.balanceOf(currentContract))
    {
        preserved with (env e){
         setup(e);
        }

        // This preserved is safe because transferFrom is called from the currentContract whose code is known and
        // it is not msg.sender. It would not be safe to do if the call was to a function of an unresolved contract.
        preserved _.transferFrom(address sender, address recipient,uint256 amount) with (env e1) {
            requireInvariant allowanceOfPoolAlwaysZero(e1.msg.sender);
            require e1.msg.sender != currentContract, "The pool does not call itself";
        }

        // This preserved is safe because transfer is called from the currentContract whose code is known and
        // it is not msg.sender.
        preserved _.transfer(address recipient, uint256 amount) with (env e2) {
            require e2.msg.sender != currentContract, "Caller must not be the pool contract for external transfer calls";
        }
    }

invariant allowanceOfPoolAlwaysZero(address a)
    _token0.allowance(_pool, a) == 0 && _token1.allowance(_pool, a) == 0
    {
        // This preserved is safe because we know the code in the pool contract.
        preserved _.approve(address spender, uint256 amount) with (env e1) {
            require e1.msg.sender != _pool, "Sender must not be the pool contract for approve calls";
        }

        // This preserved is safe because we know the code in the pool contract.
        preserved _.increaseAllowance(address spender, uint256 addedValue) with (env e2) {
            require e2.msg.sender != _pool, "Sender must not be the pool contract for increaseAllowance calls";
        }
    }


/*
Property: Integrity of totalSupply with respect to the amount of reserves. 

This is a high level property of the system - the ability to pay back liquidity providers.
If there are any LP tokens (the totalSupply is greater than 0), then neither reserves0 nor reserves1 should ever be zero (otherwise the pool could not produce the underlying tokens).

This invariant catches the original bug in Trident where the amount to receive is computed as a function of the balances and not the reserves.

Formula:
    (totalSupply() == 0 <=> getReserve0() == 0) &&
    (totalSupply() == 0 <=> getReserve1() == 0)
*/

invariant integrityOfTotalSupply()
    
    (totalSupply() == 0 <=> currentContract.reserve0 == 0) &&
    (totalSupply() == 0 <=> currentContract.reserve1 == 0)
    {
        preserved with (env e){
            requireInvariant balanceGreaterThanReserve();
            setup(e);
        }
    }


/*
Property: Monotonicity of mint.

The more tokens a user transfers to the system the more LP tokens that user should receive. 
This property is implemented as a relational property - it compares two different executions on the same state.

This invariant catches a bug in mint where the LP tokens of the first depositor are not computed correctly and the less he transfers the more LP tokens he receives. 

Formula:
    { x > y }
        _token0.transfer(currentContract, x); mint(recipient);
        ~ 
        _token0.transfer(currentContract, y); mint(recipient);
    { balanceOf(recipient) at 1  >=  balanceOf(recipient) at 2  }
*/

rule monotonicityOfMint(uint256 x, uint256 y, address recipient) {
    env eT0;
    env eM;
    setup(eM);
    address token;
    require token == _token0 || token == _token1, "Token must be either token0 or token1";
    requireInvariant integrityOfTotalSupply();
    storage init = lastStorage;
    require recipient != currentContract, "Recipient must not be the pool contract to properly test external balance changes";
    require x > y, "First amount must be greater than second amount to test monotonicity";
    token.transfer(eT0, currentContract, x);
    uint256 amountOut0 = mint(eM,recipient);
    uint256 balanceAfter1 = currentContract._balances[recipient];
    
    token.transfer(eT0, currentContract, y) at init;
    uint256 amountOut2 = mint(eM,recipient);
    uint256 balanceAfter2 = currentContract._balances[recipient]; 
    assert balanceAfter1 >= balanceAfter2; 
}

/*
Property: Sum of balances

The sum of all balances is equal to the total supply.

This property is implemented with a ghost, an additional variable that tracks changes to the balance mapping.

Formula:
    
    sum(balanceOf(u) for all address u) = totalSupply()

*/

ghost mathint sumBalances{
    // assuming value zero at the initial state before constructor 
	init_state axiom sumBalances == 0; 
}


/* here we state when and how the ghost is updated */
hook Sstore _balances[KEY address a] uint256 new_balance
// the old value that balances[a] holds before the store
    (uint256 old_balance) {
  sumBalances = sumBalances + new_balance - old_balance;
}

invariant sumFunds() 
	sumBalances == totalSupply();


/*
Property: Full withdraw example

Give an example demonstrating a case where the user's deposit (transfer or mint) can be fully refunded by burning the liquidity provided.

This property uses the `satisfy` command, which causes the Prover to produce successful examples of expected properties rather than counterexamples.  In particular, this rule does not prove that every deposit can be fully withdrawn.

*/
rule possibleToFullyWithdraw(address sender, uint256 amount) {
    env eT0;
    env eM;
    setup(eM);
    address token;
    require token == _token0 || token == _token1, "Token must be either token0 or token1";
    uint256 balanceBefore = token.balanceOf(eT0,sender);
    
    require eM.msg.sender == sender, "Message sender must be the same as the user to perform withdrawal";
    require eT0.msg.sender == sender, "Message sender must be the same as the user to perform transfer";
    require amount > 0, "Amount must be positive to test meaningful deposit and withdrawal";
    token.transfer(eT0, currentContract, amount);
    uint256 amountOut0 = mint(eM,sender);
    // immediately withdraw 
    burnSingle(eM, _token0, amountOut0, sender);
    satisfy (balanceBefore == token.balanceOf(eT0, sender));
}



/*
Property: Zero withdraw has no effect

Withdraw (burn) of zero liquidity provides nothing - all the storage of all the contracts (including the ERC20s) stays the same. 

This property is implemented by saving the storage state before the transaction and comparing  that after the transaction the storage is the same.

*/

rule zeroWithdrawNoEffect(address to) {
    env e;
    setup(e);
    // The assumption is  no skimming 
    require currentContract.reserve0 == _token0.balanceOf(currentContract) && currentContract.reserve1 == _token1.balanceOf(currentContract), "Reserves must match balances to ensure no skimming has occurred";
    storage before = lastStorage;
    burnSingle(e, _token0, 0, to);
    storage after = lastStorage;
    assert before == after;
}
