
methods {
    // `optional` makes the run skip the call to bar when Partial is the contract used in the `verify` option, because
    // bar() is not defined in Partial.
    function bar(uint256 _x) external returns(uint256) envfree optional;
    function foo(uint256 _x) external returns(uint256) envfree;
}


rule checkBar() {
  bar@withrevert(5);
  satisfy true;
}

rule parametericCheckBar(method f) {
  calldataarg args;
  env e;
	f(e,args);
  satisfy true;
}

rule useBothFunctions(uint256 x) {
  uint256 fooResult = foo(require_uint256(x + 45)); // This is performed in both contracts because foo is defined.
  uint256 barResult = bar(x);

  assert (fooResult == barResult, "Functions have different results");
}
