using ERC20Helper as erc20helper;

methods {
    
    function totalSupply() external returns uint256 envfree;
    function balanceOf(address) external returns uint256 envfree;
	function allowance(address,address) external returns uint256 envfree;
    function approve(address,uint256) external returns bool;
	function increaseAllowance(address,uint256) external returns bool;
    function transfer(address,uint256) external returns bool;
    function transferFrom(address,address,uint256) external returns bool;

	function erc20helper.tokenBalanceOf(address, address) external returns (uint256) envfree;
}

///
///
///  OTAKAR
///
///

/* 
	Property: Find and show a path for each method.
*/
rule reachability(method f)
{
	env e;
	calldataarg args;
	f(e,args);
	satisfy true;
}

/* 
   	Property: Define and check functions that should never revert
	Notice:  use f.selector to state which functions should not revert,e.g.f.selector == sig:balanceOf(address).selector 
*/  
definition nonReveritngFunction(method f ) returns bool = true; 

definition canIncreaseAllowance(method f ) returns bool = 
	f.selector == sig:approve(address,uint256).selector || 
	f.selector == sig:increaseAllowance(address,uint256).selector;

definition canDecreaseAllowance(method f ) returns bool = 
	f.selector == sig:approve(address,uint256).selector || 
	f.selector == sig:decreaseAllowance(address,uint256).selector ||
	f.selector == sig:transferFrom(address,address,uint256).selector;

definition canIncreaseBalance(method f ) returns bool = 
	f.selector == sig:mint(address,uint256).selector || 
	f.selector == sig:transfer(address,uint256).selector ||
	f.selector == sig:transferFrom(address,address,uint256).selector;

definition canDecreaseBalance(method f ) returns bool = 
	f.selector == sig:burn(address,uint256).selector || 
	f.selector == sig:transfer(address,uint256).selector ||
	f.selector == sig:transferFrom(address,address,uint256).selector;

definition priveledgedFunction(method f ) returns bool = 
	f.selector == sig:mint(address,uint256).selector || 
	f.selector == sig:burn(address,uint256).selector;

definition canIncreaseTotalSupply(method f ) returns bool = 
	f.selector == sig:mint(address,uint256).selector;

definition canDecreaseTotalSupply(method f ) returns bool = 
	f.selector == sig:burn(address,uint256).selector;


// This is a rule from the original spec, not modified by Otakar
rule noRevert(method f) filtered {f -> nonReveritngFunction(f) }
{
	env e;
	calldataarg arg;
    //consider auto filtering for non-payable functions 
	require e.msg.value == 0; 
	f@withrevert(e, arg); 
	assert !lastReverted, "method should not revert";
}

/* 
    Property: Checks if a function can be frontrun 
    Notice: Can be enhanced to check more than one function as rules can be double-parameteric
*/ 
// This is a rule from the original spec, not modified by Otakar
rule simpleFrontRunning(method f, method g) filtered { f-> !f.isView, g-> !g.isView }
{
	env e1;
	calldataarg arg;

	storage initialStorage = lastStorage;
	f(e1, arg); 
	

	env e2;
	calldataarg arg2;
	require e2.msg.sender != e1.msg.sender;
	g(e2, arg2) at initialStorage; 

	f@withrevert(e1, arg);
	bool succeeded = !lastReverted;

	assert succeeded, "should be called also if frontrunned";
}

/** 
    @title -   This rule find which functions are privileged.
    @notice A function is privileged if there is only one address that can call it.
    @dev The rules finds this by finding which functions can be called by two different users.
*/
// This is a rule from the original spec, not modified by Otakar
rule privilegedOperation(method f, address privileged) filtered {f -> priveledgedFunction(f) }
{
	env e1;
	calldataarg arg;
	require e1.msg.sender == privileged;

	storage initialStorage = lastStorage;
	f@withrevert(e1, arg); // privileged succeeds executing candidate privileged operation.
	bool firstSucceeded = !lastReverted;

	env e2;
	calldataarg arg2;
	require e2.msg.sender != privileged;
	f@withrevert(e2, arg2) at initialStorage; // unprivileged
	bool secondSucceeded = !lastReverted;

	assert  !(firstSucceeded && secondSucceeded), "function is privileged";
}

// This is a rule from the original spec, not modified by Otakar
rule decreaseInSystemEth(method f) {
   
    uint256 before = nativeBalances[currentContract];

    env e;
	calldataarg arg;
    f(e, arg);

    uint256 after = nativeBalances[currentContract];

    assert after >= before ||  false ; /* fill in cases where eth can decrease */ 
}

// This is a rule from the original spec, not modified by Otakar
rule decreaseInERC20(method f) {
    address token;
    uint256 before = erc20helper.tokenBalanceOf(token, currentContract);

    env e;
	calldataarg arg;
    f(e, arg);

    uint256 after = erc20helper.tokenBalanceOf(token, currentContract);

    assert after >= before ||  false ; /* fill in cases eth can decrease */ 

} 

//
//Here we start with Otakar's rules
//


rule burnRevertingConditions() {
    env e;
    address account;
    uint256 amount;

    bool zeroAddress = account == 0;
    bool notEnoughBalance = balanceOf(account) < amount;
    bool shouldRevert = zeroAddress || notEnoughBalance;

    burn@withrevert(account, amount);
    if(lastReverted){
        assert shouldRevert;
    } else {
        assert !shouldRevert;
    }
}

rule burnBurnAndJustTheOneAccount() {
    env e;
	address addr;
	uint256 amount;

    address addr2;
    require addr != addr2;
    	
	uint256 before = balanceOf(addr);
    uint256 before2 = balanceOf(addr2);
	burn(e, addr, amount);
    assert balanceOf(addr) == assert_uint256(before - amount);
    assert balanceOf(addr2) == before2;
}

rule mintRevertingConditions() {
    env e;
    address account;
    uint256 amount;

    bool zeroAddress = account == 0;
    bool balanceWouldOverflow = balanceOf(account) + amount > max_uint;
    //we could check also the total supply overflow, but that is handled by the invariant we have
    // [totalSupplyIsSumOfBalances]
    bool shouldRevert = zeroAddress || balanceWouldOverflow;

    mint@withrevert(account, amount);
    if(lastReverted){
        assert shouldRevert;
    } else {
        assert !shouldRevert;
    }
}

