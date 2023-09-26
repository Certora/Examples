// using CalleeA as calleeA;
// using CalleeB as calleeB;
// using CallerWithSideEffects as caller;
methods {
    function callee.x() external returns(uint256) envfree;
    function callee.value() external returns(uint256) envfree;
    function callee.setX(uint256) external returns(uint256) envfree;
    // Using address instead of Callee as parameter type because contracts are not supported as parameter type in the spec.
    function setX(address _callee, uint256 _x) external envfree;
    function setValue(address _callee, uint256 _value) external envfree;
    function getX(address _callee) external returns(uint256) envfree;
    function getValue(address _callee) external returns(uint256) envfree;
}




