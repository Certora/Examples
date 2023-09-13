using Callee as callee;
methods {
    function _.x() external => DISPATCHER(true);
    function callee.x() external returns(uint256) envfree;
    function callee.value() external returns(uint256) envfree;
    // Using address instead of Callee as parameter type because contracts are not supported as parameter type in the spec.
    function setX(address _callee, uint256 _x) external envfree;
    function setValue(address _callee, uint256 _value) external envfree;
    function getX(address _callee) external returns(uint256) envfree;
    function getValue(address _callee) external returns(uint256) envfree;
}

rule checkDispatcherSummarizationResult() {
    // Using address instead of Callee because contracts are not supported as a type in the spec.
    address calleeA;
    address calleeB;

    uint256 xOfBBefore = getX(calleeB);
    setX(calleeA, 5);
    uint256 xOfBAfter = getX(calleeB);
    assert (xOfBBefore == xOfBAfter, "DISPATCHER(true) summarizations changes values of unchanged contract.");
    assert (xOfBBefore != xOfBAfter, "DISPATCHER(true) summarizations does not change values of unchanged contract.");
}

// rule checkNONDETSummarizationResult() {
//     address calleeA;
//     address calleeB;
//     uint256 xOfBBefore = getValue(calleeB);
//     setValue(calleeA, 5);
//     uint256 xOfBAfter = getValue(calleeB);
//     assert (xOfBBefore == xOfBAfter, "NONDET summarization summarizations changes values of unchanged contract.");
// }
