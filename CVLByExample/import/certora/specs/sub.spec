import "base.spec"; // @notice Imports all the elements defined in "base.spec", excluding rules and invariants;

// @notice Using a rule defined in the imported spec while overridding its filters and adding a new filter.
use rule threeParametricRuleInBase filtered { f -> isPlusSevenSomeUInt(f), // @notice Override the filter of f
                                            g -> filterDef(g) // @notice Add a filter to g (using an overridden definition)
                                            // @notice The filter of h is inherited from the base spec
                                          }

use invariant invInBase // @notice Imports the invariant invInBase
{
    preserved minusSevenSomeUInt() { // @notice Overriding the preserved block in base.spec
      plusSevenSomeUInt();
    }

    preserved plusSevenSomeUInt() { // @notice Adding a preserved block
      minusSevenSomeUInt();
	  }

    preserved { // @notice Overriding the generic preserved block in base.spec
    }
}

methods { // @notice The methods in the methods block in base.spec are automatically added to this block
  function plusSevenSomeUInt() external returns (bool) envfree;
}

use rule ruleInBase; // @notice Imports the rule ruleInBase

use rule parametricRuleInBase; // @notice Imports the rule parametricRuleInBase

definition isPlusSevenSomeUInt(method h) returns bool = h.selector == sig:plusSevenSomeUInt().selector;

use rule twoParametricRuleInBase filtered { f -> isPlusSevenSomeUInt(f), // @notice Override the filter of f
                                            g -> filterDef(g) // @notice Add a filter to g (using an overridden definition)
                                          }

// @notice Overriding the definition from Base.spec
override definition filterDef(method f) returns bool = f.isFallback;

override function callF(env eF, calldataarg args, method f) {  // @notice Should make ruleInBase fail
  require eF.msg.value > 0;
  f@withrevert(eF, args);
  assert !lastReverted;
}