rule mintMintsAndJustTheOneAccount() {
	env e;
	address addr;
	uint256 amount;
	require amount > 0;
    address addr2;

    require addr != addr2;
	
	uint256 before = balanceOf(addr);
    uint256 before2 = balanceOf(addr2);
	mint(e, addr, amount);
    assert balanceOf(addr) == assert_uint256(before + amount);
    assert balanceOf(addr2) == before2;
}


rule decreaseAllowanceWorks() {
	env e;
	address owner = e.msg.sender;
	address spender;

	uint256 allowedBefore = allowance(owner, spender);
	uint256 subtractedValue;

	decreaseAllowance(e, spender, subtractedValue);
	assert allowance(owner, spender) == assert_uint256(allowedBefore - subtractedValue);	
}

rule decreaseAllowanceDoesNotAffectAnotherParty1() {
	env e;
	address owner = e.msg.sender;
	address spender;
    address nonSpender;
    require nonSpender != spender;

	uint256 nonspenderAllowedBefore = allowance(owner, nonSpender);
	uint256 subtractedValue;

	decreaseAllowance(e, spender, subtractedValue);
    assert allowance(owner, nonSpender) == nonspenderAllowedBefore;
}

rule decreaseAllowanceDoesNotAffectAnotherParty2() {
	env e;
	address owner = e.msg.sender;
	address ownerSpender;
    address nonOwner;
    address nonOwnerSpender;
    require nonOwner != owner;

    uint256 nonOwnerSpenderAllowance = allowance(nonOwner, nonOwnerSpender);

	uint256 subtractedValue;

	decreaseAllowance(e, spender, subtractedValue);
    assert allowance(nonOwner, nonOwnerSpender) == nonOwnerSpenderAllowance;
}

rule decreaseAllowanceRevertingConditions() {
    ..TODO..
}


rule increaseAllowanceAddsAllowance() {
	env e;
	address owner = e.msg.sender;
	address spender;

	uint256 allowedBefore = allowance(owner, spender);
	uint256 addedValue;
		
	increaseAllowance(e, spender, addedValue);
	assert allowance(owner, spender) == assert_uint256(allowedBefore + addedValue);	
}

rule decreaseAllowanceDoesNotAffectAnotherParty1() {
    ..TODO..
}

rule decreaseAllowanceDoesNotAffectAnotherParty2(){
    ..TODO..
}

rule increaseAllowanceRevertingConditions() {
    ..TODO..
}

//Martin has a same rule.
rule transferFromChangesStorageCorrectly() {
	env e;
	address spender = e.msg.sender;
	address owner;
	address recepient;

	uint256 allowedBefore = allowance(owner, spender);
	uint256 transfered;

	transferFrom(e, owner, recepient, transfered);
	uint256 allowedAfter = allowance(owner, spender);
	assert allowedBefore == assert_uint256(allowedAfter + transfered);


    ..TODO: check the balances of the two accounts..

    ..TODO: does not affect another party..
}

//TODO: make sure the rule passes
rule transferFromRevertingConditions() {
    address owner;
	env e;
	address spender = e.msg.sender;
	address recepient;

	uint256 allowed = allowance(owner, spender);
	uint256 transfered;

    bool zeroAddress = owner == 0 || receipent == 0;
    bool allowanceIsLow = allowed < trasfered;
    bool notEnoughBalance = balanceOf(owner) < transfered;
    bool overflow = balanceOf(recepient) + transfered > max_uint;

    bool isExpectedToRevert = zeroAddress || allowanceIsLow || enoughBalance || overflow;

    transferFrom@withrevert(e, owner, recepient, transfered);   

    if(lastReverted) {
        assert isExpectedToRevert;
    } else {
        assert !(isExpectedToRevert);
    }
}


rule approveSetsAllowance() {
	env e;
	address spender;
	address owner = e.msg.sender;
	uint amount;

	approve(e, spender, amount);
	uint256 allowed = allowance(owner, spender);
	assert allowed == amount;

    ..does not affect a third party..
}

rule approveRevertingConditions() {
    ..TODO..
}

rule onlyAllowedMethodsMayChangeBalance(method f) {
	env e;
	address addr;
	uint256 balanceBefore = balanceOf(addr);
	calldataarg args;
	f(e,args);
	uint256 balanceAfter = balanceOf(addr);
	assert balanceAfter > balanceBefore => canIncreaseBalance(f), "should not increase balance";
	assert balanceAfter < balanceBefore => canDecreaseBalance(f), "should not decrease balance";
}

//TODO: checked that [address] can only indeed change allowance[address]


rule onlyAllowedMethodsMayChangeAllowance(method f) {
	env e;
	address addr1;
	address addr2;
	uint256 allowanceBefore = allowance(addr1, addr2);
	calldataarg args;
	f(e,args);
	uint256 allowanceAfter = allowance(addr1, addr2);
	assert allowanceAfter > allowanceBefore => canIncreaseAllowance(f), "should not increase allowance";
	assert allowanceAfter < allowanceBefore => canDecreaseAllowance(f), "should not decrease allowance";
}

rule onlyAllowedMethodsMayChangeTotalSupply(method f) {
	env e;
	uint256 totalSupplyBefore = totalSupply();
	calldataarg args;
	f(e,args);
	uint256 totalSupplyAfter = totalSupply();
	assert totalSupplyAfter > totalSupplyBefore => canIncreaseTotalSupply(f), "should not increase total supply";
	assert totalSupplyAfter < totalSupplyBefore => canDecreaseTotalSupply(f), "should not decrease total supply";
}

invariant balanceOfZeroIsZero()
	balanceOf(0) == 0;

ghost mathint sumOfBalances {
	init_state axiom sumOfBalances == 0;
}

hook Sstore _balances[KEY address a] uint new_value (uint old_value) STORAGE {
	sumOfBalances = sumOfBalances + new_value - old_value;
	numberOfChangesOfBalances = numberOfChangesOfBalances + 1;
}

invariant totalSupplyIsSumOfBalances()
	to_mathint(totalSupply()) == sumOfBalances;

