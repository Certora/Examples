methods {
	function minusSevenSomeUInt() external envfree;
	function someUInt() external returns (uint256) envfree;
}

/// @notice Invariant in Base to be overridden by importing `Sub` contract.
invariant invInBase() someUInt() >= 7 {
	preserved {
		require (someUInt() < 30); // @notice Explicit preserved block
	}
}

/// @notice A rule to be used in the importing contract Sub as is.
rule ruleInBase() {
	uint256 before = someUInt();
	minusSevenSomeUInt();
	uint256 after = someUInt();
	assert (before >=7) => (before - after == 7);
}

/// Definition for demonstrating definition override in importing contract `Sub`.
definition filterDef(method f) returns bool = f.selector == sig:someUInt().selector;

/// CVL function to be overridden in importing contract `Sub`.
function callF(env eF, calldataarg args, method f) {
	f(eF, args);
}

/// A rule calling one parameteric function filtered to `someInt`.
rule parametricRuleInBase(method f) filtered { f -> filterDef(f)  }
{
	env eF;
	calldataarg args;
	uint256 before = someUInt();
	callF(eF, args, f);
	uint256 after = someUInt();
	assert ((before >=7) => (before - after <= 7), "Unexpected result of one call to a parametric function");
}

/// @notice f is filtered to `someInt` but g can be any function.
rule twoParametricRuleInBase(method f, method g) filtered { f -> filterDef(f)  }
{
	env eF;
	calldataarg args;
	uint256 before = someUInt();
	callF(eF, args, f);
	callF(eF, args, g);
	uint256 after = someUInt();
	assert ((before >=7) => (before - after <= 7), "Unexpected result of two calls to parametric functions");
}


