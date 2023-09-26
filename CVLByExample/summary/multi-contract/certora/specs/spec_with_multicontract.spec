using B as b;
methods {
    function b.foo(uint256) external returns(uint256) envfree; // foo of B
    function foo(uint) external returns(uint256) envfree; // foo of the currentContract A
}

rule checkMultiContractWithEnvFree() {
    uint256 x = b.foo(7);
    assert x == 7;
}

rule checkEnvFree() {
    uint256 x = foo(7);
    assert x == 7;
}