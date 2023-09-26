
// CONSTANT vs. NONDET:

methods {
  function _.get1() external => CONSTANT;
  function _.get2() external => NONDET;
  
  function getFromG1() external returns (uint256) envfree;
  function getFromG2() external returns (uint256) envfree;
}

​rule check {
  // Should be verified - two calls return the same value 
  assert (getFromG1() == getFromG1(), "getFromG1() != getFromG1() with CONSTANT summary");
  
  // Should be violated - two calls may return different values
  assert (getFromG2() == getFromG2(), "getFromG2() != getFromG2() with NONDET summary");
}
