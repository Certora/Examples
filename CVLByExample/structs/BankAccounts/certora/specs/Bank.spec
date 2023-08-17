/***
 * # Structs Example
 *
 * This is an example specification for using structs.
 */


using BankAccountRecord as baccountrecord;
using OtherContract as other;
using Bank as bank;

methods {
    function balanceOf(address)        external returns(uint) envfree;
    function balanceOfAccount(address a, uint account) external returns(uint) envfree;
    function totalSupply()             external returns(uint) envfree;
    function getCustomer(address a) external returns(BankAccountRecord.Customer) envfree;
    function withZeroBalance() external envfree;
    // Define a tuple of the struct fields as the return type for a function returning a struct. 
    // Regardless of the function being envfree.
    function cannotWithdraw(uint account) external returns (address, uint) envfree;
    function addCustomer(BankAccountRecord.Customer) external envfree;
    function canWithdraw(BankAccountRecord.Customer c, uint256) external returns(bool) envfree;
    function _.receiveCash() external => DISPATCHER(true);
}

//// Basic rules ////////////////////////////////////////////////////

// transfer from cannotWithdraw must revert.
rule canTransferOnlyIfCanWithdrawShouldPass() {
    env e;
    address from;
    address to;
    uint256 account;
    uint256 toAccount;
    uint256 amount;
    uint256 ind;

    withZeroBalance(); // fill cannotWithdraw[].
    require amount > 0;
    from, account = cannotWithdraw(ind);
    BankAccountRecord.EmptyAccount fa;

    // Assigment of structs, e.g. fa = EmptyAccount(e.msg.sender, account) is not supported in order to avoid overriding.
    // `require` is used instead.
    require fa.id == e.msg.sender && e.msg.sender == from;
    require fa.account == account;
    transfer(e, to, amount, fa.account, toAccount);

    assert (lastReverted, "trandfer from an empty account did not revert");
}

// Accounts in cannotWithdraw have zero balance.
rule balanceOfEmptyAccountIsZeroShouldPass() {
    env e;
    address from;
    uint256 account;
    uint256 amount;
    uint256 ind;

    withZeroBalance();
    
    require amount > 0;
    BankAccountRecord.EmptyAccount fa;

    from, account = cannotWithdraw(ind);
        
    require fa.id == e.msg.sender && e.msg.sender == from;
    require fa.account == account;
    assert (balanceOfAccount(from, account) == 0, "Balance is positive but cannot withdraw");
}

// Example for struct parameter and for nested struct member reference
rule witnessForIntegrityOfTransferFromCustomerAccount(BankAccountRecord.Customer c) {
    env e;
    uint256 accountNum;
    address to;
    uint256 toAccount;

    require c.accounts[accountNum].accountBalance > 0;
    transfer(e, to, assert_uint256(c.accounts[accountNum].accountBalance/2), accountNum, toAccount);
    satisfy c.accounts[accountNum].accountBalance < balanceOfAccount(to, toAccount);
}

// withdraw from a non-empty account changes the storage state.
rule storageChangesByWithdrawFromNonEmptyAccountShouldPass() {
    env e;
    storage init = lastStorage;
    uint256 accountNum;
    require balanceOfAccount(e.msg.sender, accountNum) > 0;
    withdraw(e, accountNum);
    storage after = lastStorage;
    assert (init != after, "withdraw from non-empty account does not change storage");
}

// withdraw from a non-necessarily empty account might not change the state.
rule storageChangesByWithdrawWithRevertShouldFail() {
    env e;
    storage init = lastStorage;
    uint256 accountNum;

    withdraw@withrevert(e, accountNum);
    storage after = lastStorage;
    assert init != after;  
}

// Different storage after each customer addition.
// The rule Should pass.
rule addingCustomersChangesStorageShouldPass(BankAccountRecord.Customer c1, BankAccountRecord.Customer c2) {
    addCustomer(c1);
    storage afterC1 = lastStorage;
    addCustomer(c2);
    storage afterC2 = lastStorage;
    assert (afterC1 != afterC2, "Storage after adding one customer differs from storage after adding two.");
}

// Different storage after each customer addition.
rule witnessForStorageChangeAfterEachCustomerAddition(BankAccountRecord.Customer c1, BankAccountRecord.Customer c2) {
    addCustomer(c1);
    storage afterC1 = lastStorage;
    addCustomer(c2);
    storage afterC2 = lastStorage;
    satisfy (afterC1 != afterC2);
}

// Different storage after each customer addition.
rule integrityOfStoragePerCustomerShouldPass(BankAccountRecord.Customer c1, BankAccountRecord.Customer c2) {
    storage init = lastStorage;
    addCustomer(c1);
    storage afterC1 = lastStorage;
    addCustomer(c2);
    storage afterC2 = lastStorage;
    assert (afterC1[bank] != afterC2[bank], "Adding a customer does not affect storage");
    assert (init[other] == lastStorage[other], "Adding a customer affects storage of other customers");
    assert (init[nativeBalances] == lastStorage[nativeBalances], "Change in storage affects native balances");
}

// Withdrawing balanceOfAccount(e.msg.sender, bankAccount) eth.
// No restriction on the balance of account so can be Zero.
// Therefore the rule can fail.
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

rule witnessForUnchangedBalanceAfterWithdraw() {
    uint256 bankAccount;
    env e;
    storage initBalance = lastStorage;
    uint256 balance = balanceOfAccount(e.msg.sender, bankAccount);
    require balance > 0; // balance should change by withdraw.
    bool success = withdraw(e, bankAccount);
    storage lastBalance = lastStorage;
    satisfy (success => initBalance[nativeBalances] == lastBalance[nativeBalances]);
}


