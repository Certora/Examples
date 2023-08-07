/***
 * # Structs Example
 *
 * This is an example specification for using structs.
 */

methods {
    function balanceOf(address)        external returns(uint) envfree;
    function balanceOfAccount(address a, uint account) external returns(uint) envfree;
    function totalSupply()             external returns(uint) envfree;
    function getCustomer(address a) external returns(BankAccounts.Customer) envfree;
    function withZeroBalance() external envfree;
    function cannotWithdraw(uint account) external returns (address, uint) envfree;
}

//// Basic rules ////////////////////////////////////////////////////

// transfer from cannotWithdraw must revert.
rule canTransferOnlyIfCanWithdraw() {
    env e;
    address from;
    address to;
    withZeroBalance();
    uint256 account;
    uint256 toAccount;
    uint256 amount;
    uint256 ind;

    require amount > 0;
    from, account = cannotWithdraw(ind);
    BankAccounts.EmptyAccount fa;

    // Assigment of structs, e.g. fa = EmptyAccount(e.msg.sender, account) is not supported in order to avoid overriding.
    // require is used instead.
    require fa.id == e.msg.sender && e.msg.sender == from;
    require fa.account == account;
    transfer(e, to, amount, fa.account, toAccount);

    assert (lastReverted, "trandfer from an empty account did not revert");
}

// Accounts in cannotWithdraw have zero balance.
rule balanceIsZero() {
    env e;
    address from;
    uint256 account;
    uint256 amount;
    uint256 ind;

    withZeroBalance();
    
    require amount > 0;
    BankAccounts.EmptyAccount fa;

    from, account = cannotWithdraw(ind);
        
    require fa.id == e.msg.sender && e.msg.sender == from;
    require fa.account == account;
    assert (balanceOfAccount(from, account) == 0, "Balance is positive but cannot withdraw");
}

// Example for struct parameter and for nested struct member reference
rule transferFromCustomerAccount(BankAccounts.Customer c) {
    env e;
    uint256 accountNum;
    address to;
    uint256 toAccount;

    require c.accounts[accountNum].balance > 0;
    transfer(e, to, assert_uint256(c.accounts[accountNum].balance/2), accountNum, toAccount);
    satisfy c.accounts[accountNum].balance < balanceOfAccount(to, toAccount);
}
