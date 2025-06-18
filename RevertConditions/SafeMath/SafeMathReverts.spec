methods {
    function increaseValue(uint256) external envfree;
    function decreaseValue(uint256) external envfree;
    function divideValue(uint256) external envfree;
    function value() external returns (uint256) envfree;
}

rule increaseValueRevertingConditions() {
    uint256 amount;
    uint256 valueBefore = value();
    increaseValue@withrevert(amount);
    assert lastReverted <=> valueBefore + amount > max_uint256;
}

rule decreaseValueRevertingConditions() {
    uint256 amount;
    uint256 valueBefore = value();
    decreaseValue@withrevert(amount);
    assert lastReverted <=> valueBefore - amount < 0;
    // (valueBefore - amount) is a mathint and can be negati}

rule divideValueRevertingConditions() {
    uint256 divideBy;
    uint256 valueBefore = value();
    divideValue@withrevert(divideBy);
    assert lastReverted <=> divideBy == 0;
}