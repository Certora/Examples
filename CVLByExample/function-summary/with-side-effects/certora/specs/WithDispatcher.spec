using Callee as callee;
using CallerWithSideEffects as caller;
methods {
    function _.x() external => DISPATCHER(true);
    function callee.x() external returns(uint256) envfree;
    function callee.value() external returns(uint256) envfree;
    function callee.setX(uint256) external returns(uint256) envfree;
    // Using address instead of Callee as parameter type because contracts are not supported as parameter type in the spec.
    function setX(address _callee, uint256 _x) external envfree;
    function setValue(address _callee, uint256 _value) external envfree;
    function getX(address _callee) external returns(uint256) envfree;
    function getValue(address _callee) external returns(uint256) envfree;
}

rule checkDispatcherSummarizationResult() {
    // Using address instead of Callee because contracts are not supported as a type in the spec.
    uint256 xOfBBefore = caller.getX(caller.calleeB);
    caller.setX(caller.calleeA, 5);
    uint256 xOfBAfter = caller.getX(caller.calleeB);
    assert (xOfBBefore == xOfBAfter, "DISPATCHER(true) summarizations changes values of unchanged contract.");
    assert (xOfBBefore != xOfBAfter, "DISPATCHER(true) summarizations does not change values of unchanged contract.");
}


