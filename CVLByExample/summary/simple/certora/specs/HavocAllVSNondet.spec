

methods {
  function _.get1() external => HAVOC_ALL;
  function _.get2() external => NONDET;
  function getFromG1() external returns (uint256) envfree;
  function getFromG2() external returns (uint256) envfree;
}​

// Check that two calls to a function summarized by HAVOC_ALL from the same state have the same result. Should fail.
rule checkHavocAllChanges {
  storage init = lastStorage;
  uint256 firstG1 = getFromG1();
  uint256 secondG1 = getFromG1() at init;
  assert (firstG1 == secondG1, "HAVOC_ALL called from same state have different results"); 
}

// Check that two calls to a function summarized by HAVOC_ALL from different state have the same result. Should fail.
rule checkHavocAllChanges1 {
  storage init = lastStorage;
  uint256 secondG1 = getFromG1() at init;
  assert (getFromG1() == secondG1, "HAVOC_ALL called from different states has different results"); 
}

// Check that two calls to a function summarized by Nondet from the same state have the same result. Should be verified.
rule checkNondetDoesNotChange {
  storage init = lastStorage;
  uint256 firstG2 = getFromG2();
  uint256 secondG2 = getFromG2() at init;
  assert (firstG2 == secondG2, "NONDET called from same state have different results"); // Should be verified
}

// Check that two calls to a function summarized by Nondet from different states have the same result. Should fail.
rule checkNondetDoesNotChange1 {
  storage init = lastStorage;
  uint256 secondG2 = getFromG2() at init;
  assert (getFromG2() == secondG2, "NONDET called from different states has different results"); // Should be verified
}

