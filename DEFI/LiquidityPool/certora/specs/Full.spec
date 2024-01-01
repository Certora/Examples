/***
This example is a full spec for LiquidityPool.
To run this use Certora cli with the conf file runFullPoll.conf
Example of a run: https://prover.certora.com/output/1512/b84b2123fc1f447ba6cff06d8e07552c?anonymousKey=9917501bc57d897a7ec341a2521b30d92237f95d
UnsatCores: https://prover.certora.com/output/1512/ce180e9d91464a3a9271cb5bf7119125/UnsatCoreVisualisation.html?anonymousKey=88059d4e9f56250f609546f0b77ebc3ed819509d
Mutation test for this spec: https://mutation-testing.certora.com/?id=66c71fdd-9a1d-44e4-b084-d8d4c3de9e61&anonymousKey=e157a2be-ed9d-4d30-90bb-06b6bee05daf
See https://docs.certora.com for a complete guide.
***/

using Asset as underlying;
using TrivialReceiver as _TrivialReceiver;

methods
{
    function balanceOf(address)                      external returns(uint256) envfree;
    function totalSupply()                           external returns(uint256) envfree;
    function transfer(address, uint256)              external returns(bool);
    function transferFrom(address, address, uint256) external returns(bool);
    function amountToShares(uint256)                 external returns(uint256) envfree;
    function sharesToAmount(uint256)                 external returns(uint256) envfree;
    function depositedAmount()                       external returns(uint256) envfree;
    function deposit(uint256)                        external returns(uint256);
    function withdraw(uint256)                       external returns(uint256);
    function calcPremium(uint256)                    external returns (uint256) envfree;

    function _.executeOperation(uint256,uint256,address) external => DISPATCHER(true);
    function flashLoan(address, uint256)                 external;

    function underlying.balanceOf(address)               external returns(uint256) envfree;
    function underlying.allowance(address, address)      external returns(uint256) envfree;
    function underlying.totalSupply()                    external returns(uint256) envfree;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Reentrancy ghost and hook                                                                                           │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
definition lock_on() returns bool = ghostReentrancyStatus == 2;
definition poll_functions(method f) returns bool = f.selector == sig:withdraw(uint256).selector ||
                                      f.selector == sig:deposit(uint256).selector ||
                                      f.selector == sig:flashLoan(address, uint256).selector;


ghost uint256 ghostReentrancyStatus;
ghost bool lock_status_on_call;

hook Sload uint256 status currentContract._status STORAGE {
    require ghostReentrancyStatus == status;
}

hook Sstore currentContract._status uint256 status STORAGE {
    ghostReentrancyStatus = status;
}

// we are hooking here on "CALL" opcodes in order to simulate reentrancy to a non-view function and check that the function reverts
hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    lock_status_on_call = lock_on(); 
}

