// ALWAYS function summary
using CallsExternalContract as caller;

methods {
  function _.get1() external => ALWAYS(7); // Since IntGetter is an interface and not a contract, `_` is the only way to refer to it.
  function caller.getFromG1() external returns (uint256);
  function caller.getFromG2() external returns (uint256);
}

rule checkAlwaysSummary {
  env e;
  assert (caller.getFromG1(e) == 7, "Summaried to 7 but not always 7"); // Should be verified
}

rule checkNotSummarized {
  env e;
  assert (caller.getFromG2(e) == 7, "Not summarized not always 7"); // Should be violated
}