ghost mathint numberOfChangesOfBalances {
	init_state axiom numberOfChangesOfBalances == 0;
}

rule noMethodChangesMoreThanTwoBalances(method f) {
	env e;
	mathint numberOfChangesOfBalancesBefore = numberOfChangesOfBalances;
	calldataarg args;
	f(e,args);
	mathint numberOfChangesOfBalancesAfter = numberOfChangesOfBalances;
	assert numberOfChangesOfBalancesAfter <= numberOfChangesOfBalancesBefore + 2;
}

// We are checking just that if transfer(10) works, then also transfer(5);transfer(5) works. 
//We do not check the other direction (does not make sense becase of overflow reverts, i.e. does not hold)
rule transferIsOneWayAdditive() {
	env e;
	address recipient;
	uint256 amount_a; uint amount_b;
	mathint sum = amount_a + amount_b;
	require sum < max_uint256;
	storage init = lastStorage; // saves storage
	
	transfer(e, recipient, assert_uint256(sum));
	storage after1 = lastStorage;

	transfer@withrevert(e, recipient, amount_a) at init; // restores storage
		assert !lastReverted;	//if the transfer passed with sum, it should pass with both summands individually
	transfer@withrevert(e, recipient, amount_b);
		assert !lastReverted;
	storage after2 = lastStorage;

	assert after1[currentContract] == after2[currentContract];
}

//TODO: consider adding other additive rules



///
///
///  MARTIN
///
///


// /*
// 	Property: Checks precondition which guarantees that transer will not revert.c
// */
// rule transferRevert {
// 	address recipient;
// 	mathint amount;
// 	require(amount >= 0 && amount < max_uint256);
// 	env e;

// 	mathint balance_sender_before = balanceOf(e, e.msg.sender);
// 	require(balance_sender_before >= 0 && balance_sender_before < max_uint256);
// 	mathint allow = allowance(e, e.msg.sender, e.msg.sender);
// 	require (recipient != 0 && e.msg.sender != 0 && balance_sender_before >= amount
// 	&& e.msg.value != 0 && allow >= amount);

// 	transfer@withrevert(e, recipient, assert_uint256(amount));
// 	assert !lastReverted;
// }

/*
	Property: Increase of an allowance followed by its decrease results in the same allowance as was at the beginning of transaction.
*/
rule IncreaseAllowanceAndDecreaseAllowanceAreInverse {
	uint256 allowance;	
	address other;
	env e;

    storage initialStorage = lastStorage;

	uint256 beforeIncrease = allowance(e, e.msg.sender, other);
	increaseAllowance(e, other, allowance);
	decreaseAllowance(e, other, allowance);	
	assert beforeIncrease == allowance(e, e.msg.sender, other);

    uint256 beforeIncrease = allowance(e, e.msg.sender, other) at initialStorage;	
	decreaseAllowance(e, other, allowance);	
	increaseAllowance(e, other, allowance);
    assert beforeIncrease == allowance(e, e.msg.sender, other);
}

/*
  Property: A transfer performed between operations manipulating allowance does not influence allowance
  Notice: we consider change of allowance between sender and receipent which should be changed by transfer
*/
//This is currently implied by the rule [onlyAllowedMethodsMayChangeBalance]
// rule transferDoesNotChangeAllowance {
// 	mathint allowance;
// 	require(allowance >= 0 && allowance < max_uint256);
// 	address recipient;
// 	mathint amount;
// 	require(amount >= 0 && amount < max_uint256);
// 	env e;

// 	mathint beforeIncrease = allowance(e, e.msg.sender, recipient);
// 	transfer(e, recipient, assert_uint256(amount));
// 	mathint afterDecrease = allowance(e, e.msg.sender, recipient);

// 	assert beforeIncrease == afterDecrease;
// }

definition isMintOrBurn(method f) returns bool =
	f.selector == sig:burn(address,uint256).selector || f.selector == sig:mint(address,uint256).selector;


/*
	Property: Burn after mint, or mint after burn with the same amount should not change balance of the account.
	Notice: Rule takes the method f and according to its type chooses to perform burn or mint.
*/
rule mintOrBurn(method f) filtered {f -> isMintOrBurn(f)} {
	address account;
	uint256 amount;

    storage initialStorage = lastStorage;

	mathint accountBefore = balanceOf(e, account);
	mint(e, account, amount);
	burn(e, account, amount);
	assert(accountBefore == balanceOf(e, account));

	mathint accountBefore = balanceOf(e, account) at initialStorage;
	burn(e, account, amount);
	mint(e, account, amount);
	assert(accountBefore == balanceOf(e, account));
}


=== we ended here on August 10 at 14:21 ===

///// UNIT TEST /////
/*
  Property: Checks that the allowance between sender and msg.sender is changed correctly by transfer
  Same as [transferFromChangesStorageCorrectly]
*/
// rule allowanceSetByTransfer {
// 	address recipient;
// 	address sender;
// 	mathint amount;
// 	env e;
// 	storage initial = lastStorage;
//
// 	mathint allowanceBefore = allowance(e, sender, e.msg.sender);
// 	require(amount >= 0 && amount < max_uint256);
// 	transferFrom@withrevert(e, sender, recipient, assert_uint256(amount));
// 	bool succeeded = !lastReverted;
// 	mathint allowanceAfter = allowance(e, sender, e.msg.sender);
//
// 	assert succeeded => (allowanceBefore - amount == allowanceAfter || e.msg.sender == sender);
// }

//// SYSTEM STATE ////
/*
  Property: all deposits must be greater or equal to withdraws for all methods with exception of burn
  Notice: in case of burn, one can burn from initial _totalSupply
*/
ghost mathint totalWithdraw {
	init_state axiom totalWithdraw == 0;
}

ghost mathint totalDeposit {
	init_state axiom totalDeposit == 0;
}
ghost mapping(address => bool) increasedBalances;

hook Sstore _balances[KEY address a] uint256 newBalance (uint256 oldBalance) STORAGE {
	if (newBalance >= oldBalance) {
		totalDeposit = totalDeposit + newBalance - oldBalance;
		increasedBalances[a] = true;
	} else {
		totalWithdraw = totalWithdraw + oldBalance - newBalance;
		increasedBalances[a] = false;
	}
}

