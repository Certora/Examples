using CalleeA as calleeA;
using CalleeB as calleeB;
using CallerWithSideEffects as caller;

methods {
    // Cannot use summary HAVOC_ALL for internal functions
    function calleeA.x() external returns(uint256) => HAVOC_ALL;
    function calleeB.x() external returns(uint256) => NONDET;
    // Using address instead of Callee as parameter type because contracts are not supported as parameter type in the spec.
    function setX(address _callee, uint256 _x) external envfree;
    function setValue(address _callee, uint256 _value) external envfree;
    function getX(address _callee) external returns(uint256) envfree;
    function getValue(address _callee) external returns(uint256) envfree;
}

rule checkHavocAllSummarizationResult() {
    // Using address instead of Callee because contracts are not supported as a type in the spec.

    uint256 xOfBBefore = caller.getX(caller.calleeB);
    caller.setX(caller.calleeA, 5);
    uint256 xOfBAfter = caller.getX(caller.calleeB);
    assert (xOfBBefore == xOfBAfter, "HAVOC_ALL summarizations changes values of unchanged contract.");
}

rule checkNONDETSummarizationResult() {
    uint256 xOfABefore = caller.getX(caller.calleeA);
    caller.setValue(caller.calleeB, 5);
    uint256 xOfAAfter = caller.getValue(caller.calleeA);
    assert (xOfABefore == xOfAAfter, "NONDET summarization summarizations changes values of unchanged contract.");
}
