


// ALWAYS vs. CONSTANT:

methods {
  function _.get1() external => ALWAYS(7);
  function _.get2() external => CONSTANT;
  function getFromG1() external returns (uint256) envfree;
  function getFromG2() external returns (uint256) envfree;
}


​rule constantVsAlways {
  assert (getFromG2() == getFromG1(), "getFromG1() != getFromG2()"); // Should be violated
}

​rule constantCanbeAnyValue {
  satisfy getFromG2() == getFromG1(); 
}


​rule constantDoesNotChange(method f) {
  uint256 g2Before = getFromG2();

  env e;
  calldataarg args;
  f(e,args);

  assert getFromG2() == g2Before;
}



