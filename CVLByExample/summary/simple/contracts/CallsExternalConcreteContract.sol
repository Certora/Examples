contract IntGetter {
    uint256 x;
    uint256 y;

  function get1() external returns (uint256) {
    if (y == 0)
        return 0;
    else 
        return x/y;
  }

  function get2() external returns (uint256) {
    return x + y;
  }

}

contract CallsExternalContract {
  IntGetter g1;
  IntGetter g2;
  
  function getFromG1() external returns (uint256) { return g1.get1(); }
  function getFromG2() external returns (uint256) { return g1.get2(); }
}