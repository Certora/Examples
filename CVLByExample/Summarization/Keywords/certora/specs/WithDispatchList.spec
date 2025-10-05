using IntGetterImpl as intGetter;
using AnotherIntGetterImpl as anotherIntGetter;

methods {
    function _.setX(uint x) external => DISPATCH(optimistic=true)[ IntGetterImpl._ ];
    function setXOnParameter(address ad, uint256 val) external envfree;
}

/**
 * Check that changing x in the contract determined by the dispatch list behaves correctly.
 */
rule checkDispatchListResolution(address a) {
    uint256 xOfOtherBefore = anotherIntGetter.x;
    setXOnParameter(a, 5);
    uint256 xOfOtherAfter = anotherIntGetter.x;
    uint256 xOfChangedAfter = intGetter.x;
    assert (xOfOtherBefore == xOfOtherAfter, "AnotherIntGetter's x should not have been affected by the set.");
    assert (xOfChangedAfter == 5, "IntGetter's x should be set to 5.");
}

