interface IntGetter {
  function get1() external view returns (uint256);
  function get2() external view returns (uint256);
  function set1() external;
}

contract CallsExternalContract {
  IntGetter g1;
  IntGetter g2;
  
  function getFromG1() external view returns (uint256) { 
    return g1.get1(); 
  }

  function getFromG2() external view returns (uint256) { 
    return g1.get2(); 
  }
}