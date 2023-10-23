
methods {
    // `optional` makes the run skip the call to bar when Partial is the contract used in the `verify` option, because
    // bar() is not defined in Partial.
    function bar(uint256 _x) external returns(uint256) envfree optional;
    function foo(uint256 _x) external returns(uint256) envfree;
}

/**
  Since `bar` is undefined in `Partial`, when the main contract is `Partial` the non-parameterized rules are 
  skipped while the parameterized rule instantiates only the functions present in `Partial` and pass.
*/

// This rule shows the difference between the behaviors when the main contract is `Base` in which `bar` is defined and
// when the main contract is `Partial` in which `bar is undefined.
// When the main contract is `Base` the rule passes. 
// When the main contract is `Partial` this rule is skipped.
rule checkBar() {
  bar@withrevert(5);
  satisfy true;
}

// When the main contract is `Partial` the rule instantiates only the functions present in `Partial` and passes.
rule parametericCheckBar(method f) {
  calldataarg args;
  env e;
	f(e,args);
  satisfy true;
}

// One of the functions is not defined in `Partial`.
// When the main contract is `Base` the rule passes. 
// When the main contract is `Partial` the rule is skipped.
rule useBothFunctions(uint256 x) {
  uint256 fooResult = foo(require_uint256(x + 45)); // This is performed in both contracts because foo is defined.
  uint256 barResult = bar(x);

  assert (fooResult == barResult, "Functions have different results");
}
