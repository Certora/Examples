methods {
    /**
        - Multi-contract must not be used in summary declarations. Summaries always implicitly apply to "any contract".;
        - Multi-contract should only be used in envfree declarations without summaries.;
        - When a valid envfree declaration also includes a summary (a therefore does not use multi-contract),;
          the summary applies to "any contract" while the enfree declaration applies to "currentContract".;
    */
    function _.getSomeUInt() external  => ALWAYS(5) ALL;
    function getSomeUInt() external returns(uint256) envfree optional;
    function callGetSomeUIntInImpl1() external returns(uint256) envfree;
    function callGetSomeUIntInImpl2() external returns(uint256) envfree;
}

rule checkA {
    assert callGetSomeUIntInImpl1() == 5;
}

rule checkB {
    assert callGetSomeUIntInImpl2() == 5;
}