invariant positiveBalance()
	totalWithdraw <= totalDeposit
	filtered {f -> f.selector != sig:burn(address,uint256).selector}

//// HIGH LEVEL RULE & RISK ANALYSIS ////
/*
 	Property: There must be a way how to eventually increase a balance of someonelse than the owner
	Note: The rule just checks if implementation is not scam.
 */

// definition canIncrease(method f) returns bool =
// 	f.selector == sig:mint(address,uint256).selector || f.selector == sig:transfer(address,uint256).selector || f.selector == sig:transferFrom(address, address, uint256).selector;
// Probably implied by the correct changes of balance
//rule mustIncreaseAccount(method f) filtered {f -> canIncrease(f)} {
//	env e;
//	calldataarg args;
//
//	f(e,args);
//
//	address a;
//	address owner = _owner();
//
//	require(a != owner);
//	satisfy !increasedBalances[a];
// }


// ghost bool allowanceStore;
// ghost address allowanceOwner;
// ghost address allowanceSender;
// ghost uint256 allowanceValue;
// hook Sload uint256 v _allowances[KEY address a][KEY address b] STORAGE {
// 	allowanceOwner = a;
// 	allowanceSender = b;
// 	allowanceValue = v;
// }
//
// hook Sstore _allowances[KEY address a][KEY address b] uint256 v STORAGE {
// 	allowanceStore = true;
// }

/*
    Property: If one checks allowance of two addressed, the allowances mapping must be accessed.
	Done by [decreaseAllowanceDoesNotAffectAnotherParty2]
*/
// rule allowanceAccessAllowances() {
// 	address owner;
// 	address sender;
// 	env e;
//
// 	require(allowanceStore == false);
// 	uint256 v = allowance(e, owner, sender);
// 	assert(allowanceOwner == owner);
// 	assert(allowanceSender == sender);
// 	assert(v == allowanceValue);
// 	assert(allowanceStore == false);
// }


///
///
///  ANTTI
///
///


ghost mapping(address => uint256) balances;
ghost mathint sumOfBalances {
    init_state axiom sumOfBalances == 0;
}

hook Sstore _balances[KEY address u] uint256 newBalance (uint256 oldBalance) STORAGE {
    balances[u] = newBalance;
    sumOfBalances = sumOfBalances + newBalance - oldBalance;
}

rule transferRevertingConditions {
	env e;
	address recipient;
	uint256 amount;
    require e.msg.value == 0;

	bool senderBalanceTooLow = balanceOf(e.msg.sender) < amount;
    bool zeroRecipient = recipient == 0;
    bool zeroSender = e.msg.sender == 0;
    bool senderIsRecipient = e.msg.sender == recipient;

    bool recipientBalanceOverflows = balanceOf(recipient) + amount > max_uint256 && !senderIsRecipient;

    bool shouldRevert = senderBalanceTooLow || zeroRecipient || zeroSender || recipientBalanceOverflows;

	transfer@withrevert(e, recipient, amount);
    if (lastReverted) {
        assert shouldRevert;
    } else {
        assert !shouldRevert;
    }
}

// Antt: This rule is strange, transfer doesn't require approve
//rule transferIsPossible {
//	address recipient;
//	uint256 amount;
//	env e;
//    require e.msg.value == 0;
//
//	uint256 balance_sender_before = balanceOf@withrevert(e, e.msg.sender);
//    assert !lastReverted, "balanceOf reverted";
//
//	require (recipient != 0);
//    require (e.msg.sender != 0);
//    require (balance_sender_before >= amount);
//    require (recipient != e.msg.sender);
//
//    approve@withrevert(e, e.msg.sender, amount);
//    assert !lastReverted, "approve reverted";
//	require (allowance(e, e.msg.sender, e.msg.sender) >= amount);
//    
//    require balanceOf(e, recipient) == balances[recipient];
//    require totalSupply(e) - amount >= 0; // In mathint
//    require assert_uint256(totalSupply(e) - amount) >= balances[recipient];
//
//	transfer@withrevert(e, recipient, amount);
//	assert !lastReverted, "transfer reverted when ${e.msg.sender} sent to ${recipient}";
//
//}

// Antti: This rule checks that receiver receives correctly the sent funds.  It should be inserted as part of [transferFromChangesStorageCorrectly]
rule transferFromDoesNotHaveFee {
    env e;
    require e.msg.value == 0;
    address sender;
    address receiver;
    uint256 amount;

    bool senderIsReceiver = sender == receiver;

    uint256 balanceBefore = balanceOf(receiver);

    transferFrom(e, sender, receiver, amount);

    uint256 balanceAfter = balanceOf(e, receiver);

    if (senderIsReceiver) {
        assert balanceAfter == balanceBefore;
    } else {
        assert balanceAfter == assert_uint256(balanceBefore + amount);
    }
}

// Cannot send more than spending limit
// risk analysis
// Antti: This rule is implied by [transferFromRevertingConditions]
//rule transferFromRevertsWhenExceedingAllowance(address spender, address receiver, uint256 limit) {
//    env e;
//    require e.msg.value == 0;
//    require spender != 0;
//    require receiver != 0;
//    require e.msg.sender != 0;
//
//    approve@withrevert(e, spender, limit);
//    assert !lastReverted, "approve failed";
//
//    uint256 actual;
//
//    require actual > limit;
//
//    env e2;
//    require e2.msg.sender != e.msg.sender;
//    require e2.msg.sender == spender;
//    require e2.msg.value == 0;
//
//    transferFrom@withrevert(e2, e.msg.sender, receiver, actual);
//    assert lastReverted, "Overspent";
//}

