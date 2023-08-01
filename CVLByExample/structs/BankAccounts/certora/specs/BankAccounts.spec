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
}

//// ## Part 1: Basic rules ////////////////////////////////////////////////////

rule sanity {
  env e;
  calldataarg arg;
  method f;
  f(e, arg);
  satisfy true;
}

// Transfer must move `amount` tokens from the caller's account to `recipient`
rule transferSpec() {
    address sender; address recip; uint amount; uint senderAccount; uint toAccount;

    env e;
    require e.msg.sender == sender;

    mathint balance_sender_before = balanceOf(sender);
    mathint balance_recip_before = balanceOf(recip);

    transfer(e, recip, amount, senderAccount, toAccount);

    mathint balance_sender_after = balanceOf(sender);
    mathint balance_recip_after = balanceOf(recip);

    require sender != recip;

    assert balance_sender_after == balance_sender_before - amount,
        "transfer must decrease sender's balance by amount";

    assert balance_recip_after == balance_recip_before + amount,
        "transfer must increase recipient's balance by amount";
}


/// Transfer must revert if the sender's balance is too small
rule transferReverts {
    env e; address recip; uint amount; uint fromAccount; uint toAccount;

    require balanceOfAccount(e.msg.sender, fromAccount) < amount;

    transfer@withrevert(e, recip, amount, fromAccount, toAccount);

    assert lastReverted,
        "transfer(recip,amount) must revert if sender's balance is less than `amount`";
}


/// Transfer must not revert unless
///  the sender doesn't have enough funds,
///  or the message value is nonzero,
///  or the recipient's balance would overflow,
///  or the message sender is 0,
///  or the recipient is 0
///
/// @title Transfer doesn't revert
rule transferDoesntRevert(BankAccounts.Customer c) {
    env e; address recipient; uint amount; uint fromAccount; uint toAccount;

    require fromAccount < c.accounts.length;

    // BankAccounts.Customer c2 = getCustomer(recipient);
    // require toAccount < c2.accounts.length;
    require c.accounts[fromAccount].balance > amount;
    require e.msg.value == 0;
    require balanceOfAccount(recipient, toAccount) + amount < max_uint;
    require e.msg.sender != 0;
    require recipient != 0;

    transfer@withrevert(e, recipient, amount, fromAccount, toAccount);
    assert !lastReverted;
}

// ## Part 2: parametric rules ///////////////////////////////////////////////

// ## Part 3: ghosts and hooks ///////////////////////////////////////////////

// ghost mathint sum_of_balances {
//     init_state axiom sum_of_balances == 0;
// }

// hook Sstore _customers[KEY address a][KEY uint account].accounts[account].balance uint new_value (uint old_value) STORAGE {
//     // when balance changes, update ghost
//     sum_of_balances = sum_of_balances + new_value - old_value;
// }

// //// ## Part 4: invariants /////////////////////////////////////////////////////

// /** `totalSupply()` returns the sum of `balanceOf(u)` over all users `u`. */
// invariant totalSupplyIsSumOfBalances()
//     to_mathint(totalSupply()) == sum_of_balances;

