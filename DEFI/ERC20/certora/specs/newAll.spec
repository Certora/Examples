methods {
    
    function totalSupply() external returns uint256 envfree;
    function balanceOf(address) external returns uint256 envfree;
	function allowance(address,address) external returns uint256 envfree;
    function approve(address,uint256) external returns bool;
	function increaseAllowance(address,uint256) external returns bool;
    function transfer(address,uint256) external returns bool;
    function transferFrom(address,address,uint256) external returns bool;
	function _owner() external returns address envfree;
	function deposit() external;
	function depositTo(address,uint256) external;
}

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
definition nonRevertingFunction(method f) returns bool = true; 

definition canIncreaseAllowance(method f) returns bool = 
	f.selector == sig:approve(address,uint256).selector || 
	f.selector == sig:increaseAllowance(address,uint256).selector;

definition canDecreaseAllowance(method f) returns bool = 
	f.selector == sig:approve(address,uint256).selector || 
	f.selector == sig:decreaseAllowance(address,uint256).selector ||
	f.selector == sig:transferFrom(address,address,uint256).selector;

definition canIncreaseBalance(method f) returns bool = 
	f.selector == sig:mint(address,uint256).selector || 
	f.selector == sig:transfer(address,uint256).selector ||
	f.selector == sig:transferFrom(address,address,uint256).selector ||
	f.selector == sig:deposit().selector ||
	f.selector == sig:depositTo(address,uint256).selector ||
	f.selector == sig:addAmount(uint256).selector ||
	f.selector == sig:withdraw(uint256).selector;

definition canDecreaseBalance(method f) returns bool = 
	f.selector == sig:burn(address,uint256).selector || 
	f.selector == sig:transfer(address,uint256).selector ||
	f.selector == sig:transferFrom(address,address,uint256).selector ||
	f.selector == sig:deposit().selector ||
	f.selector == sig:depositTo(address,uint256).selector ||
	f.selector == sig:addAmount(uint256).selector ||
	f.selector == sig:withdraw(uint256).selector;

definition priveledgedFunction(method f) returns bool = 
	f.selector == sig:mint(address,uint256).selector || 
	f.selector == sig:burn(address,uint256).selector;

definition canIncreaseTotalSupply(method f) returns bool = 
	f.selector == sig:mint(address,uint256).selector ||
	f.selector == sig:deposit().selector ||
	f.selector == sig:addAmount(uint256).selector;

definition canDecreaseTotalSupply(method f) returns bool = 
	f.selector == sig:burn(address,uint256).selector ||
	f.selector == sig:withdraw(uint256).selector;


// Note: Still reverts with unclear reason 
// rule noRevert(method f) filtered { f -> nonRevertingFunction(f) }
// {
// 	env e;
// 	calldataarg arg;
//     //consider auto filtering for non-payable functions 
// 	require e.msg.value == 0;
// 	f@withrevert(e, arg); 
// 	assert !lastReverted || (e.msg.sender != _owner() && priveledgedFunction(f)), "method should not revert";
// }

// Note: Need to check how to require overflows
// /* 
//     Property: Checks if a function can be frontrun.
// */ 
// rule simpleFrontRunning(method f, method g) filtered { f-> !f.isView, g-> !g.isView }
// {
// 	env e1;
// 	calldataarg arg1;

// 	storage initialStorage = lastStorage;
// 	// Note: We try to run f to make sure it was not reverted. If f reverts this case
//     // will not be considered.
//     f(e1, arg1);
	
// 	env e2;
// 	calldataarg arg2;
// 	require e2.msg.sender != e1.msg.sender;
// 	g(e2, arg2) at initialStorage; 

// 	f@withrevert(e1, arg1);
// 	bool succeeded = !lastReverted;

// 	assert succeeded, "should be called also if frontrunned";
// }

/** 
    @title -   This rule find which functions are privileged.
    @notice A function is privileged if there is only one address that can call it.
    @dev The rules finds this by finding which functions can be called by two different users.
*/
rule privilegedOperation(method f, address privileged) filtered {f -> priveledgedFunction(f) }
{
	env e1;
	calldataarg arg1;
	require e1.msg.sender == privileged;

	storage initialStorage = lastStorage;
	f@withrevert(e1, arg1); // privileged succeeds executing candidate privileged operation.
	bool firstSucceeded = !lastReverted;

	env e2;
	calldataarg arg2;
	require e2.msg.sender != privileged;
	f@withrevert(e2, arg2) at initialStorage; // unprivileged
	bool secondSucceeded = !lastReverted;

	assert  !(firstSucceeded && secondSucceeded), "function is privileged";
}

rule decreaseInSystemEth(method f) {
    uint256 before = nativeBalances[currentContract];

    env e;
	calldataarg arg;
    f(e, arg);

    uint256 after = nativeBalances[currentContract];

    assert after >= before || true; /* change true to fill in cases where eth can decrease */
}

rule decreaseInERC20(method f) {
    uint256 before = balanceOf(currentContract);

    env e;
	calldataarg arg;
    f(e, arg);

    uint256 after = balanceOf(currentContract);

    assert after >= before || true; /* change true to fill in cases token can decrease */ 
}

