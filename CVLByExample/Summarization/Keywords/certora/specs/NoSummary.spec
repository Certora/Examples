methods {
    function setXA(uint256) external envfree;
    function getXA() external returns(uint256) envfree;
    function setXB(uint256) external envfree;
    function getXB() external returns(uint256) envfree;

    function a() external returns(address) envfree;
}

/**
 * Check that changing x in CalleeA does not affect x of CalleeB.
 */
rule checkNoSummarization() {
    uint256 xOfBBefore = getXB();
    setXA(5);
    uint256 xOfBAfter = getXB();
    assert (xOfBBefore == xOfBAfter, "DISPATCHER(true) summarizations changes values of unchanged contract.");
}


rule havocAll(method f) {
    env e;
    address before = a();
    
    calldataarg args;
    f(e,args);
    assert before == a();
}

strong invariant a_alwasyZero()
    a() == 0;

