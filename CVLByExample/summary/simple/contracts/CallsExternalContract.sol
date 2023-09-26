interface IntGetter {
  function get1() external returns (uint256);
  function get2() external returns (uint256);
}

contract CallsExternalContract {
  IntGetter g1;
  IntGetter g2;
  
  function getFromG1() external returns (uint256) { return g1.get1(); }
  function getFromG2() external returns (uint256) { return g1.get2(); }
}