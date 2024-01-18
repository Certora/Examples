/***
 * # ERC20 Example
 *
 * This is an example specification for a generic ERC20 contract.
 */

// No overflow in this rule because addAmount() checks for overflow.
rule noOverflow() {
    env e;
    uint256 amount1;
    uint256 amount2;

    // requireInvariant totalSupplyIsSumOfBalances();

    storage initial = lastStorage;
    addAmount(e, amount1);
    addAmount(e,  amount2);
    storage afterTwoSteps = lastStorage;

    addAmount(e, assert_uint256(amount1 + amount2)) at initial;
    storage afterOneStep = lastStorage;
    assert afterOneStep == afterTwoSteps;
    
}

// addAmount() uses `unchecked` therefore is not checking for overflow. The `assert_uint256(amount1 + amount2))`
// catches the overflow.
rule catchOverflow() {
    env e;
    uint256 amount1;
    uint256 amount2;

    storage initial = lastStorage;
    addAmount(e, amount1);
    addAmount(e, amount2);
    storage afterTwoSteps = lastStorage;

    addAmount(e, assert_uint256(amount1 + amount2)) at initial;
    storage afterOneStep = lastStorage;
    assert afterOneStep == afterTwoSteps;
    
}