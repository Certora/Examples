


// ALWAYS vs. CONSTANT:

methods {
  function _.get1() external => ALWAYS(7);
  function _.get2() external => CONSTANT;
  function getFromG1() external returns (uint256) envfree;
  function getFromG2() external returns (uint256) envfree;
}

​rule checkConstantSummary {
  assert (getFromG2() == getFromG1(), "getFromG1() != getFromG2()"); // Should be violated
}

​rule checkAlwaysSummary {
  assert (getFromG1() == 7, "getFromG1() != 7"); // Should be verified
}