// Authorised spender can spend
// Unit test
// Antti: This rule is implied by [transferFromRevertingConditions]
//rule transferFromSucceedsOnAuthorisedSpender(address spender, address receiver) {
//    env e;
//    require e.msg.value == 0;
//    require spender != 0;
//    require receiver != 0;
//    require e.msg.sender != 0;
//
//    uint256 limit;
//
//    approve@withrevert(e, spender, limit);
//    assert !lastReverted, "approve failed";
//
//    env e2;
//    require e2.msg.sender != e.msg.sender;
//    require e2.msg.sender == spender;
//    require e2.msg.value == 0;
//
//    uint256 actual;
//    require actual <= limit;
//
//    require balanceOf(e, e.msg.sender) >= limit;
//
//    require totalSupply(e) - actual >= 0;
//    require assert_uint256(totalSupply(e) - actual) >= balanceOf(e2, receiver);
//
//
//    transferFrom@withrevert(e2, e.msg.sender, receiver, actual);
//    assert !lastReverted, "authorised transfer failed";
//}

// Antti: This rule is implied by [transferFromRevertingConditions], a special case allowance < transferred
//rule transferFromFailsOnUnauthorisedSpender {
//    env e;
//    require e.msg.value == 0;
//    address spender;
//    address receiver;
//    require spender != 0;
//    require receiver != 0;
//    require e.msg.sender != 0;
//
//    uint256 limit;
//
//    approve@withrevert(e, spender, limit);
//    assert !lastReverted, "approve failed";
//
//    env e2;
//    require e2.msg.sender != e.msg.sender;
//    require e2.msg.sender != spender;
//    require e2.msg.value == 0;
//
//    uint256 actual;
//    require actual <= limit;
//    require actual > 0;
//
//    require balanceOf(e, e.msg.sender) >= limit;
//
//    require totalSupply(e) - actual >= 0;
//    require assert_uint256(totalSupply(e) - actual) >= balanceOf(e2, receiver);
//    require allowance(e2, e.msg.sender, e2.msg.sender) == 0;
//
//    transferFrom@withrevert(e2, e.msg.sender, receiver, actual);
//    assert lastReverted, "unauthorised transfer succeeded";
//}

// Unit test
// Antti: This rule is a special case of [onlyAllowedMethodsMayChangeTotalSupply]
//rule transferFromDoesntChangeTotalSupply(address alice, address bob, uint256 amount) {
//    env e;
//    require e.msg.value == 0;
//    uint256 supplyBefore = totalSupply@withrevert(e);
//
//    transferFrom@withrevert(e, alice, bob, amount);
//
//    uint256 supplyAfter = totalSupply@withrevert(e);
//
//    assert supplyBefore == supplyAfter;
//}
//
// Unit test


// Antti: This rule should be inserted to [mintMintsAndJustTheOneAccount]
rule mintIncreasesTotalSupply() {
    env e;
    require e.msg.value == 0;

    address destination;
    uint256 amount;

    uint256 prevTotalSupply = totalSupply();

    mint(e, destination, amount);

    assert totalSupply() == assert_uint256(prevTotalSupply + amount);
}

// Antti: This rule should be added to [mintRevertingConditions]
rule onlyOwnerCanMint() {
    env e;
    require e.msg.value == 0;
    address destination;
    uint256 amount;
    address nonDeployer;

    require e.msg.sender != currentContract._owner;
    mint@withrevert(e, destination, amount);
    assert lastReverted, "non-owner can mint";
}

// If something is transferred, allowance decreases by that amount
rule allowanceDecreasesWithTransfer() {
    address spender;
    address receiver;
    uint256 allowance;
    uint256 amount;

    require amount <= allowance;

    require spender != 0;
    require receiver != 0;

    env e;
    require e.msg.value == 0;

    require e.msg.sender != 0;
    approve@withrevert(e, spender, allowance);
    assert !lastReverted, "approve reverted";

    env e2;
    require e2.msg.value == 0;

    require e2.msg.sender == spender;

    require totalSupply@withrevert(e) - amount >= 0;
    assert !lastReverted, "totalSupply reverted";

    require balanceOf(e, e.msg.sender) >= amount;

    require balanceOf@withrevert(e, receiver) + amount <= to_mathint(totalSupply(e));
    assert !lastReverted, "balanceOf reverted";

    transferFrom@withrevert(e2, e.msg.sender, receiver, amount);
    assert !lastReverted, "transfer reverted";

    uint256 newAllowance = allowance@withrevert(e, e.msg.sender, spender);
    assert !lastReverted, "allowance query reverted";
    assert allowance - newAllowance == to_mathint(amount), "Incorrect allowance update";
}


///
///
///  DOMINIK
///
///

function ownerOnlyOperation(method f) returns bool {
    return f.selector == sig:mint(address, uint256).selector || f.selector == sig:burn(address, uint256).selector;
}


rule totalSupplyChangesByMintOrBurnOnly(method f) {
    env e;
    calldataarg args;

    mathint totalSupplyBefore = totalSupply();
    f(e,args);
    mathint totalSupplyAfter = totalSupply();

    // assert (totalSupplyBefore != totalSupplyAfter) => (f.selector == sig:mint(address,uint256).selector || f.selector == sig:burn(address,uint256).selector);
    assert (totalSupplyBefore > totalSupplyAfter) => (f.selector == sig:burn(address,uint256).selector);
    assert (totalSupplyBefore < totalSupplyAfter) => (f.selector == sig:mint(address,uint256).selector);
}


rule transferRecipientCannotBeZero() {
    env e;

    address account;
    uint256 amount;

    transfer(e, account, amount);

    assert account != 0;
}

rule balanceChangesByMintBurnOrTransferOnly(method f) {
    env e;
    calldataarg args;
    address account;

    mathint balanceBefore = balanceOf(account);
    f(e,args);
    mathint balanceAfter = balanceOf(account);

    assert (balanceBefore > balanceAfter) => (
        f.selector == sig:burn(address,uint256).selector ||
        (f.selector == sig:transfer(address,uint256).selector && account == e.msg.sender) ||
        f.selector == sig:transferFrom(address,address,uint256).selector
    );

    assert (balanceBefore < balanceAfter) => (
        f.selector == sig:mint(address,uint256).selector ||
        f.selector == sig:transfer(address,uint256).selector ||
        f.selector == sig:transferFrom(address,address,uint256).selector
    );
}