// this rule prove the assumption e.msg.sender != currentContract;
rule reentrancyCheck(env e, method f, calldataarg args) filtered{f -> poll_functions(f)}{
    bool lockBefore = lock_on();
    
    f(e, args);
    
    bool lockAfter = lock_on();
    
    assert !lockBefore && !lockAfter;
    assert lock_status_on_call;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Deposite                                                                                                            │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule depositIntegrity(env e){

    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack

    uint256 amount;
    uint256 clientBalanceBefore = underlying.balanceOf(e.msg.sender);
    uint256 clientSharesBefore = balanceOf(e.msg.sender);

    uint256 depositedShares = deposit(e, amount);

    uint256 clientBalanceAfter = underlying.balanceOf(e.msg.sender);
    uint256 clientSharesAfter = balanceOf(e.msg.sender);

    assert (amount == 0) => (depositedShares == 0) && (clientBalanceBefore == clientBalanceAfter) && (clientSharesBefore == clientSharesAfter);
    assert (amount > 0) => (clientBalanceBefore - amount == to_mathint(clientBalanceAfter)) && (clientSharesBefore + depositedShares == to_mathint(clientSharesAfter));
}

rule depositRevertConditions(env e){

    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack

    uint256 amount;
    uint256 clientBalanceBefore = underlying.balanceOf(e.msg.sender);
    uint256 clientSharesBefore = balanceOf(e.msg.sender);
    
    bool underFlow = clientBalanceBefore - amount < 0;
    bool emptyPool = totalSupply() == 0 || depositedAmount() == 0;
    bool clientSharesOverflow = (clientSharesBefore + amount > max_uint256 && emptyPool) || clientSharesBefore + amountToShares(amount) > max_uint256;
    bool totalSharesOverflow = totalSupply() + amountToShares(amount) > max_uint256;
    bool contractUnderlyingOverflow = underlying.balanceOf(currentContract) + amount > max_uint256 || depositedAmount() + amount > max_uint256;
    bool overflow =  clientSharesOverflow || totalSharesOverflow || contractUnderlyingOverflow;
    bool payable = e.msg.value != 0;
    bool reentrancy = lock_on();
    bool notEnoughAllowance = underlying.allowance(e.msg.sender, currentContract) < amount;
    bool zeroShares = amountToShares(amount) == 0 && !emptyPool;
    bool expectedRevert = underFlow || overflow || payable || reentrancy || notEnoughAllowance || zeroShares;

    deposit@withrevert(e, amount);

    assert lastReverted <=> expectedRevert;
}

rule depositGreaterThanZeroWithMinted(env e) {
    uint256 amount;
    require amount > 0;
    uint256 amountMinted = deposit(e, amount);
    
    assert amount > 0 <=> amountMinted > 0;
}

rule splitDepositFavoursTheContract(env e){
    uint256 wholeAmount;
    uint256 amountA; 
    uint256 amountB;
    require amountA + amountB == to_mathint(wholeAmount);
    requireInvariant totalSharesIsZeroWithUnderlyingDeposited();

    storage init = lastStorage;

    uint256 wholeShares = deposit(e, wholeAmount);

    uint256 sharesA = deposit(e, amountA) at init;
    uint256 sharesB = deposit(e, amountB);

    assert to_mathint(wholeShares) >= sharesA + sharesB;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Withdraw                                                                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule withdrawIntegrity(env e){

    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack

    uint256 shares;
    uint256 clientBalanceBefore = underlying.balanceOf(e.msg.sender);
    uint256 clientSharesBefore = balanceOf(e.msg.sender);

    uint256 withdrawAmount = withdraw(e, shares);

    uint256 clientBalanceAfter = underlying.balanceOf(e.msg.sender);
    uint256 clientSharesAfter = balanceOf(e.msg.sender);


    assert (shares == 0) => (withdrawAmount == 0) && (clientBalanceBefore == clientBalanceAfter) && (clientSharesBefore == clientSharesAfter);
    assert (shares > 0) => (clientBalanceBefore + withdrawAmount == to_mathint(clientBalanceAfter)) && (clientSharesBefore - shares == to_mathint(clientSharesAfter));
}

rule withdrawRevertConditions(env e){

    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack

    uint256 amount;
    uint256 clientBalanceBefore = underlying.balanceOf(e.msg.sender);
    uint256 clientSharesBefore = balanceOf(e.msg.sender);
    
    bool clientBalanceUnderflow = clientSharesBefore - amount < 0;
    bool poolUnderflow = underlying.balanceOf(currentContract) - sharesToAmount(amount) < 0 || totalSupply() - amount < 0;
    bool underflow = clientBalanceUnderflow || poolUnderflow;
    bool overflow = clientBalanceBefore + sharesToAmount(amount) > max_uint256;
    bool payable = e.msg.value != 0;
    bool reentrancy = lock_on();
    bool notEnoughAllowance = underlying.allowance(currentContract, currentContract) < sharesToAmount(amount);
    bool zeroAmount = sharesToAmount(amount) == 0;
    bool poolIsEmpty = underlying.balanceOf(currentContract) == 0;
    bool expectedRevert = poolIsEmpty || underflow || overflow || payable || reentrancy || notEnoughAllowance || zeroAmount;

    withdraw@withrevert(e, amount);

    assert lastReverted <=> expectedRevert;
}

rule splitWithdrawFavoursTheContract(env e){
    uint256 wholeShares;
    uint256 sharesA; 
    uint256 sharesB;
    require sharesA + sharesB == to_mathint(wholeShares);

    storage init = lastStorage;

    uint256 wholeAmount = withdraw(e, wholeShares);

    uint256 amountA = withdraw(e, sharesA) at init;
    uint256 amountB = withdraw(e, sharesB);

    assert to_mathint(wholeAmount) >= amountA + amountB;
}


/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ FlashLoan, need to ask Nurit for interesting rules, pretty much depended on implementation                          │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule flashLoanIntegrity(env e){
    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack

    address receiver;
    uint256 amount;

    uint256 contractUnderlyingBalanceBefore  = underlying.balanceOf(currentContract);
    uint256 contractSharesBefore = balanceOf(currentContract);

    flashLoan(e, receiver, amount);

    uint256 contractUnderlyingBalanceAfter = underlying.balanceOf(currentContract);
    uint256 contractSharesAfter = balanceOf(currentContract);

    assert (amount == 0) => contractUnderlyingBalanceBefore == contractUnderlyingBalanceAfter;
    assert (amount > 0) => contractUnderlyingBalanceBefore < contractUnderlyingBalanceAfter;
    assert contractSharesBefore == contractSharesAfter;
}

rule flashLoanRevertConditions(env e){
    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack

    address receiver;
    uint256 amount;
    
    bool noPremium = calcPremium(amount) == 0;
    bool receiverIsNotIFlashloanAddress = receiver != _TrivialReceiver;\
    bool payable = e.msg.value != 0;
    bool reentrancy = lock_on();
    bool clientUnderflow = underlying.balanceOf(e.msg.sender) - calcPremium(amount) < 0;
    bool poolUnderflow = underlying.balanceOf(currentContract) - amount < 0 || depositedAmount() - amount < 0;
    bool underflow = clientUnderflow || poolUnderflow;
    bool poolBlanceOverflow = underlying.balanceOf(currentContract) + calcPremium(amount) > max_uint256 || depositedAmount() + calcPremium(amount) > max_uint256;
    bool clientBalanceOverflow = underlying.balanceOf(e.msg.sender) + amount > max_uint256;
    bool overflow = poolBlanceOverflow || clientBalanceOverflow;
    bool notEnoughAllowance = to_mathint(underlying.allowance(e.msg.sender, currentContract)) < calcPremium(amount) + amount || underlying.allowance(currentContract, currentContract) < amount;
    bool isExpectedToRevert = notEnoughAllowance || overflow || underflow || noPremium || receiverIsNotIFlashloanAddress || payable || reentrancy;

    flashLoan@withrevert(e, receiver, amount);

    assert isExpectedToRevert <=> lastReverted;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Find and show a path for each method.                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule reachability(method f)
{
	env e;
	calldataarg args;
	f(e,args);
	satisfy true;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ The total shares supply of the system is less than equal the underlying asset holding of the system                │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
invariant totalSharesLessThanUnderlyingBalance()
    totalSupply() <= underlying.balanceOf(currentContract)
    {
        preserved with(env e) {
            require e.msg.sender != currentContract;
            requireInvariant totalSharesLessThanDepositedAmount();
            requireInvariant depositedAmountLessThanContractUnderlyingAsset();
        }
    }

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ The total shares supply of the system is less than equal the deposit amount                                         │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
invariant totalSharesLessThanDepositedAmount()
    totalSupply() <= depositedAmount();

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ The deposited Amount of the system is less than equal the contract underlying asset                                 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
invariant depositedAmountLessThanContractUnderlyingAsset()
    depositedAmount() <= underlying.balanceOf(currentContract)
    {
        preserved with(env e) {
            require e.msg.sender != currentContract;
        }
    }

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ The total shares supply of the system is zero if and only if the underlying asset holding of the system is zero    │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
invariant totalSharesIsZeroWithUnderlyingDeposited()
		totalSupply() == 0 <=> depositedAmount() == 0;

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Sum of shares equal total shares supply                                                                             │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/

ghost mathint sumOfShares {
    init_state axiom sumOfShares == 0;
}

hook Sstore _balanceOf[KEY address user] uint256 newSharesBalance (uint256 oldSharesBalance) STORAGE
{
    sumOfShares = sumOfShares + newSharesBalance - oldSharesBalance;
}

invariant totalSharesEqualSumOfShares()
		to_mathint(totalSupply()) == sumOfShares;


/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Sum of underlying equal total supply                                                                             │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/

ghost mathint sumBalances {
    init_state axiom sumBalances == 0;
}

hook Sstore underlying._balanceOf[KEY address user] uint256 newBalance (uint256 oldBalance) STORAGE
{
    sumBalances = sumBalances + newBalance - oldBalance;
}

invariant totalIsSumBalances()
    to_mathint(underlying.totalSupply()) == sumBalances;

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Client shares and balance anti-monotonicity ((increase and decrease) or (decrease and increase))                    │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule sharesAndBalanceConsistency(env e, method f) filtered {
    f -> f.selector != sig:transfer(address,uint256).selector &&
    f.selector != sig:transferFrom(address,address,uint256).selector
    } {
    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack

    uint256 UnderlyingBalanceBefore = underlying.balanceOf(e.msg.sender);
    uint256 SharesBefore = balanceOf(e.msg.sender);
    
    calldataarg args;
    f(e, args);
    
    uint256 UnderlyingBalanceAfter = underlying.balanceOf(e.msg.sender);
    uint256 SharesAfter = balanceOf(e.msg.sender);
    
    assert UnderlyingBalanceBefore < UnderlyingBalanceAfter <=> SharesBefore > SharesAfter;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ More shares leads to bigger withdraw                                                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule moreSharesMoreWithdraw(env e) {
    uint256 sharesX;
    uint256 sharesY;
    uint256 amountX;
    uint256 amountY;

    storage init = lastStorage;
    
    amountX = withdraw(e, sharesX);
    amountY = withdraw(e, sharesY) at init;
    
    assert sharesX > sharesY => amountX >= amountY;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Rounding favours the house                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule amountRoundingTripFavoursContract(env e) {
    requireInvariant totalSharesIsZeroWithUnderlyingDeposited();

    uint256 clientAmountBefore = underlying.balanceOf(e.msg.sender);
    uint256 contractAmountBefore = underlying.balanceOf(currentContract);

    uint256 clientShares = deposit(e, clientAmountBefore);
    uint256 clientAmountAfter = withdraw(e, clientShares);
    uint256 contractAmountAfter = underlying.balanceOf(currentContract);

    assert clientAmountBefore >= clientAmountAfter;
    assert contractAmountBefore <= contractAmountAfter;
}

/*
Bug detected, if contract deploy with balance it can be drained.
Bug fixed by calculating deposit amount and use in in the conversions instead of the contract underlying asset.
*/
rule sharesRoundingTripFavoursContract(env e) {
    uint256 clientSharesBefore = balanceOf(e.msg.sender);
    uint256 contractSharesBefore = balanceOf(currentContract);

    requireInvariant totalSharesLessThanDepositedAmount();
    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack

    uint256 depositedAmount = depositedAmount();

    uint256 clientAmount = withdraw(e, clientSharesBefore);
    uint256 clientSharesAfter = deposit(e, clientAmount);
    uint256 contractSharesAfter = balanceOf(currentContract);

    /* 
    if client is last and first depositor he will get more shares
    but still he wont be able to withdraw more underlying asset than deposited amount (which in that case its only his deposit) 
    as proved in noClientHasSharesWithMoreValueThanDepositedAmount invariant.
    */ 
    assert (clientAmount == depositedAmount) => clientSharesBefore <= clientSharesAfter; 
    
    // all other states
    assert (clientAmount < depositedAmount) => clientSharesBefore >= clientSharesAfter;
    assert contractSharesBefore <= contractSharesAfter;
}

/*
  prove bug fix
*/
invariant noClientHasSharesWithMoreValueThanDepositedAmount(address a)
        sharesToAmount(balanceOf(a)) <= depositedAmount()
		{
			preserved with(env e) {
				require balanceOf(a) + balanceOf(e.msg.sender) < to_mathint(totalSupply());
			}
            preserved transferFrom(address sender, address recipient, uint256 amount) with (env e) {
                require balanceOf(sender) + balanceOf(e.msg.sender) + balanceOf(recipient) < to_mathint(totalSupply());
            }
		}
/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Conversions are monotonic increasing functions.                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/

rule amountToSharesConversion(env e){
    uint256 amountA;
    uint256 amountB;
    assert amountA <= amountB => amountToShares(amountA) <= amountToShares(amountB);
}

rule sharesToAmountConversion(env e){
    uint256 sharesA;
    uint256 sharesB;
    assert sharesA <= sharesB => sharesToAmount(sharesA) <= sharesToAmount(sharesB);
}

rule calculatePremium(env e){
    uint256 amountA;
    uint256 amountB;
    assert amountA <= amountB => calcPremium(amountA) <= calcPremium(amountB);
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ThirdParty not affected.                                                                                            │                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule thirdPartyNotAffected(env e, method f, calldataarg args) filtered {
    f -> f.selector != sig:transfer(address,uint256).selector &&
    f.selector != sig:transferFrom(address,address,uint256).selector
    }{
    address thirdParty;

    require thirdParty != currentContract && thirdParty != e.msg.sender; 

    uint256 thirdPartyBalanceBefore = underlying.balanceOf(thirdParty);
    uint256 thirdPartySharesBefore = balanceOf(thirdParty);

    f(e, args);

    uint256 thirdPartyBalanceAfter = underlying.balanceOf(thirdParty);
    uint256 thirdPartySharesAfter = balanceOf(thirdParty);

    assert (thirdPartyBalanceAfter == thirdPartyBalanceBefore);
    assert (thirdPartySharesAfter == thirdPartySharesBefore);
}