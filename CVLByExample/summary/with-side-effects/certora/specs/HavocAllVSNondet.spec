using CalleeA as calleeA;
using CalleeB as calleeB;
using CallerWithSideEffects as caller;

methods {
    // Cannot use summary HAVOC_ALL for internal functions
    function _.x() external  => HAVOC_ALL;
    function _.value() external  => NONDET;
    function setXA(uint256 _x) external envfree;
    function getXB() external returns(uint256) envfree;
    function setValueA(uint256 _value) external envfree;
    function getValueB() external returns(uint256) envfree;
}

// Check that changing calleeA does not affect callee B with HAVOC_ALL summarization.
rule checkHavocAllSummarizationResult() {
    uint256 xOfBBefore = getXB();
    setXA(5);
    uint256 xOfBAfter = getXB();
    assert (xOfBBefore == xOfBAfter, "HAVOC_ALL summarization changes values of unchanged contract.");
}

// Check that changing calleeA does not affect callee B with NONDET summarization.
rule checkNONDETSummarizationResult() {
    uint256 xOfBBefore = getValueB();
    setValueA(5);
    uint256 xOfBAfter = getValueB();
    assert (xOfBBefore == xOfBAfter, "NONDET summarization changes values of unchanged contract.");
}
