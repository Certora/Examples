// link, dispatcher, + all
// --------------------
// 0, 0, 0   => violations due to havocs
// 0, 1, 0 => violations due to switching called contract
// 1, 0, 0 => no violations
// 1,1, 0 => does nothing because of the link (equivalent to link only)
// 1,1,1 => equivalent to no link with dispatcher
// ------------------------------------------
using CalleeA as calleeA;
using CalleeB as calleeB;
using CallerWithSideEffects as caller;
methods {
    function setXA(uint256) external envfree;
    function getXA() external returns(uint256) envfree;
    function setXB(uint256) external envfree;
    function getXB() external returns(uint256) envfree;
}

/**
 * Check that changing x in CalleeA does not affect x of CalleeB.
 */
rule checkNoSummarization() {
    uint256 xOfBBefore = getXB();
    caller.setXA(5);
    uint256 xOfBAfter = caller.getXB();
    assert (xOfBBefore == xOfBAfter, "DISPATCHER(true) summarizations changes values of unchanged contract.");
}


