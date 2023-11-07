/**
  @title Storage Example
 
  This is an example specification for comparing storage (`lastStorage`) and `nativeBalances`.
  The spec demontstrates:
  1. Changes in storage in case of successful/unsuccessful transactions.
  2. Changes in `lastStorage` when changing data structures of the current contract.
  3. The relation between the balances of the sender and the receiver of a transaction.
  4. Changes in ghost storage.
 */
 

using Bank as bank;

methods {
    function balanceOfAccount(address user, uint account) external returns(uint) envfree;
    /// Definition of a function with struct as an argument
    function addCustomer(BankAccountRecord.Customer) external envfree;
    function getNumberOfAccounts(address) external returns (uint256) envfree;
    function isCustomer(address) external returns (bool) envfree;
}

// This rule demonstrates comparing the full storage.
/// withdrawal from a non-empty account changes the storage state.
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

/// This rule demonstrates comparing full storage after a transaction with possible revert.
/// withdrawal from a non-necessarily empty account might not change the state.
/// This rule fails because when the withdrawn account is empty the `withdraw` function reverts and therefore the
/// storage is unaffected.
rule storageDoesNotChangeByWithdrawWhenRevert() {
    env e;
    storage init = lastStorage;
    uint256 accountNum;

    withdraw@withrevert(e, accountNum);
    storage after = lastStorage;
    assert (lastReverted => init == after, "Storage changes after revert.");  
}

/// This rule demonstrates how to verify changes in the full storage when changing data structures of the current contract.
/// The storage changes after each customer addition.
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
    require !isCustomer(c1.id);
    require !isCustomer(c2.id);
    addCustomer(c1);
    storage afterC1 = lastStorage;
    addCustomer(c2);
    storage afterC2 = lastStorage;
    satisfy (afterC1 != afterC2);
}

/// This rule demonstrates how to compare the storage of a specific contract and nativeBalances in several
/// points of the run using several variables and indices.
/// Different storage after each customer addition.
rule integrityOfStoragePerCustomerShouldPass(BankAccountRecord.Customer c1, BankAccountRecord.Customer c2) {
    require c1.id != c2.id;
    require !isCustomer(c1.id);
    require !isCustomer(c2.id);
    storage init = lastStorage;
    addCustomer(c1);
    storage afterC1 = lastStorage;
    addCustomer(c2);
    storage afterC2 = lastStorage;

    // comparing the storage of `bank` after one and two additions.
    assert (afterC1[bank] != afterC2[bank], "Adding a customer does not affect storage of bank");
    // comparing the storage of the current contract to its storage at the initial state.
    // currentContract is the same as `bank`.
    assert (init[currentContract] != lastStorage[currentContract], "Adding a customer does not affect storage of the current contract");
    // comparing the storage of the nativeBalances to nativeBalances at the initial state.
    assert (init[nativeBalances] == lastStorage[nativeBalances], "Change in storage affects native balances");
}


/// This rule demonstrates how to call `deposit` (can be any transaction) twice from the same state by restoring the storage to
/// its initial state before the second call.
/// Two withdrawals are sequentially called where both start from the initial state. Therefore, the storage after each of the
/// withdrawals are the same.
/// This fails in the default configuration because of the call to an unresolved function in withdraw. 
/// It passes with -optimistic_fallback.
rule storageAfterTwoDepositFromInitDoesNotChangeShouldPass() {
    uint256 bankAccount;
    env e;
    require e.msg.sender < max_address;
    // uint256 initBalance = nativeBalances[bank];
    storage initStorage = lastStorage;
    deposit(e, bankAccount);
    // Only full storage can be assigned to a variable.
    storage afterCallStorage = lastStorage;
    // nativeBalances is mapping(address => uint256. mapping is not yet supported as a CVL local variable type, so a variable
    // corresponds to a single entry is used instead.
    uint256 afterCallBalance = nativeBalances[bank];
    deposit(e, bankAccount) at initStorage;
    assert (nativeBalances[bank] == afterCallBalance, "Different native balances from same initial storage");
    assert(lastStorage[bank] == afterCallStorage[bank], "Different native storage from same initial storage");
    assert(lastStorage[nativeBalances] == afterCallStorage[nativeBalances], 
        "Different storage of native balances after call from same initial storage");
}

/// Mirror on a struct _customers[a].accounts[i].accountBalance
ghost mapping(address => mapping(uint256 => uint256)) accountBalanceMirror {
    init_state axiom forall address a. forall uint256 i. accountBalanceMirror[a][i] == 0;
}

// ghost for demonstrating storage of a ghost.
ghost mapping(address => mathint) numOfOperations {
    init_state axiom forall address a. numOfOperations[a] == 0;
}

/// hook on a complex data structure, a mapping to a struct with a dynamic array
hook Sstore _customers[KEY address a].accounts[INDEX uint256 i].accountBalance uint256 new_value (uint old_value) STORAGE {
    require  old_value == accountBalanceMirror[a][i]; // Need this inorder to sync on insert of new element  
    accountBalanceMirror[a][i] = new_value;
    numOfOperations[a] = old_value + 1;
}

/// @title "ghost storage does not change after deposit()"
rule ghostStorageComparison() {
    uint256 bankAccount;
    env e;
    require e.msg.value > 0; // balance should change by deposit.
    // deposit msg.value to account `bankAccount` and to the native balance of msg.sender.
    deposit(e, bankAccount);
    storage afterOneDeposit = lastStorage;
    // nativeBalances is mapping(address => uint256). `mapping` is not yet supported as a CVL local variable type, so a variable
    // corresponding to a single entry is used instead.
    deposit(e, bankAccount);
    storage afterTwoDeposits = lastStorage;
    assert(afterTwoDeposits[numOfOperations] == afterOneDeposit[numOfOperations], "ghost storage changes after each deposit");
}


