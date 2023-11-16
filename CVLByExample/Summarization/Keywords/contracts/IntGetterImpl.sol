interface IntGetter {
  function get1() external view returns (uint256);
  function get2() external view returns (uint256);
  function set1(uint256 val) external;
  function set2(uint256 val) external;
}

contract IntGetterImpl is IntGetter {
    uint256 var1;
    uint256 var2;

  function get1() external view returns (uint256) {
    return var1;
  }

  function get2() external view returns (uint256) {
    return var2;
  }

  function set1(uint256 val) external {
    var1 = val;
  }

  function set2(uint256 val) external {
    var2 = val;
  }

}