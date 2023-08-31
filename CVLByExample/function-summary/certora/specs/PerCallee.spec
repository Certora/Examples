

methods {
  function _.get1() external => PER_CALLEE_CONSTANT;
  function getFromG1() external returns (uint256) envfree;
  function getFromG2() external returns (uint256) envfree;
}​

rule check {
  assert (getFromG1() == getFromG1(), "ALWAYS summary failed"); // Should be verified
  assert (getFromG2() == getFromG2(), "Different results of calls to same unresolved function"); // Should be verified
  assert (getFromG1() == getFromG2(), "Different results for summarized and non-summarized different functions"); // Should be violated
}
