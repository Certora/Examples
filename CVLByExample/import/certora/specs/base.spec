methods {
	function minusSevenSomeUInt() external envfree;
	function someUInt() external returns (uint256) envfree;
}


invariant invInBase() someUInt() >= 7 {
	preserved minusSevenSomeUInt() {} // Explicit preserved block

	preserved { // Generic preserved block
		require true;
	}
}

rule ruleInBase() {
	uint256 before = someUInt();
	minusSevenSomeUInt();
	uint256 after = someUInt();
	assert (before >=7) => (before - after == 7);
}

definition filterDef(method f) returns bool = f.selector == sig:someUInt().selector;

function callF(env eF, calldataarg args, method f) {
	f(eF, args);
}

rule parametricRuleInBase(method f) filtered { f -> filterDef(f)  }
{
	env eF;
	calldataarg args;
	uint256 before = someUInt();
	callF(eF, args, f);
	uint256 after = someUInt();
	assert (before >=7) => (before - after <= 7);
}

rule twoParametricRuleInBase(method f, method g) filtered { f -> filterDef(f)  }
{
	env eF;
	calldataarg args;
	uint256 before = someUInt();
	callF(eF, args, f);
	callF(eF, args, g);
	uint256 after = someUInt();
	assert (before >=7) => (before - after <= 7);
}

rule threeParametricRuleInBase(method f, method g, method h) filtered { f -> filterDef(f), h -> h.isFallback  }
{
	env eF;
	calldataarg args;
	uint256 before = someUInt();
	callF(eF, args, f);
	callF(eF, args, g);
	h(eF, args);
	uint256 after = someUInt();
	assert (before >=7) => (before - after <= 7);
}
