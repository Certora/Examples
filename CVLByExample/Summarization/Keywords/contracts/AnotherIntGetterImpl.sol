interface IntGetter {
  function get1() external view returns (uint256);
  function get2() external view returns (uint256);
  function set1(uint256 val) external;
  function set2(uint256 val) external;
}

contract AnotherIntGetterImpl is IntGetterImpl {

}