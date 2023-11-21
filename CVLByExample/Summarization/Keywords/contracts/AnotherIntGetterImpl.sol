import './IntGetter.sol';

contract AnotherIntGetterImpl is IntGetter {
  uint256 anothervar1;
  uint256 anothervar2;

  function get1() external view override returns (uint256) {
    return anothervar1;
  }

  function get2() external view override returns (uint256) {
    return anothervar2;
  }

  function set1(uint256 val) override external {
    anothervar1 = val;
  }

  function set2(uint256 val) override external {
    anothervar2 = val;
  }

  function dummyB() public pure returns (uint256) {
        return 222;
  }
}