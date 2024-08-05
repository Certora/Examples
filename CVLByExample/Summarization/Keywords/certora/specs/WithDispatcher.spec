methods {
    function _.x() external => DISPATCHER(true);
    function _.dummyB() external => DISPATCHER(true);
    function setXA(uint256 _x) external envfree;
    function getXB() external returns(uint256) envfree;
    function getDummyB() external returns(uint256) envfree;
}

/**
 * Check that changing x in CalleeA does not affect x of CalleeB.
 */
rule checkDispatcherUnresolvedSummarizationResult() {
    uint256 xOfBBefore = getXB();
    setXA(5);
    uint256 xOfBAfter = getXB();
    assert (xOfBBefore == xOfBAfter, "DISPATCHER(true) summarizations changes values of unchanged contract.");
}

// getDummyB appears only in calleeB so the rule passes also in the configuration where calleeB does not have a link,
// since the dispatcher finds only one function with the signature given in the summarization.
rule checkDispatcherUniqueSummarizationResult() {
    uint256 dummyB = getDummyB();
    
    assert (dummyB == 222, "DISPATCHER(true) summarizations changes values of unchanged contract.");
}

