using B as B;

methods {
    function callAFunc() external returns (uint256) envfree;
    function _.toBeSummarized() external => ALWAYS(5) ALL;
    function B.toBeSummarized() external returns(uint256) => ALWAYS(7) ALL;
}

rule isFive {
    assert callAFunc() == 5;
}

rule isSeven {
    assert callAFunc() == 7;
}