/***
 * # ERC20 Example
 *
 * This is an example specification for a generic ERC20 contract.
 */

methods {
    function balanceOf(address)         external returns(uint) envfree;
    function allowance(address,address) external returns(uint) envfree;
    function totalSupply()              external returns(uint) envfree;
    function transferFrom(address,address,uint) external returns(bool) envfree;
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

rule onlyApproveIncreasesAllowance {
    address holder; address spender;

    mathint allowance_before = allowance(holder, spender);

    method f; env e; calldataarg args; // was: env e; uint256 amount;
    f(e, args);                        // was: approve(e, spender, amount);

    mathint allowance_after = allowance(holder, spender);

    satisfy allowance_after > allowance_before =>
        (f.selector == sig:approve(address,uint).selector),
        "only approve and increaseAllowance can increase allowances";
}

//// ## Part 3: Ghosts and Hooks ///////////////////////////////////////////////

ghost mathint sum_of_balances {
    init_state axiom sum_of_balances == 0;
}

hook Sstore _balances[KEY address a] uint new_value (uint old_value) STORAGE {
    // when balance changes, update ghost
    sum_of_balances = sum_of_balances + new_value - old_value;
}

//// ## Part 4: Invariants /////////////////////////////////////////////////////

/// @dev This rule is unsound!
invariant balancesBoundedByTotalSupply(address alice, address bob)
    balanceOf(alice) + balanceOf(bob) <= to_mathint(totalSupply())
{
    preserved transfer(address recip, uint256 amount) with (env e) {
        require recip        == alice || recip        == bob;
        require e.msg.sender == alice || e.msg.sender == bob;
    }

    preserved transferFrom(address from, address to, uint256 amount) {
        require from == alice || from == bob;
        require to   == alice || to   == bob;
    }
}

/** `totalSupply()` returns the sum of `balanceOf(u)` over all users `u`. */
invariant totalSupplyIsSumOfBalances()
    to_mathint(totalSupply()) == sum_of_balances;

rule sanity {
  env e;
  calldataarg arg;
  method f;
  f(e, arg);
  satisfy true;
}

// New features

// Safe casting examples
// depositAmount() uses `unchecked` therefore is not checking for overflow. With the  `require_uint256(amount1 + amount2))` the
// rule passes although an overflow exists.
rule requireHidesOverflow() {
    env e;
    uint256 amount1;
    uint256 amount2;

    storage initial = lastStorage;
    depositAmount(e, amount1);
    depositAmount(e, amount2);
    storage afterTwoSteps = lastStorage;

    depositAmount(e, require_uint256(amount1 + amount2)) at initial;
    storage afterOneStep = lastStorage;
    assert afterOneStep == afterTwoSteps;
}



