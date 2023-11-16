interface IntGetter {
  function get1() external view returns (uint256);
  function get2() external view returns (uint256);
  function set1() external;
  function set2() external;
}

contract CallsExternalContract {
  IntGetter g;
  
  function getFromG1() external view returns (uint256) { 
    return g.get1(); 
  }

  function getFromG2() external view returns (uint256) { 
    return g.get2(); 
  }

  function setToG1() external { 
    return g.set1(); 
  }

  function setToG2() external { 
    return g.set2(); 
  }

}