rule transferUpdatesBalancesCorrectly() {
    env e;
    address account;
    uint256 amount;

    require account != e.msg.sender;

    mathint balanceBefore = balanceOf(account);
    mathint balanceOfSenderBefore = balanceOf(e.msg.sender);

    transfer(e,account,amount);
    assert balanceOfSenderBefore >= to_mathint(amount);
    
    mathint balanceAfter = balanceOf(account);
    mathint balanceOfSenderAfter = balanceOf(e.msg.sender);

    assert balanceAfter == balanceBefore + amount;
    assert balanceOfSenderAfter == balanceOfSenderBefore - amount;

    ..TODO.. third party
}

rule transferRevertingConditions {
    ..TODO..
}

rule transferToMyselfDoesNotChangeBalance() {
    env e;
    address account;
    uint256 amount;
    require account == e.msg.sender;

    mathint balanceBefore = balanceOf(account);

    transfer(e,account,amount);
    assert balanceBefore >= to_mathint(amount);
    
    mathint balanceAfter = balanceOf(account);

    assert balanceAfter == balanceBefore;
}

rule transferDoesNotEffectUnintendedAccounts() {
    env e;
    address account;
    address unintendedAccount;
    uint256 amount;

    require account != unintendedAccount;
    require e.msg.sender != unintendedAccount;

    mathint balanceBefore = balanceOf(unintendedAccount);

    transfer(e,account,amount);

    mathint balanceAfter = balanceOf(unintendedAccount);

    assert balanceBefore == balanceAfter;
}

rule transferFromIncreasesBalanceByAmount() {
    env e;
    address sender;
    address recipient;
    uint256 amount;
    
    require recipient != sender;

    mathint balanceOfRecipientBefore = balanceOf(recipient);
    mathint balanceOfSenderBefore = balanceOf(sender);
    mathint allowanceBefore = allowance(sender, e.msg.sender);

    transferFrom(e,sender, recipient, amount);
    assert sender != 0 && recipient != 0;
    assert balanceOfSenderBefore >= to_mathint(amount);
    assert allowanceBefore >= to_mathint(amount);

    mathint balanceOfRecipientAfter = balanceOf(recipient);
    mathint balanceOfSenderAfter = balanceOf(sender);
    mathint allowanceAfter = allowance(sender,e.msg.sender);

    assert balanceOfRecipientAfter == balanceOfRecipientBefore + amount;
    assert balanceOfSenderAfter == balanceOfSenderBefore - amount;
    assert allowanceAfter == allowanceBefore - amount;
}


rule transferFromDoesNotUpdateBalanceIfSenderIsRecipient() {
    env e;
    address owner;
    uint256 amount;

    mathint balanceBefore = balanceOf(owner);
    mathint allowanceBefore = allowance(owner, e.msg.sender);

    transferFrom(e, owner, owner, amount);
    assert owner != 0;
    assert balanceBefore >= to_mathint(amount);
    assert allowanceBefore >= to_mathint(amount);

    mathint balanceAfter = balanceOf(owner);
    mathint allowanceAfter = allowance(owner,e.msg.sender);

    assert balanceBefore == balanceAfter;
    assert allowanceAfter == allowanceBefore - amount;
}


rule transferFromDoesNotEffectUnintendedAccounts() {
    env e;
    address sender;
    address recipient;
    address unintendedAccount;
    uint256 amount;

    require sender != unintendedAccount;
    require recipient != unintendedAccount;

    mathint balanceBefore = balanceOf(unintendedAccount);

    transferFrom(e,sender, recipient, amount);

    mathint balanceAfter = balanceOf(unintendedAccount);

    assert balanceBefore == balanceAfter;
}

rule onlyOwnerFunctionsCanBeCalledByOwnerOnly(method f) {
    env e;
    calldataarg args;
    require ownerOnlyOperation(f);

    f(e,args);
    assert e.msg.sender == _owner();
}



rule increaseAllowanceSetsAllowancesAsExpected() {
    env e;
    address spender;
    address randomAccount;
    address randomAccount2;
    uint256 amount;

    mathint allowanceBefore = allowance(e.msg.sender, spender);
    mathint anotherAllowanceBefore = allowance(e.msg.sender, randomAccount);
    mathint randomAllowanceBefore = allowance(randomAccount, randomAccount2);

    increaseAllowance(e, spender, amount);
    assert spender != 0;

    mathint allowanceAfter = allowance(e.msg.sender, spender);
    mathint anotherAllowanceAfter = allowance(e.msg.sender, randomAccount);
    mathint randomAllowanceAfter = allowance(randomAccount, randomAccount2);

    assert allowanceAfter == allowanceBefore + amount;
    assert randomAccount != spender => anotherAllowanceAfter == anotherAllowanceBefore;
    assert randomAccount != e.msg.sender => randomAllowanceBefore == randomAllowanceAfter;
}



rule decreaseAllowanceSetsAllowancesAsExpected() {
    env e;
    address spender;
    address randomAccount;
    address randomAccount2;
    uint256 amount;

    require e.msg.sender != randomAccount;

    mathint allowanceBefore = allowance(e.msg.sender, spender);
    mathint anotherAllowanceBefore = allowance(e.msg.sender, randomAccount);
    mathint randomAllowanceBefore = allowance(randomAccount, randomAccount2);

    decreaseAllowance(e, spender, amount);
    assert spender != 0;
    assert allowanceBefore >= to_mathint(amount);

    mathint allowanceAfter = allowance(e.msg.sender, spender);
    mathint anotherAllowanceAfter = allowance(e.msg.sender, randomAccount);
    mathint randomAllowanceAfter = allowance(randomAccount, randomAccount2);

    assert allowanceAfter == allowanceBefore - amount;
    assert randomAccount != spender => anotherAllowanceAfter == anotherAllowanceBefore;
    assert randomAccount != e.msg.sender => randomAllowanceBefore == randomAllowanceAfter;
}


