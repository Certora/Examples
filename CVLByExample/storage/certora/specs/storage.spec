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
    function balanceOf(address)        external returns(uint) envfree;
    function balanceOfAccount(address user, uint account) external returns(uint) envfree;
    function totalSupply()             external returns(uint) envfree;
    function getCustomer(address a) external returns(BankAccountRecord.Customer) envfree;
    /// Definition of a compiler-generated method returning a struct as a tuple 
    function blackList(uint256) external returns (address, uint) envfree;
    /// Definition of a function with struct as an argument
    function addCustomer(BankAccountRecord.Customer) external envfree;
    function isCustomer(address a) external returns(bool) envfree;
    function getNumberOfAccounts(address) external returns (uint256) envfree;
    function isCustomer(address) external returns (bool) envfree;
}

// This rule demonstrated comparing the full storage.
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

/// This rule demonstrates comparing full storage after a transaction with possible revert.
/// withdraw from a non-necessarily empty account might not change the state.
/// This rule fails because in case the withdrawn account is empty the `withdraw` function reverts and therefore the
/// storage is not changed.
rule storageDoesNotChangeByWithdrawWhenRevert() {
    env e;
    storage init = lastStorage;
    uint256 accountNum;

    withdraw@withrevert(e, accountNum);
    storage after = lastStorage;
    assert (lastReverted => init == after, "Storage changes after revert.");  
}

/// This rule demonstrates how to check changes in the full storage when changing data structures of the current contract.
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

    // comparing the storage of bank after one and two additions.
    assert (afterC1[bank] != afterC2[bank], "Adding a customer does not affect storage of bank");
    // comparing the storage of the current contract to its storage at the initial state.
    assert (init[currentContract] != lastStorage[currentContract], "Adding a customer does not affect storage of the current contract");
    // comparing the storage of the nativeBalances to nativeBalances at the initial state.
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

/// Demonstrated how to compare nativeBalances in different stages of the execution.
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

/// Demonstrates comparing native balances at two points of the execution.
// deposit msg.value to this.
rule nativeBalanceChangesByDepositShouldPass() {
    uint256 bankAccount;
    env e;
    require e.msg.sender < max_address;
    require e.msg.sender != bank;
    uint256 initBalance = nativeBalances[bank];
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
    satisfy(success => (lastStorage[bank] != initStorage[bank]));
}

// withdraw that changes native balances.
// This rule fails without the optimistic_fallback argument to the prover because withdraw uses an unresolved "call"
// for the eth transfer which can result also unchanged balances.
// with optimistic_fallback the rule passes because it forces a balance change.
// rule nativeBalanceChangesByWithdrawShouldPass {
//     uint256 bankAccount;
//     env e;
//     uint256 initBalance = nativeBalances[bank];
//     require e.msg.sender != currentContract;
//     bool success = withdraw(e, bankAccount);
//     assert(success => (nativeBalances[bank] != initBalance), "Balance of bank does not change by withdraw");
// }

/// This rule demonstrates how to call deposit (can be any transaction) twice from the same state by restoring the storage to
// its inital state before the second call.
/// Two withdraws are called one after the other where both start from the initial state. Therefore, the storage after each of the
/// withdraws is the same.
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
    // nativeBalances is mapping(address => uint256. mapping is not yet supported as CVL local variable type, so a variable
    // corresponds to a single entry is used instead.
    uint256 afterCallBalance = nativeBalances[bank];
    deposit(e, bankAccount) at initStorage;
    assert (nativeBalances[bank] == afterCallBalance, "Different native balances from same initial storage");
    assert(lastStorage[bank] == afterCallStorage[bank], "Different native storage from same initial storage");
    assert(lastStorage[nativeBalances] == afterCallStorage[nativeBalances], 
        "Different storage of native balances after call from same initial storage");
}

/// Represent the sum of all accounts of all users
/// sum _customers[a].accounts[i].accountBalance 
ghost mathint sumBalances {
    init_state axiom sumBalances == 0;
}

/// Mirror on a struct _customers[a].accounts[i].accountBalance
ghost mapping(address => mapping(uint256 => uint256)) accountBalanceMirror {
    init_state axiom forall address a. forall uint256 i. accountBalanceMirror[a][i] == 0;
}

/// Number of accounts per user 
ghost mapping(address => uint256) numOfAccounts {
    // assumption: it's infeasible to grow the list to these many elements.
    axiom forall address a. numOfAccounts[a] < max_uint256;
    init_state axiom forall address a. numOfAccounts[a] == 0;
}

/// Store hook to synchronize numOfAccounts with the length of the customers[KEY address a].accounts array.
/// We need to use (offset 32) here, as there is no keyword yet to access the length.
hook Sstore _customers[KEY address user].(offset 32) uint256 newLength STORAGE {
    if (newLength > numOfAccounts[user])
        require accountBalanceMirror[user][require_uint256(newLength-1)] == 0 ;   
    numOfAccounts[user] = newLength;
}

ghost uint256 numOperations;

/**
 An internal step check to verify that our ghost works as expected, it should mirror the number of accounts.
 Note: once this rule is proven it is safe to have this as a require on the sload .
 Once the sload is defined, this invariant becomes a tautology  
 */
invariant checkNumOfAccounts(address user) 
    numOfAccounts[user] == getNumberOfAccounts(user);

/// This Sload is required in order to eliminate adding unintializaed account balance to sumBlanaces.
hook Sload uint256 length _customers[KEY address user].(offset 32) STORAGE {
    require numOfAccounts[user] == length; 
}

/// hook on a complex data structure, a mapping to a struct with a dynamic array
hook Sstore _customers[KEY address a].accounts[INDEX uint256 i].accountBalance uint256 new_value (uint old_value) STORAGE {
    require  old_value == accountBalanceMirror[a][i]; // Need this inorder to sync on insert of new element  
    sumBalances =  sumBalances + new_value - old_value ;
    accountBalanceMirror[a][i] = new_value;
}

hook Sload uint256 value  _customers[KEY address a].accounts[INDEX uint256 i].accountBalance   STORAGE {
    // when balance load, safely assume it is less than the sum of all values
    require to_mathint(value) <= sumBalances;
    require to_mathint(i) <= to_mathint(numOfAccounts[a]-1);
}

/// Non-customers have no account.
invariant emptyAccount(address user) 
     !isCustomer(user) => ( 
        getNumberOfAccounts(user) == 0 &&
         (forall uint256 i. accountBalanceMirror[user][i] == 0 )) ; 

invariant totalSupplyEqSumBalances()
    to_mathint(totalSupply()) == sumBalances 
    {
        preserved addCustomer(BankAccountRecord.Customer c) 
        {
            requireInvariant emptyAccount(c.id);
        }
    }

/// Comparing nativeBalances of current contract.
invariant solvency()
    totalSupply() <= nativeBalances[currentContract] {
        // safely assume that Bank doesn't call itself
        preserved with (env e){ 
            require e.msg.sender != currentContract;
        }
    }

