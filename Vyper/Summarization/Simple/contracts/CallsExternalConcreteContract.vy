interface IntGetter {
  function get1() external view returns (uint256);
  function get2() external view returns (uint256);
  function setX(uint256 _x) external;
}

contract IntGetter1 is IntGetter {
    uint256 x;
    uint256 y;

  function get1() external view returns (uint256) {
    if (y == 0)
        return 0;
    else 
        return x/y;
  }

  function get2() external view returns (uint256) {
    return x + y;
  }

  function setX(uint256 _x) external {
    x = _x;
  }

}

contract IntGetter2  is IntGetter {
    uint256 x;
    uint256 y;

  function get1() external view returns (uint256) {
    if (y < 3)
        return 0;
    else 
        return x * y;
  }

  function get2() external view returns (uint256) {
    return x * y;
  }

  function setX(uint256 _x) external {
    x = _x;
  }

}

contract CallsExternalConcreteContract {
  IntGetter1 g1;
  IntGetter2 g2;
  
  function getFromG1() external returns (uint256) { 
    return g1.get1(); 
  }

  function getFromG2() external returns (uint256) { 
    return g1.get2(); 
  }

  function setFromG1(uint256 _x) external { 
    return g1.setX(_x); 
  }
}