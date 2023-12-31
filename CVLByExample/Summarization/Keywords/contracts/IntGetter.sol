abstract contract IntGetter {
  uint256 public x;
  uint256 public value;

  
  function get1() external view virtual returns (uint256);
  function get2() external view virtual returns (uint256);
  function set1(uint256 val) virtual external;
  function set2(uint256 val) virtual external;

  function setX(uint256 _x) public returns (uint256) {
      x = _x;
      return x;
  }

  function getX() public view returns (uint256) {
      return x;
  }

  function getValue() public view returns (uint256) {
      return value;
  }

  function setValue(uint256 _value) public returns (uint256) {
      value = _value;
      return value;
  }
  
}
