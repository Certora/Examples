/**
  @title Storage Example
 
  This is an example specification for comparing storage (`lastStorage`) and `nativeBalances`.
  The spec demontstrates:
  1. Changes in storage in case of successful/unsuccessful transactions.
  2. Changes in `lastStorage` when changing data structures of the current contract.
  3. The relation between the balances of the sender and the receiver of a transaction.
  4. 
  

 */
 

using Bank as bank;

methods {
    function balanceOf(address)        external returns(uint) envfree;
    function balanceOfAccount(address user, uint account) external returns(uint) envfree;
    function totalSupply()             external returns(uint) envfree;
    function getCustomer(address a) external returns(BankAccountRecord.Customer) envfree;
    /// Definition of a compiler-generated method returning a struct as a tuple 
    function blackList(uint256) external returns (address, uint) envfree;
    /// Definition of a function with struct as an argument
    function addCustomer(BankAccountRecord.Customer) external envfree;
    function _.receiveCash() external => DISPATCHER(true);
}

/// withdraw from a non-empty account changes the storage state.
/// This rule should pass.
rule storageChangesByWithdrawFromNonEmptyAccount() {
    env e;
    storage init = lastStorage;
    uint256 accountNum;
    require balanceOfAccount(e.msg.sender, accountNum) > 0;
    withdraw(e, accountNum);
    storage after = lastStorage;
    assert (init != after, "withdraw from non-empty account does not change storage");
}

/// This rule demonstrates comparing storage with possible revert.
/// withdraw from a non-necessarily empty account might not change the state.
/// This rule fails because in case the withdrown account is empty the `withdraw` function revert and therefor the
/// balance is not changed.
rule storageChangesByWithdrawWithRevert() {
    env e;
    storage init = lastStorage;
    uint256 accountNum;

    withdraw@withrevert(e, accountNum);
    storage after = lastStorage;
    assert init != after;  
}

/// This rule demonstrates how to check changes in `lastStorage` when changing data structures of the current contract
/// Different storage after each customer addition.
/// The rule Should pass.
rule addingCustomersChangesStorageShouldPass(BankAccountRecord.Customer c1, BankAccountRecord.Customer c2) {
    require c1.id != c2.id;
    addCustomer(c1);
    storage afterC1 = lastStorage;
    addCustomer(c2);
    storage afterC2 = lastStorage;
    assert (afterC1 != afterC2, "Storage after adding one customer is the same as storage after adding two.");
}

/// Witness for different storage after each customer addition.
rule witnessForStorageChangeAfterEachCustomerAddition(BankAccountRecord.Customer c1, BankAccountRecord.Customer c2) {
    addCustomer(c1);
    storage afterC1 = lastStorage;
    addCustomer(c2);
    storage afterC2 = lastStorage;
    satisfy (afterC1 != afterC2);
}

/// This rule demonstrates how to compare the storage of the current contract and nativeBalances in several
/// points of the run. Using several variables and indices.
/// Different storage after each customer addition.
rule integrityOfStoragePerCustomerShouldPass(BankAccountRecord.Customer c1, BankAccountRecord.Customer c2) {
    require c1.id != c2.id;
    storage init = lastStorage;
    addCustomer(c1);
    storage afterC1 = lastStorage;
    addCustomer(c2);
    storage afterC2 = lastStorage;

    assert (afterC1[bank] != afterC2[bank], "Adding a customer does not affect storage");
    assert (init[currentContract] != lastStorage[currentContract], "Adding a customer does not affect storage of the current contract, bank ");
    assert (init[nativeBalances] == lastStorage[nativeBalances], "Change in storage affects native balances");
}

/// This rule demonstrates the difference from the previous rule in case there is not restriction on the balance of 
/// account so can be Zero.
/// Withdrawing balanceOfAccount(e.msg.sender, bankAccount) eth.
/// Therefore the rule fails.
rule withdrawDoesNotAffectNativeBalancesShouldFail() {
    uint256 bankAccount;
    env e;
    storage initBalance = lastStorage;
    uint256 balance = balanceOfAccount(e.msg.sender, bankAccount);
    require balance > 0; // balance should change by withdraw.
    bool success = withdraw(e, bankAccount);
    storage lastBalance = lastStorage;
    assert (success => (initBalance[nativeBalances] == lastBalance[nativeBalances]), "withdraw affects native balances");
}