rule approveSetsAllowancesAsExpected() {
    env e;
    address spender;
    address randomAccount;
    address randomAccount2;
    uint256 amount;

    mathint anotherAllowanceBefore = allowance(e.msg.sender, randomAccount);
    mathint randomAllowanceBefore = allowance(randomAccount, randomAccount2);

    approve(e, spender, amount);
    assert spender != 0;

    mathint allowanceAfter = allowance(e.msg.sender, spender);
    mathint anotherAllowanceAfter = allowance(e.msg.sender, randomAccount);
    mathint randomAllowanceAfter = allowance(randomAccount, randomAccount2);

    assert allowanceAfter == to_mathint(amount);
    assert randomAccount != spender => anotherAllowanceAfter == anotherAllowanceBefore;
    assert randomAccount != e.msg.sender => randomAllowanceBefore == randomAllowanceAfter;
}

 
rule mintIncreasesBalance() {
    env e;
    address account;
    address randomAccount;
    uint256 amount;

    require account != randomAccount;

    mathint balanceBefore = balanceOf(account);
    mathint randomBalanceBefore = balanceOf(randomAccount);
    mathint totalSupplyBefore = totalSupply();

    mint(e, account, amount);
    assert account != 0;

    mathint balanceAfter = balanceOf(account);
    mathint randomBalanceAfter = balanceOf(randomAccount);
    mathint totalSupplyAfter = totalSupply();

    assert balanceAfter == balanceBefore + amount;
    assert randomBalanceBefore == randomBalanceAfter;
    assert totalSupplyBefore + amount == totalSupplyAfter;
}


rule burnDecreasesBalance() {
    env e;
    address account;
    address randomAccount;
    uint256 amount;

    require account != randomAccount;

    mathint balanceBefore = balanceOf(account);
    mathint randomBalanceBefore = balanceOf(randomAccount);
    mathint totalSupplyBefore = totalSupply();

    burn(e, account, amount);
    assert account != 0;
    assert balanceBefore >= to_mathint(amount);

    mathint balanceAfter = balanceOf(account);
    mathint randomBalanceAfter = balanceOf(randomAccount);
    mathint totalSupplyAfter = totalSupply();

    assert balanceAfter == balanceBefore - amount;
    assert randomBalanceBefore == randomBalanceAfter;
    assert totalSupplyBefore  - amount == totalSupplyAfter;
}


// ghost mathint sumOfBalances{
//     init_state axiom sumOfBalances == 0;
// }

// hook Sstore _balances[KEY address addr] uint256 new_balance (uint256 old_balance) STORAGE {
//     sumOfBalances = sumOfBalances + to_mathint(new_balance) - to_mathint(old_balance);
// }

// hook Sload uint256 value _balances[KEY address addr] STORAGE {
//     require to_mathint(value) <= sumOfBalances;
// }

// invariant sumOfBalancesEqualsTotalSupply()
//     sumOfBalances == to_mathint(totalSupply());



///
///
///  JAROSLAV
///
///

/*

	Functions to cover:
	- balanceOf
		- maybe, it is just a getter, so probably not
	- transfer (DONE for now)
		- rules: transferDoesTheTransfer
		- we check the possibly revert causes
		- we check that the balance is indeed transfered
		- the fact that it cannot change the totalSupply is covered by another rule & invariant
		- we check that transfer does not affect a third 
	- approve (TODO)
		- rules:
		- check revert causes
		- check nonzero address (a revert cause)
		- check that it does not affect a third party
	

*/

/*
	Assume we want to do two seemingly independet transfers:
	1. transfer [amount_A] from [e_A.msg.sender] to [to_A], and
	2. transfer [amount_B] from [e_B.msg.sender] to [to_B],
	such that [e_A.msg.sender != e_B.msg.sender] and [to_A != to_B]. 
	This rule checks that the fact whether the transfer A reverts or not
	does not depend on the order of the two transfers. (the case for B follows).
*/
rule orderOfIndependentTransfersDoesNotAffectReverting(
	env e_A, 
	address to_A, 
	uint256 amount_A,
	env e_B, 
	address to_B,
	uint256 amount_B
) {
	require (e_A.msg.sender != e_B.msg.sender) || 
		(to_mathint(balanceOf(e_A, e_A.msg.sender)) >= amount_A + amount_B);
	require to_B != e_A.msg.sender;
	require (to_A != to_B) ||
		(to_mathint(balanceOf(e_A, to_A)) + amount_A + amount_B <= max_uint);


	storage initialStorage = lastStorage;

	transfer@withrevert(e_A, to_A, amount_A);
	bool ARevertedAtS1 = lastReverted;

	transfer(e_B, to_B, amount_B) at initialStorage;
	transfer@withrevert(e_A, to_A, amount_A);
	bool ARevertedAtS2 = lastReverted;

	assert (ARevertedAtS1 == ARevertedAtS2);
	// the other assert, over B, should be symteric, so no need to prove.
}

/*
	Here we cover only the case where e.msg.sender != to. The case when e.msg.sender is handled by [transferToMyself].
	In particular, we check that:
		1. we cover all the rever cases
		2. the amount is indeed transfered
*/

rule transferDoesTheTransfer(address to, uint256 amount) {
	env e;

	require e.msg.sender != to;
	uint256 initialFromBalance = balanceOf(e, e.msg.sender);
	uint256 initialToBalance = balanceOf(e, to);
	
	bool insufficientFunds = initialFromBalance < amount;
	//the overflow should not be possible if the invariant [somOfBalancesEqualsTotalSupply] holds.
	//So, alternatively, we should require the invariant here. 
	bool wouldOverflow =  initialToBalance + amount > max_uint;
	bool nonZeroAddress = (e.msg.sender == 0) || (to == 0 );
	
	transfer@withrevert(e, to, amount);

	if(lastReverted){	
		//check that it reverted due to one of the expected cases
		assert insufficientFunds || wouldOverflow || nonZeroAddress;
	} else {
		//check that none of the cases that we belive should trigger a revert did not apply
		assert !(insufficientFunds || wouldOverflow || nonZeroAddress);		
		//check that the balance was indeed transfered
		assert to_mathint(balanceOf(e, to)) == initialToBalance + amount;
		assert to_mathint(balanceOf(e, e.msg.sender)) == initialFromBalance - amount;		
	}
}

/*
	Check that:
		1. If I transfer the tokens to myself, my balance does not change. 
		2. that we cover all revert cases.
*/
rule transferToMyself(uint256 amount) {
	env e;
	uint256 balanceBefore = balanceOf(e, e.msg.sender);
	bool zeroAddress = e.msg.sender == 0;
	transfer@withrevert(e, e.msg.sender, amount);
	if(lastReverted) {	
		assert zeroAddress || balanceBefore < amount;
	} else {
		assert !(zeroAddress || balanceBefore < amount);
		assert balanceOf(e, e.msg.sender) == balanceBefore;
	}
	
}



