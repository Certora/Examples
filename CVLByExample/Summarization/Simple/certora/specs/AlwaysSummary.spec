// ALWAYS function summary

methods {
  function _.get1() external => ALWAYS(7); // Since IntGetter is an interface and not a contract, `_` is the only way to refer to it.
  function getFromG1() external returns (uint256) envfree;
  function getFromG2() external returns (uint256) envfree;
}

rule checkAlwaysSummary {
  assert (getFromG1() == 7, "Summaried to 7 but not always 7"); // Should be verified
}

rule checkNotSummarized {
  assert (getFromG2() == 7, "Not summarized not always 7"); // Should be violated
}
