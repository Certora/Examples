import "base.spec"; // Imports all the elements defined in "base.spec", excluding rules and invariants;

use rule threeParametricRuleInBase filtered { f -> isPlusSevenSomeUInt(f), // Override the filter of f
                                            g -> filterDef(g) // Add a filter to g (using an overridden definition)
                                            // The filter of h is inherited from the base spec
                                          }

use invariant invInBase // Imports the invariant invInBase
{
    preserved minusSevenSomeUInt() { // Overriding the preserved block in base.spec
      plusSevenSomeUInt();
    }

    preserved plusSevenSomeUInt() { // Adding a preserved block
      minusSevenSomeUInt();
	  }

    preserved { // Overriding the generic preserved block in base.spec
    }
}

methods { // The methods in the methods block in base.spec are automatically added to this block
  function plusSevenSomeUInt() external returns (bool) envfree;
}

use rule ruleInBase; // Imports the rule ruleInBase

use rule parametricRuleInBase; // Imports the rule parametricRuleInBase

definition isPlusSevenSomeUInt(method h) returns bool = h.selector == sig:plusSevenSomeUInt().selector;

use rule twoParametricRuleInBase filtered { f -> isPlusSevenSomeUInt(f), // Override the filter of f
                                            g -> filterDef(g) // Add a filter to g (using an overridden definition)
                                          }

override definition filterDef(method f) returns bool = f.isFallback;

override function callF(env eF, calldataarg args, method f) {  // Should make ruleInBase fail
  require eF.msg.value > 0;
  f@withrevert(eF, args);
  assert !lastReverted;
}
