import "../helpers/erc20.spec";

methods
{
    // envfree declarations
    function balanceOf(address) external returns(uint256) envfree;
    function totalSupply()      external returns(uint256) envfree;
    function asset()            external returns(address) envfree;

    // for checing call backs to the pool's function
    function _.deposit(uint256)  external => DISPATCHER(true);
    function _.withdraw(uint256) external => DISPATCHER(true);
    function _.flashLoan(address, uint256)        external => DISPATCHER(true);
   
    // flash loan receiver function
    function _.executeOperation(uint256,uint256,address) external => DISPATCHER(true);

    // harness functions
    function underlyingBalance()            external returns(uint256) envfree;
    function underlyingAllowance(address a) external returns(uint256) envfree;
 
}

function safeAssumptions(address a, env e) {
    require asset()      != currentContract;
    require e.msg.sender != currentContract;
    requireInvariant noAllowance(a);
}

invariant noAllowance(address a)
    underlyingAllowance(a) == 0
{ preserved with (env e) { safeAssumptions(a, e); } }


/// flash loans must increase the pool's underlying asset balance, assuming the
/// receiver has no pool balance.
rule flashLoanIncreasesBalance {
    address receiver; uint256 amount; env e;

    safeAssumptions(receiver, e);

    mathint balance_before = underlyingBalance();

    flashLoan(e, receiver, amount);

    mathint balance_after = underlyingBalance();

    assert balance_after >= balance_before,
        "flash loans must not decrease the contract's underlying balance";
}


/// `deposit` must increase the pool's underlying asset balance
rule integrityOfDeposit {

    mathint balance_before = underlyingBalance();


    env e; uint256 amount;
    safeAssumptions(_, e);

    deposit(e, amount);

    mathint balance_after = underlyingBalance();

    assert balance_after == balance_before + amount,
        "deposit must increase the underlying balance of the pool";
}

