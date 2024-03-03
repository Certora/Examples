/**
  get2 nondet set1 get2 get2 should not change.
  get2 havoc set1 get2. get2 changes.
*/

using IntGetter1 as g1;
using IntGetter2 as g2;

methods {
  function _.get1() external => HAVOC_ALL;
  function getFromG1() external returns (uint256) envfree;
  function getFromG2() external returns (uint256) envfree;
  function IntGetter1.setX(uint256) external envfree;
  function IntGetter2.setX(uint256) external envfree;
}​


// Check that two calls to a function summarized by Nondet from the same state have the same result. Should be verified.
rule checkNondetDoesNotChange {
  uint256 g1Before = getFromG1();
  uint256 g2Before = getFromG2();
  g1.setX(5);
  uint256 g1After = getFromG1();
  uint256 g2After = getFromG2();
  assert (g1Before == g1After, "two calls to NONDET summarized function have different result"); // Should Fail
  assert (g2Before == g2After, "two calls to NONDET summarized function have different result"); // Should Fail

}

rule checkNotSummarizedDoesNotChange {
  uint256 g2Before = getFromG2();
  g1.setX(6);
  uint256 g2After = getFromG2();
  assert (g2Before == g2After, "two calls to NONDET summarized function have different result"); // Should Fail
}