/// Demonstrated how to compare nativeBalances in the init state and after a transaction.
/// The sum of balances of the sender and reciever does not change by deposit.
rule sumOfSenderAndReceiverDoesNotChangeByDeposit {
    uint256 bankAccount;
    env e;
    uint256 initBankBalance = nativeBalances[bank];
    uint256 initSenderBalance = nativeBalances[e.msg.sender];
    storage initStorage = lastStorage;
    require e.msg.value > 0; // balance should change by deposit.
    // deposit msg.value to account `bankAccount` and to the native balance of msg.sender.
    deposit(e, bankAccount);
    assert((nativeBalances[bank] + nativeBalances[e.msg.sender]) == (initBankBalance + initSenderBalance),
    "Sum of balances of sender and receiver changes by deposit.");
}

// deposit msg.value to this.
rule nativeBalanceChangesByDepositShouldPass() {
    uint256 bankAccount;
    env e;
    require e.msg.sender < max_address;
    require e.msg.sender != bank;
    uint256 initBalance = nativeBalances[bank];
    storage initStorage = lastStorage;
    require e.msg.value > 0; // balance should change by deposit.
    // deposit msg.value to account `bankAccount` and to the native balance of msg.sender.
    deposit(e, bankAccount);
    assert(nativeBalances[bank] != initBalance, "Balance of bank does not change by deposit");
}

rule witnessStorageChangesByWithdrawShouldPassInFixed() {
    uint256 bankAccount;
    env e;
    uint256 initBalance = nativeBalances[bank];
    storage initStorage = lastStorage;
    uint256 balance = balanceOfAccount(e.msg.sender, bankAccount);
    require balance > 0; // balance should change by withdraw.
    require e.msg.sender != currentContract;
    bool success = withdraw(e, bankAccount);
    satisfy(success => (lastStorgae[bank] != initStorage));
}

// withdraw that changes native balances.
// This rule fails without the optimistic_fallback argument to the prover because withdraw uses an unresolved "call"
// for the eth transfer which can result also unchanged balances.
// with optimistic_fallback the rule passes because it forces a balance change.
rule nativeBalanceDoesNotChangeByWithdrawShouldPassInFixed() {
    uint256 bankAccount;
    env e;
    uint256 initBalance = nativeBalances[bank];
    storage initStorage = lastStorage;
    uint256 balance = balanceOfAccount(e.msg.sender, bankAccount);
    require balance > 0; // balance should change by withdraw.
    require e.msg.sender != currentContract;
    bool success = withdraw(e, bankAccount);
    assert(success => (nativeBalances[bank] == initBalance), "Balance of bank does not change by withdraw");
}

/// two withdraws one after the other where both start from the initial state. Therefore, the balances after each of the
/// withdraws is the same.
/// This fails in the default configuration because of the call to an unresolved function in withdraw. 
/// It passes with -optimistic_fallback.
rule storageAfterTwoWithdrawFromInitDoesNotChangeShouldPass() {
    uint256 bankAccount;
    env e;
    require e.msg.sender < max_address;
    // uint256 initBalance = nativeBalances[bank];
    storage initStorage = lastStorage;
    // uint256 balance = balanceOfAccount(e.msg.sender, bankAccount);
    // uint256 balance = nativeBalances[e.msg.sender];
    // require balance > 0; // balance should change by withdraw.
    bool success1 = withdraw(e, bankAccount);
    storage afterWithdraw = lastStorage;
    uint256 afterWithdrawBalance = nativeBalances[bank];
    bool success2 = withdraw(e, bankAccount) at initStorage;
    assert((success1 && success2) => 
    (nativeBalances[bank] == afterWithdrawBalance), "Different native balances from same initial storage");
    assert((success1 && success2) => 
    (lastStorage[bank] == afterWithdraw[bank]), "Different native balances from same initial storage");
}

// Comparing nativeBalances after some method f.
rule parametericFunctionCanChangeBalance(method f) {
    env e;
    uint256 nativeBefore = nativeBalances[bank];    
    calldataarg args;
    f(e,args); /* check on all possible arguments */
    assert( nativeBalances[bank] != nativeBefore, "nativeBalances does not change by unresolved")  ;
}

rule witnessParametricFunctionCanChangeBalance(method f) {
    env e;
    uint256 nativeBefore = nativeBalances[bank];    
    calldataarg args;
    f(e,args); /* check on all possible arguments */
    satisfy nativeBalances[bank] != nativeBefore;
}