/*
	The below function just calls (dispatch) all methods (an arbitrary one) from the contract, 
	using given [env e], [address from] and [address to].
	We use this function in several rules, including: . The usecase is typically to show that 
	the call of the function does not affect a "property" of a third party (i.e. != e.msg.sender, from, to),
	such as the balance or allowance.  

*/
function callFunctionWithParams(env e, method f, address from, address to) {
	uint256 amount;

	if (f.selector == sig:transfer(address, uint256).selector) {
		transfer(e, to, amount);
	} else if (f.selector == sig:allowance(address, address).selector) {
		allowance(e, from, to);
	} else if (f.selector == sig:approve(address, uint256).selector) {
		approve(e, to, amount);
	} else if (f.selector == sig:transferFrom(address, address, uint256).selector) {
		transferFrom(e, from, to, amount);
	} else if (f.selector == sig:increaseAllowance(address, uint256).selector) {
		increaseAllowance(e, to, amount);
	} else if (f.selector == sig:decreaseAllowance(address, uint256).selector) {
		decreaseAllowance(e, to, amount);
	} else if (f.selector == sig:mint(address, uint256).selector) {
		mint(e, to, amount);
	} else if (f.selector == sig:burn(address, uint256).selector) {
		burn(e, from, amount);
	} else {
		calldataarg args;
		f(e, args);
	}
}

/*
	Given addresses [e.msg.sender], [from], [to] and [thirdParty], we check that 
	there is no method [f] that would:
	1] not take [thirdParty] as an input argument, and
	2] yet changed the balance of [thirdParty].
	Intuitively, we target e.g. the case where a transfer of tokens [from] -> [to]
	changes the balance of [thirdParty]. 
*/
rule doesNotAffectAThirdPartyBalance(method f) {
	env e;	
	address from;
	address to;
	address thirdParty;

	require (thirdParty != from) && (thirdParty != to) && (thirdParty != e.msg.sender);

	uint256 thirdBalanceBefore = balanceOf(e, thirdParty);
	callFunctionWithParams(e, f, from, to);

	assert balanceOf(e, thirdParty) == thirdBalanceBefore;
}

/*
	Given addresses [e.msg.sender], [from], [to] and [thirdParty], we check that 
	there is no method [f] that would:
	1] not take [thirdParty] as an input argument, and
	2] yet changed the allowance of [thirdParty] w.r.t a [thirdPartySpender].
*/
rule doesNotAffectAThirdPartyAllowance(method f) {
	env e;	
	address from;
	address to;
	address thirdParty;
	address thirdPartySpender;

	require (thirdParty != from) && (thirdParty != to) && (thirdParty != e.msg.sender);

	uint256 spenderAllowanceBefore = allowance(e, thirdParty, thirdPartySpender);
	callFunctionWithParams(e, f, from, to);

	assert allowance(e, thirdParty, thirdPartySpender) == spenderAllowanceBefore;
}



ghost mathint sumOfBalances {
	init_state axiom sumOfBalances == 0;
}

hook Sstore _balances[KEY address addr] uint256 new_balance (uint256 old_balance) STORAGE {	
	sumOfBalances = sumOfBalances + to_mathint(new_balance) - to_mathint(old_balance);
}

hook Sload uint256 v _balances[KEY address addr] STORAGE {	
	require to_mathint(v) <= sumOfBalances;
}

invariant somOfBalancesEqualsTotalSupply(env e)
	sumOfBalances == to_mathint(totalSupply(e));




/*
	List of functions we assume are allowd to change the [totalSupply]
*/

definition canChangeTotalSupply(method f ) returns bool = 
	f.selector == sig:mint(address,uint256).selector ||
	f.selector == sig:burn(address,uint256).selector
	;

/*
	Functions that are not not allowed to change the [totalSupply] (via [canChangeTotalSupply()])
	do not change the total balance.
*/
rule totalSuppyDoesNotChange(method f) filtered {f -> !canChangeTotalSupply(f) } 
{		
	env e;
	calldataarg args;

	uint256 before = totalSupply(e);
	f(e,args);
    uint256 after = totalSupply(e);
	assert before == after;
}

/*
	Mint is one of the functions that can change the total balance (can it?). So, we check whether it does it correctly.
*/
rule mintIncreasesTheTotalBalanceCorrectly(address to, uint256 amount) {
	env e;
	
	uint256 before = totalSupply(e); //Question: how does the type cast work here?
	mint(e, to, amount);
	uint256 after = totalSupply(e);
	
	assert assert_uint256(before + amount) == after; 
}

rule mintCanBeDoneOnAnyAddresWithAnyReasonableAmount(address to, uint256 amount) {
	env e;

	require e.msg.sender == _owner(e);
	//we can, instead, require the invariant somOfBalancesEqualsTotalSupply here I suppose. But that might be a too strong requirement. 
	require totalSupply(e) + amount < max_uint; 
	require balanceOf(e, to) + amount < max_uint;
	require to != 0;
	
	mint@withrevert(e, to, amount);

	assert !lastReverted;
}

/*
	Burn is one of the functions that can change the total balance (can it?). So, we check whether it does it correctly.
*/
rule burnDecreasesTheTotalBalanceCorrectly(address from, uint256 amount) {
	env e;
	
	uint256 before = totalSupply(e); 
	burn(e, from, amount);
	uint256 after = totalSupply(e);
	
	assert amount <= before; //just checking if the compiler (with safe math) handles underflows correctly
	assert assert_uint256(before - amount) == after; 
}

rule burnCanBeDoneOnAnyAddresWithAnyReasonableAmount(address from, uint256 amount) {
	env e;

	require e.msg.sender == _owner(e);
	require balanceOf(e, from) >= amount;
	//we can, instead, require the invariant somOfBalancesEqualsTotalSupply here I suppose. But that might be a too strong requirement. 
	require amount <= totalSupply(e); 
	require from != 0;
	
	burn@withrevert(e, from, amount);

	assert !lastReverted;
}