rule witnessForChangedBalanceAfterWithdraw() {
    uint256 bankAccount;
    env e;
    storage initBalance = lastStorage;
    uint256 balance = balanceOfAccount(e.msg.sender, bankAccount);
    require balance > 0; // balance should change by withdraw.
    bool success = withdraw(e, bankAccount);
    storage lastBalance = lastStorage;
    satisfy (success => initBalance[nativeBalances] != lastBalance[nativeBalances]);
}

// deposit msg.value to this.
rule nativeBalanceChangesByDepositShouldPass() {
    uint256 bankAccount;
    env e;
    require e.msg.sender < max_address;
    uint256 initBalance = nativeBalances[bank];
    storage initStorage = lastStorage;
    require e.msg.value > 0; // balance should change by deposit.
    // deposit msg.value to account `bankAccount` and to the native balance of msg.sender.
    deposit(e, e.msg.value, bankAccount);
    // storage lastBalance = lastStorage;
    // assert(initStorage[nativeBalances] != lastStorage[nativeBalances], "deposit does not change balances");
    assert(nativeBalances[bank] != initBalance, "Balance of bank does not change by deposit");
}

rule sumOfSenderAndReceiverDoesNotChangeByDepositShouldPass() {
    uint256 bankAccount;
    env e;
    uint256 initBankBalance = nativeBalances[bank];
    uint256 initSenderBalance = nativeBalances[e.msg.sender];
    storage initStorage = lastStorage;
    require e.msg.value > 0; // balance should change by deposit.
    // deposit msg.value to account `bankAccount` and to the native balance of msg.sender.
    deposit(e, e.msg.value, bankAccount);
    // storage lastBalance = lastStorage;
    // assert(initStorage[nativeBalances] != lastStorage[nativeBalances], "deposit does not change balances");
    assert((nativeBalances[bank] + nativeBalances[e.msg.sender]) == (initBankBalance + initSenderBalance),
    "Sum of balances of sender and receiver changes by deposit.");
}

rule witnessSumOfSenderAndReceiverDoesNotChangeByDepositShouldPass() {
    uint256 bankAccount;
    env e;
    uint256 initBankBalance = nativeBalances[bank];
    uint256 initSenderBalance = nativeBalances[e.msg.sender];
    storage initStorage = lastStorage;
    require e.msg.value > 0; // balance should change by deposit.
    // deposit msg.value to account `bankAccount` and to the native balance of msg.sender.
    deposit(e, e.msg.value, bankAccount);
    // storage lastBalance = lastStorage;
    // assert(initStorage[nativeBalances] != lastStorage[nativeBalances], "deposit does not change balances");
    satisfy((nativeBalances[bank] + nativeBalances[e.msg.sender]) == (initBankBalance + initSenderBalance));
}

rule witnessForNativeBalanceChangesByDeposit() {
    uint256 bankAccount;
    env e;
    require e.msg.sender < max_address;
    uint256 initBalance = nativeBalances[bank];
    storage initStorage = lastStorage;
    require e.msg.value > 0; // balance should change by deposit.
    // deposit msg.value to account `bankAccount` and to the native balance of msg.sender.
    deposit(e, e.msg.value, bankAccount);
    // storage lastBalance = lastStorage;
    // assert(initStorage[nativeBalances] != lastStorage[nativeBalances], "deposit does not change balances");
    satisfy(nativeBalances[bank] != initBalance);
}

// Commented out until fixed
// withdraw that changes native balances.
// This rule fails without the optimistic_fallback argument to the prover because withdraw uses an unresolved "call"
// for the eth transfer which can result also unchanged blances.
// with optimistic_fallback the rule passes because it forces a balance change.
rule nativeBalanceChangesByWithdrawShouldPassInFixed() {
    uint256 bankAccount;
    env e;
    uint256 initBalance = nativeBalances[bank];
    storage initStorage = lastStorage;
    uint256 balance = balanceOfAccount(e.msg.sender, bankAccount);
    require balance > 0; // balance should change by withdraw.
    bool success = withdraw(e, bankAccount);
    assert(success => (nativeBalances[bank] != initBalance), "Balance of bank does not change by withdraw");
}

// Commented out until fixed
rule nativeBalanceAfterTwoWithdrawFromInitShouldPass() {
    uint256 bankAccount;
    env e;
    require e.msg.sender < max_address;
    uint256 initBalance = nativeBalances[bank];
    storage initStorage = lastStorage;
    uint256 balance = balanceOfAccount(e.msg.sender, bankAccount);
    // uint256 balance = nativeBalances[e.msg.sender];
    require balance > 0; // balance should change by withdraw.
    bool success1 = withdraw(e, bankAccount);
    uint256 afterWithdraw = nativeBalances[bank];
    bool success2 = withdraw(e, bankAccount) at initStorage;
    assert((success1 && success2) => 
    (nativeBalances[bank] == afterWithdraw), "Different balances from same initial balance");
}

rule unresolvedFunctionCanChangeBalance(method f) {
    env e;
    uint256 nativeBefore = nativeBalances[bank];    
    calldataarg args;
    f(e,args); /* check on all possible arguments */
    assert( nativeBalances[bank] != nativeBefore, "nativeBalances does not change by unresolved")  ;
}

rule witnessUnresolvedFunctionCanChangeBalance(method f) {
    env e;
    uint256 nativeBefore = nativeBalances[bank];    
    calldataarg args;
    f(e,args); /* check on all possible arguments */
    satisfy nativeBalances[bank] != nativeBefore;
}





