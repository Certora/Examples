import "base.spec"; // @notice Imports all the elements defined in "base.spec", excluding rules and invariants;

methods {
    function twiceSomeUInt() external returns (uint256) envfree;
}

// @notice Overriding the definition of `f` from `Base.spec` to `twiceSomeUInt()`
override definition filterDef(method f) returns bool = f.selector == sig:twiceSomeUInt().selector;

// @notice Overriding the preserved block in base.spec
use invariant invInBase
{
    preserved minusSevenSomeUInt() {
        requireInvariant dividedBy7();
        require someUInt() > 14;
    }
} // @notice Imports the invariant invInBase

invariant dividedBy7()
    twiceSomeUInt() % 7 == 0;

methods {
    // @notice The methods in the methods block in `base.spec` are automatically added to this block
    function plusSevenSomeUInt() external returns (bool) envfree;
}

use rule ruleInBase; // @notice Imports the rule `ruleInBase`

use rule parametricRuleInBase; // @notice Imports the rule `parametricRuleInBase`

// Returns true when `h` is the function `plusSevenSoneInt`.

definition isPlusSevenSomeUInt(method h) returns bool = h.selector == sig:plusSevenSomeUInt().selector;

// Using a definition of the importing spec for overriding the filters from the imported spec.
use rule twoParametricRuleInBase // @notice Add a filter to g (using an overridden definition)

filtered { f -> isPlusSevenSomeUInt(f), g -> filterDef(g) } // @notice Override the filter of f

// Adding `@withrevert` to the imported function and restricting `msg.value`.
// This will revert because callF is non payable so the `require` cannot hold.
override function callF(env eF, calldataarg args, method f) {
    // @notice Should make ruleInBase fail
    require eF.msg.value > 0;
    f@withrevert(eF, args);
    assert !lastReverted;
}
