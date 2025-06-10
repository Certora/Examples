error dummy file:14:1: Illegal character: ​
error dummy file:18:1: Illegal character: ​
error dummy file:23:1: Illegal character: ​
// ALWAYS vs. CONSTANT:
methods {
    function _.get1() external => ALWAYS(7);
    function _.get2() external => CONSTANT;
    function getFromG1() external returns (uint256) envfree;
    function getFromG2() external returns (uint256) envfree;
}

// Should be violated
rule constantVsAlways {
    assert getFromG2() == getFromG1(), "getFromG1() != getFromG2()";
}

rule constantCanbeAnyValue {
    satisfy getFromG2() == getFromG1();
}

rule constantDoesNotChange(method f) {
    uint256 g2Before = getFromG2();
    env e;
    calldataarg args;
    f(e, args);
    assert getFromG2() == g2Before;
}