/***
 * # ERC20 Example
 *
 * This is an example specification for a generic ERC20 contract.
 */

methods {
    function balanceOf(address)         external returns(uint) envfree;
    function allowance(address,address) external returns(uint) envfree;
    function totalSupply()              external returns(uint) envfree;
    function add(uint256 x, uint256 y)  external returns(uint256) envfree;          
}

//// ## Part 1: Basic Rules ////////////////////////////////////////////////////

/// Transfer must move `amount` tokens from the caller's account to `recipient`
rule transferSpec {
    address sender; address recip; uint amount;

    env e;
    require e.msg.sender == sender;

    mathint balance_sender_before = balanceOf(sender);
    mathint balance_recip_before = balanceOf(recip);

    transfer(e, recip, amount);

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
    env e; address recip; uint amount;

    require balanceOf(e.msg.sender) < amount;

    transfer@withrevert(e, recip, amount);

    assert lastReverted,
        "transfer(recip,amount) must revert if sender's balance is less than `amount`";
}


/// Transfer shouldn't revert unless
///  the sender doesn't have enough funds,
///  or the message value is nonzero,
///  or the recipient's balance would overflow,
///  or the message sender is 0,
///  or the recipient is 0
///
/// @title Transfer doesn't revert
rule transferDoesntRevert {
    env e; address recipient; uint amount;

    require balanceOf(e.msg.sender) > amount;
    require e.msg.value == 0;
    require balanceOf(recipient) + amount < max_uint;
    require e.msg.sender != 0;
    require recipient != 0;

    transfer@withrevert(e, recipient, amount);
    assert !lastReverted;
}

//// ## Part 2: Parametric Rules ///////////////////////////////////////////////

/// If `approve` changes a holder's allowance, then it was called by the holder
rule onlyHolderCanChangeAllowance {
    address holder; address spender;

    mathint allowance_before = allowance(holder, spender);
    method f; env e; calldataarg args; // was: env e; uint256 amount;
    f(e, args);                        // was: approve(e, spender, amount);

    mathint allowance_after = allowance(holder, spender);

    assert allowance_after > allowance_before => e.msg.sender == holder,
        "approve must only change the sender's allowance";

    assert allowance_after > allowance_before =>
        (f.selector == sig:approve(address,uint).selector || f.selector == sig:increaseAllowance(address,uint).selector),
        "only approve and increaseAllowance can increase allowances";
}

//// ## Part 3: Ghosts and Hooks ///////////////////////////////////////////////

persistent ghost mathint sum_of_balances {
    init_state axiom sum_of_balances == 0;
}

hook Sstore _balances[KEY address a] uint new_value (uint old_value) {
    // when balance changes, update ghost
    sum_of_balances = sum_of_balances + new_value - old_value;
}

// This `sload` makes `sum_of_balances >= balance` hold at the beginning of each rule.
hook Sload uint256 balance _balances[KEY address a]  {
  require sum_of_balances >= balance;
}

//// ## Part 4: Invariants

/** `totalSupply()` returns the sum of `balanceOf(u)` over all users `u`. */
invariant totalSupplyIsSumOfBalances()
    totalSupply() == sum_of_balances;

// satisfy examples
// Generate an example trace for a first deposit operation that succeeds.
rule satisfyFirstDepositSucceeds(){
    env e;
    require totalSupply() == 0;
    deposit(e);
    satisfy totalSupply() == e.msg.value;
}

// Generate an example trace for a withdraw that results totalSupply == 0.
rule satisfyLastWithdrawSucceeds() {
    env e;
    uint256 amount;
    requireInvariant totalSupplyIsSumOfBalances();
    require totalSupply() > 0;
    withdraw(e, amount);
    satisfy totalSupply() == 0;
}

// A witness with several function calls.
rule satisfyWithManyOps(){
    env e; env e1; env e2; env e3;
    address recipient; uint amount;

    requireInvariant totalSupplyIsSumOfBalances();
    // The following two requirement are to avoid overflow exmaples.
    require balanceOf(e.msg.sender) > e.msg.value + 10 * amount;
    require balanceOf(recipient) + amount < max_uint;
    require e.msg.sender != 0;
    require recipient != 0;
    deposit(e1);
    depositTo(e2, recipient, amount);
    transfer(e3, recipient, amount);
    assert totalSupply() > 0;  
}



// A non-vacuous example where transfer() does not revert.
rule satisfyVacuityCorrection {
    env e; address recip; uint amount;

    require balanceOf(e.msg.sender) > 0;

    transfer(e, recip, amount);

    satisfy balanceOf(e.msg.sender) == 0;
}