//
//Here we start with Otakar's rules
//

rule burnRevertingConditions() {
    env e;

	address account;
    uint256 amount;

	bool totalSupplyUnderFlow = totalSupply() - amount < 0;
	bool notOwner = e.msg.sender != _owner();
	bool notPayable = e.msg.value != 0;
    bool zeroAddress = account == 0;
    bool notEnoughBalance = balanceOf(account) < amount;
    bool shouldRevert = zeroAddress || notEnoughBalance || notPayable || notOwner || totalSupplyUnderFlow;

    burn@withrevert(e, account, amount);
    if(lastReverted) {
        assert shouldRevert;
    } 
    else {
        assert !shouldRevert;
    }
}

rule transferRevertingConditions() {
    env e;
	uint256 amount;
	address account;
	require e.msg.sender != account;

	bool overflow = balanceOf(account) + amount > max_uint256;
	bool notPayable = e.msg.value != 0;
    bool zeroAddress = e.msg.sender == 0 || account == 0;
    bool notEnoughBalance = balanceOf(e.msg.sender) < amount;
    bool shouldRevert = overflow || notPayable || zeroAddress || notEnoughBalance;
	

    transfer@withrevert(e, account, amount);
    if(lastReverted) {
        assert shouldRevert;
    } 
    else {
        assert !shouldRevert;
    }
}

rule burnIntegrity() {
    env e;
	address addr;
	uint256 amount;
    	
	uint256 before = balanceOf(addr);

    burn(e, addr, amount);
    assert balanceOf(addr) == assert_uint256(before - amount);
}

rule burnDoesNotAffectThirdParty() {
    env e;
	address addr1;
	uint256 amount;

    address addr2;
    require addr1 != addr2;

    uint256 before = balanceOf(addr2);

	burn(e, addr1, amount);
    assert balanceOf(addr2) == before;
}

rule mintRevertingConditions() {
    env e;
	address account;
    uint256 amount;

	bool nonOwner = e.msg.sender != _owner();
	bool nonPayable = e.msg.value != 0;
    bool zeroAddress = account == 0;
    bool overflow = balanceOf(account) + amount > max_uint || totalSupply() + amount > max_uint;
    bool shouldRevert = nonOwner || nonPayable || zeroAddress || overflow;

    mint@withrevert(e, account, amount);
    if(lastReverted){
        assert shouldRevert;
    } else {
        assert !shouldRevert;
    }
}

rule mintIntegrity() {
	env e;
	address addr;
	uint256 amount;
    require amount > 0;

	uint256 before = balanceOf(addr);
	
    mint(e, addr, amount);
    assert balanceOf(addr) == assert_uint256(before + amount);
}

