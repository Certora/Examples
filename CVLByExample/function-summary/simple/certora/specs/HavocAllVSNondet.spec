

methods {
  function _.get1() external => HAVOC_ALL;
  function _.get2() external => NONDET;
  function getFromG1() external returns (uint256) envfree;
  function getFromG2() external returns (uint256) envfree;
}​

rule check {
    storage init = lastStorage;
    uint256 firstG1 = getFromG1();
    uint256 secondG1 = getFromG1() at init;
    uint256 firstG2 = getFromG2();
    uint256 secondG2 = getFromG2() at init;
  assert (firstG1 == secondG1, "HAVOC_ALL has different results"); // Should be verified
  assert (getFromG1() == secondG1, "HAVOC_ALL has different results"); // Should be verified
  assert (firstG2 == secondG2, "NONDET has different"); // Should be verified
  assert (getFromG2() == secondG2, "NONDET has different"); // Should be verified
}
