/* This spec provides an example for tracking sums.
 */
methods {
    function totalSupply() external returns (uint256) envfree;
    function balanceOf(address) external returns (uint256) envfree;
}


/// @title A ghost variable to track the sum of all balances
ghost mathint sumOfBalances {
    init_state axiom sumOfBalances == 0;
}

/// @title A hook to update `sumOfBalances`
hook Sstore _balances[KEY address addr] uint256 newValue (uint256 oldValue) {
    sumOfBalances = sumOfBalances - oldValue + newValue;
}

/// @title Require that `sumOfBalances` is greater than any balance
hook Sload uint256 balance _balances[KEY address addr] {
    require sumOfBalances >= to_mathint(balance);
}

/// @title The sum of balances is `totalSupply`
invariant totalSupplyIsSumOfBalances()
    to_mathint(totalSupply()) == sumOfBalances;


/// @title Partial transfer integrity rule
rule transferIntegrity(env e, address recipient, uint256 amount) {
    requireInvariant totalSupplyIsSumOfBalances();

    // Pre state
    uint256 recipientBefore = balanceOf(recipient);
    uint256 senderBefore = balanceOf(e.msg.sender);

    // Run transaction
    transfer(e, recipient, amount);

    // Post state
    uint256 recipientAfter = balanceOf(recipient);

    // Verify recipient balance updated correctly
    assert (
        e.msg.sender != recipient =>
        to_mathint(recipientAfter) == recipientBefore + amount
    );
}
