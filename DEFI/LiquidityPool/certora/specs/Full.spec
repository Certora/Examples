/***
This example is a full spec for LiquidityPool.
To run this use Certora cli with the conf file runFullPoll.conf
Example of a run: 
UnsatCores: 
Mutation test for this spec: 
See https://docs.certora.com for a complete guide.
***/


using Asset as underlying;

methods
{
    function balanceOf(address)                      external returns(uint256) envfree;
    function totalSupply()                           external returns(uint256) envfree;
    function transfer(address, uint256)              external returns(bool);
    function transferFrom(address, address, uint256) external returns(bool);
    function amountToShares(uint256)                 external returns(uint256) envfree;
    function sharesToAmount(uint256)                 external returns(uint256) envfree;
    function deposit(uint256)                        external returns(uint256);
    function withdraw(uint256)                       external returns(uint256);

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

ghost uint256 ghostReentrancyStatus;

hook Sload uint256 status currentContract._status STORAGE {
    require ghostReentrancyStatus == status;
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
    
    deposit(e, amount);

    uint256 clientBalanceAfter = underlying.balanceOf(e.msg.sender);
    uint256 clientSharesAfter = balanceOf(e.msg.sender);

    assert (amount == 0) => (clientBalanceBefore == clientBalanceAfter) && (clientSharesBefore == clientSharesAfter);
    assert (amount > 0) => (clientBalanceBefore > clientBalanceAfter) && (clientSharesBefore < clientSharesAfter);
}

rule depositRevertConditions(env e){

    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack

    uint256 amount;
    uint256 clientBalanceBefore = underlying.balanceOf(e.msg.sender);
    uint256 clientSharesBefore = balanceOf(e.msg.sender);
    
    bool underFlow = clientBalanceBefore - amount < 0;
    bool emptyPool = totalSupply() == 0 || underlying.balanceOf(currentContract) == 0;
    bool clientSharesOverflow = (clientSharesBefore + amount > max_uint256 && emptyPool) || clientSharesBefore + amountToShares(amount) > max_uint256;
    bool totalSharesOverflow = totalSupply() + amountToShares(amount) > max_uint256;
    bool contractUnderlyingOverflow = underlying.balanceOf(currentContract) + amount > max_uint256;
    bool overflow =  clientSharesOverflow || totalSharesOverflow || contractUnderlyingOverflow;
    bool payable = e.msg.value != 0;
    bool reentrancy = ghostReentrancyStatus == 2;
    bool notEnoughAllowance = underlying.allowance(e.msg.sender, currentContract) < amount;
    bool zeroShares = amountToShares(amount) == 0 && totalSupply() > 0 && underlying.balanceOf(currentContract) > 0;
    bool expectedRevert = underFlow || overflow || payable || reentrancy || notEnoughAllowance || zeroShares;

    deposit@withrevert(e, amount);

    assert lastReverted <=> expectedRevert;
}

rule depositDontAffectThirdParty(env e){
    address thirdParty;
    uint256 amount;

    require thirdParty != e.msg.sender && thirdParty != currentContract;

    uint256 thirdPartyBalanceBefore = underlying.balanceOf(thirdParty);
    uint256 thirdPartySharesBefore = balanceOf(thirdParty);

    deposit(e, amount);

    uint256 thirdPartyBalanceAfter = underlying.balanceOf(thirdParty);
    uint256 thirdPartySharesAfter = balanceOf(thirdParty);

    assert thirdPartyBalanceBefore == thirdPartyBalanceAfter;
    assert thirdPartySharesBefore == thirdPartySharesAfter;
}

rule depositGreaterThanZeroWithMinted(env e) {
    uint256 amount;
    uint256 amountMinted = deposit(e, amount);
    
    assert amount > 0 <=> amountMinted > 0;
}

rule splitDepositFavoursTheContract(env e){
    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack

    uint256 wholeAmount;
    uint256 amountA; 
    uint256 amountB;
    require amountA + amountB == to_mathint(wholeAmount);

    requireInvariant totalSharesLessThanUnderlyingBalance();
    requireInvariant totalIsSumBalances();
    requireInvariant totalSharesEqualSumOfShares();
    requireInvariant totalSharesIsZeroWithUnderlying();

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

    uint256 amount;
    uint256 clientBalanceBefore = underlying.balanceOf(e.msg.sender);
    uint256 clientSharesBefore = balanceOf(e.msg.sender);
    
    withdraw(e, amount);

    uint256 clientBalanceAfter = underlying.balanceOf(e.msg.sender);
    uint256 clientSharesAfter = balanceOf(e.msg.sender);

    assert (amount == 0) => (clientBalanceBefore == clientBalanceAfter) && (clientSharesBefore == clientSharesAfter);
    assert (amount > 0) => (clientBalanceBefore < clientBalanceAfter) && (clientSharesBefore > clientSharesAfter);
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
    bool reentrancy = ghostReentrancyStatus == 2;
    bool notEnoughAllowance = underlying.allowance(currentContract, currentContract) < sharesToAmount(amount);
    bool zeroAmount = sharesToAmount(amount) == 0;
    bool expectedRevert = underflow || overflow || payable || reentrancy || notEnoughAllowance || zeroAmount;

    withdraw@withrevert(e, amount);

    assert lastReverted <=> expectedRevert;
}

rule withdrawDontAffectThirdParty(env e){
    address thirdParty;
    uint256 amount;

    require thirdParty != e.msg.sender && thirdParty != currentContract;

    uint256 thirdPartyBalanceBefore = underlying.balanceOf(thirdParty);
    uint256 thirdPartySharesBefore = balanceOf(thirdParty);

    withdraw(e, amount);

    uint256 thirdPartyBalanceAfter = underlying.balanceOf(thirdParty);
    uint256 thirdPartySharesAfter = balanceOf(thirdParty);

    assert thirdPartyBalanceBefore == thirdPartyBalanceAfter;
    assert thirdPartySharesBefore == thirdPartySharesAfter;
}

rule splitWithdrawFavoursTheContract(env e){
    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack

    uint256 wholeShares;
    uint256 sharesA; 
    uint256 sharesB;
    require sharesA + sharesB == to_mathint(wholeShares);

    requireInvariant totalSharesLessThanUnderlyingBalance();
    requireInvariant totalSharesIsZeroWithUnderlying();

    storage init = lastStorage;

    uint256 wholeAmount = withdraw(e, wholeShares);

    uint256 amountA = deposit(e, sharesA) at init;
    uint256 amountB = deposit(e, sharesB);

    assert to_mathint(wholeAmount) >= amountA + amountB;
}


/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ FlashLoan, need to ask Nurit for interesting rules, pretty much depended on implementation                          │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule flashLoanIntegrity(env e){
    
    address receiver;
    uint256 amount;

    uint256 contractUnderlyingBalanceBefore  = underlying.balanceOf(currentContract);
    uint256 contractSharesBefore = balanceOf(currentContract);

    flashLoan(e, receiver, amount);

    uint256 contractUnderlyingBalanceAfter = underlying.balanceOf(currentContract);
    uint256 contractSharesAfter = balanceOf(currentContract);

    assert contractUnderlyingBalanceBefore <= contractUnderlyingBalanceAfter;
    assert contractSharesBefore <= contractSharesAfter;
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
        }
    }

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ The total shares supply of the system is zero if and only if the underlying assert holding of the system is zero    │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
invariant totalSharesIsZeroWithUnderlying()
		totalSupply() == 0 <=> underlying.balanceOf(currentContract) == 0
		{
			preserved with(env e) {
				require e.msg.sender != currentContract;
			}
		}
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
│ Client Shares and Balance can (increase and decrease) or (decrease and increase)                                    │
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
    requireInvariant totalSharesIsZeroWithUnderlying();

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
*/
rule sharesRoundingTripFavoursContract(env e) {
    uint256 clientSharesBefore = balanceOf(e.msg.sender);
    uint256 contractSharesBefore = balanceOf(currentContract);

    requireInvariant totalSharesEqualSumOfShares();
    require underlying.balanceOf(currentContract) > 0 => balanceOf(currentContract) > 0; //this assumption hides the bug and cant be proved.
    require sumOfShares >= clientSharesBefore + contractSharesBefore;
    require e.msg.sender != currentContract; // this assumption must hold to avoid shares dilute attack


    uint256 clientAmount = withdraw(e, clientSharesBefore);
    uint256 clientSharesAfter = deposit(e, clientAmount);
    uint256 contractSharesAfter = balanceOf(currentContract);

    assert clientSharesBefore >= clientSharesAfter;
    assert contractSharesBefore <= contractSharesAfter;
}