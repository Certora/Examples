/* This spec provides an example for the need for tracking sums in a spec, and the
 * issues in doing so.
 */
methods {
    function totalSupply() external returns (uint256) envfree;
    function balanceOf(address) external returns (uint256) envfree;
}


/** @title Partial transfer integrity rule
 *  The Prover will find a violation for this rule, caused by an overflow in the
 *  recipient's balance. This overflow is an artifact of the over-approximation of
 *  the Prover. In reality `totalSupply` would prevent such an overflow.
 */
rule transferIntegrity(env e, address recipient, uint256 amount) {

    // Pre state
    uint256 recipientBefore = balanceOf(recipient);

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


/** @title The sum of two balances is at most `totalSupply`
 *  This invariant cannot be verified without additional assumptions.
 */
invariant sumOfTwo(address a, address b)
   (a != b) => (balanceOf(a) + balanceOf(b) <= to_mathint(totalSupply()));
