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
rule transferFromCustomerAccountShouldPass(BankAccountRecord.Customer c) {
    env e;
    uint256 accountNum;
    address to;
    uint256 toAccount;

    require c.accounts[accountNum].balance > 0;
    transfer(e, to, assert_uint256(c.accounts[accountNum].balance/2), accountNum, toAccount);
    satisfy c.accounts[accountNum].balance < balanceOfAccount(to, toAccount);
}

// withdraw from a non-necessarily empty account might not change the state.
rule compareStoragePossibleRevertShouldFail() {
    env e;
    storage init = lastStorage;
    uint256 accountNum;

    withdraw(e, accountNum);
    storage after = lastStorage;
    assert (init != after, "Storage doesn't change with withdraw"); 
}

// withdraw from a non-empty account changes the storage state.
rule compareStorageNoRevertShouldPass() {
    env e;
    storage init = lastStorage;
    uint256 accountNum;
    // require canWithdraw(getCustomer(e.msg.sender), accountNum);
    require balanceOfAccount(e.msg.sender, accountNum) > 0;
    withdraw(e, accountNum);
    storage after = lastStorage;
    assert init != after;  
}

// withdraw from a non-necessarily empty account might not change the state.
rule compareStorageWithRevertShouldFail() {
    env e;
    storage init = lastStorage;
    uint256 accountNum;

    withdraw@withrevert(e, accountNum);
    storage after = lastStorage;
    assert init != after;  
}

// Different storage after each customer addition.
rule compareAfterAddingCustomersShouldPass(BankAccountRecord.Customer c1, BankAccountRecord.Customer c2) {
    addCustomer(c1);
    storage afterC1 = lastStorage;
    addCustomer(c2);
    storage afterC2 = lastStorage;
    assert (afterC1 != afterC2, "Storage after adding one customer differs from storage after adding two.");
}

// Different storage after each customer addition.
rule compareAfterAddingCustomersSatisfy(BankAccountRecord.Customer c1, BankAccountRecord.Customer c2) {
    addCustomer(c1);
    storage afterC1 = lastStorage;
    addCustomer(c2);
    storage afterC2 = lastStorage;
    satisfy (afterC1 != afterC2);
}

// Different storage after each customer addition.
rule compareChangedFieldAfterAddingCustomersShouldPass(BankAccountRecord.Customer c1, BankAccountRecord.Customer c2) {
    storage init = lastStorage;
    addCustomer(c1);
    storage afterC1 = lastStorage;
    addCustomer(c2);
    storage afterC2 = lastStorage;
    assert (afterC1[bank] != afterC2[bank]);
    assert init[other] == lastStorage[other];
    assert init[nativeBalances] == lastStorage[nativeBalances];
}

rule compareBalanceAfterWithdrawShouldFail() {
    uint256 bankAccount;
    env e;
    storage initBalance = lastStorage;
    bool success = withdraw(e, bankAccount);
    storage lastBalance = lastStorage;
    assert (success => initBalance[nativeBalances] == lastBalance[nativeBalances]);
}

rule compareBalanceAfterDepositShouldPass() {
    uint256 bankAccount;
    env e;
    storage initBalance = lastStorage;
    require e.msg.value > 0; // balance should change by withdraw.
    deposit(e, e.msg.value, bankAccount);
    storage lastBalance = lastStorage;
    assert (initBalance[nativeBalances] != lastBalance[nativeBalances], "deposit does not change balances");
}

// withdraw that changes native balances.
// This rule fails without the optimistic_fallback argument to the prover because withdraw uses an unresolved "call"
// for the eth transfer which can result also unchanged blances.
// with optimistic_fallback the rule passes because it forces a balance change.
rule compareBalanceAfterWithdrawShouldPass() {
    uint256 bankAccount;
    env e;
    storage initBalance = lastStorage;
    uint256 balance = nativeBalances[e.msg.sender];
    require balance > 0; // balance should change by withdraw.
    bool success = withdraw(e, bankAccount);
    storage lastBalance = lastStorage;
    assert ((balance > 0 && success) => initBalance[nativeBalances] != lastBalance[nativeBalances]);
}




