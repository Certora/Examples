methods {
  function _.set1() external => NONDET;
  function _.set2() external => HAVOC_ALL;
  function getFromG1() external returns (uint256) envfree;
  function getFromG2() external returns (uint256) envfree;
}​

/***
 check which function changes which variable in intGetterImpl 
 */
rule checkChangeG1(method f) {
  uint256 g1Before = getFromG1();

  env e;
  calldataarg args;
  f(e,args);

  uint256 g1After = getFromG1();
  assert (g1Before == g1After, "get1 changed"); // Should fail only on set2

}

/***
 check which function changes which variable in intGetterImpl 
 */
rule checkChangeG2(method f) {
  uint256 g2Before = getFromG2();

  env e;
  calldataarg args;
  f(e,args);

  uint256 g2After = getFromG2();
  assert (g2Before == g2After, "get2 changed"); // Should fail only on set2

}