rule mintDoesNotAffectThirdParty() {
	env e;
	address addr1;
	uint256 amount;
	require amount > 0;
    
    address addr2;
    require addr1 != addr2;
	
	uint256 before = balanceOf(addr2);
	
    mint(e, addr1, amount);
    assert balanceOf(addr2) == before;
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

rule decreaseAllowanceRevertingConditions(env e, address spender, uint256 subtractedValue) {
    require e.msg.value == 0; // prevents revert on sending eth to none payable function
	bool notEnoughAllowance = subtractedValue > allowance(e.msg.sender, spender);
	bool ownerZeroAddress = e.msg.sender == 0;
	bool spenderZeroAddress = spender == 0;
	bool shouldRevert = notEnoughAllowance || ownerZeroAddress || spenderZeroAddress;

    decreaseAllowance@withrevert(e, spender, subtractedValue);
    if(lastReverted) {
        assert shouldRevert;
    }
	else {
        assert !shouldRevert;
    }
}

rule increaseAllowanceWorks() {
	env e;
	address owner = e.msg.sender;
	address spender;

	uint256 allowedBefore = allowance(owner, spender);
	uint256 addedValue;
		
	increaseAllowance(e, spender, addedValue);
	assert allowance(owner, spender) == assert_uint256(allowedBefore + addedValue);	
}

rule increaseAllowanceRevertingConditions(env e, address spender, uint256 addedValue) {
	
	bool nonPayable = e.msg.value != 0;
	bool ownerZeroAddress = e.msg.sender == 0;
	bool spenderZeroAddress = spender == 0;
	bool overflow = allowance(e.msg.sender, spender) + addedValue > max_uint256;
	bool shouldRevert = overflow || nonPayable || ownerZeroAddress || spenderZeroAddress;

	increaseAllowance@withrevert(e, spender, addedValue);
	if(lastReverted) {
		assert shouldRevert;
	}
	else {
		assert !shouldRevert;
	}
}

/*
This rule checks that decreaseAllowence does not change the allowence
of the owner with a different spender.
*/
rule increaseAllowanceMethodsDoesNotAffectAnotherSpender(
	env e,
	address spender,
	address nonSpender,
	uint256 subtractedValue)  {
    require nonSpender != spender;

	uint256 nonSpenderAllowedBefore = allowance(e.msg.sender, nonSpender);

	increaseAllowance(e, spender, subtractedValue);
    
	assert allowance(e.msg.sender, nonSpender) == nonSpenderAllowedBefore;
}

/*
This rule checks that decreaseAllowence does not change the allowence
of the owner with a different spender.
*/
rule decreaseAllowanceMethodsDoesNotAffectAnotherSpender(
	env e,
	address spender,
	address nonSpender,
	uint256 subtractedValue)  {
    require nonSpender != spender;

	uint256 nonSpenderAllowedBefore = allowance(e.msg.sender, nonSpender);

	decreaseAllowance(e, spender, subtractedValue);
    
	assert allowance(e.msg.sender, nonSpender) == nonSpenderAllowedBefore;
}

/*
This rule checks that decreaseAllowence does not affect the allowences of other owners.
*/
rule increaseAllowanceMethodsDoesNotAffectAnotherOwnerAllowences(
	env e,
	address ownerSpender,
	address nonOwner,
	address nonOwnerSpender,
	uint256 subtractedValue) {
	require nonOwner != e.msg.sender;

    uint256 nonOwnerSpenderAllowance = allowance(nonOwner, nonOwnerSpender);
	
	increaseAllowance(e, ownerSpender, subtractedValue);
    
	assert allowance(nonOwner, nonOwnerSpender) == nonOwnerSpenderAllowance;
}

/*
This rule checks that decreaseAllowence does not affect the allowences of other owners.
*/
rule decreaseAllowanceMethodsDoesNotAffectAnotherOwnerAllowences(
	env e,
	address ownerSpender,
	address nonOwner,
	address nonOwnerSpender,
	uint256 subtractedValue) {
	require nonOwner != e.msg.sender;

    uint256 nonOwnerSpenderAllowance = allowance(nonOwner, nonOwnerSpender);
	
	decreaseAllowance(e, ownerSpender, subtractedValue);
    
	assert allowance(nonOwner, nonOwnerSpender) == nonOwnerSpenderAllowance;
}

//Martin has a same rule.
rule transferFromChangesStorageCorrectly() {
	env e;
	address spender = e.msg.sender;
	address owner;
	address recepient;
	address thirdParty;

	require owner != recepient;
	require thirdParty != owner && thirdParty != recepient;

	uint256 allowedBefore = allowance(owner, spender);
	uint256 ownerBalanceBefore = balanceOf(owner);
	uint256 recepientBalanceBefore = balanceOf(recepient);
	uint256 thirdPartyBalanceBefore = balanceOf(thirdParty);
	uint256 transfered;

	transferFrom(e, owner, recepient, transfered);

	uint256 ownerBalanceAfter = balanceOf(owner);
	uint256 recepientBalanceAfter = balanceOf(recepient);
	uint256 thirdPartyBalanceAfter = balanceOf(thirdParty);
	uint256 allowedAfter = allowance(owner, spender);
	
	assert allowedBefore == assert_uint256(allowedAfter + transfered);
	assert assert_uint256(ownerBalanceBefore - transfered) == ownerBalanceAfter;
	assert assert_uint256(recepientBalanceBefore + transfered) == recepientBalanceAfter;
	assert thirdPartyBalanceBefore == thirdPartyBalanceAfter;
}

//TODO: make sure the rule passes
rule transferFromRevertingConditions() {
    address owner;
	env e;
	address spender = e.msg.sender;
	address recepient;
	require owner != recepient;


	uint256 allowed = allowance(owner, spender);
	uint256 transfered;

	bool sendEthToNotPayable = e.msg.value != 0;
    bool zeroAddress = owner == 0 || spender == 0 || recepient == 0;
    bool allowanceIsLow = allowed < transfered;
    bool notEnoughBalance = balanceOf(owner) < transfered;
    bool overflow = balanceOf(recepient) + transfered > max_uint;

    bool isExpectedToRevert = sendEthToNotPayable || zeroAddress || allowanceIsLow || notEnoughBalance || overflow;

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
	address thirdParty; 
	uint amount;

	uint256 thirdPartyAllowanceBefore = allowance(thirdParty, spender);

	approve(e, spender, amount);
	uint256 allowed = allowance(owner, spender);
	assert allowed == amount;

	uint256 thirdPartyAllowanceAfter = allowance(thirdParty, spender);

    assert thirdPartyAllowanceBefore == thirdPartyAllowanceBefore;
}

rule approveRevertingConditions() {
    env e;
	address spender;
	address owner = e.msg.sender;
	uint256 amount;

	bool nonPayable = e.msg.value != 0;
	bool zeroAddress = owner == 0 || spender == 0;

	bool shouldRevert = zeroAddress || nonPayable;

	approve@withrevert(e, spender, amount);

	if(lastReverted){
		assert shouldRevert;
	} else {
		assert !shouldRevert;
	}
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
	assert f.selector == sig:depositTo(address,uint256).selector => (numberOfChangesOfBalancesAfter <= numberOfChangesOfBalancesBefore + 4);
	assert f.selector != sig:depositTo(address,uint256).selector => (numberOfChangesOfBalancesAfter <= numberOfChangesOfBalancesBefore + 2);
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
