import './IntGetter.sol';

contract IntGetterImpl is IntGetter {
    uint256 var1;
    uint256 var2;

  function get1() external view override returns (uint256) {
    return var1;
  }

  function get2() external view override returns (uint256) {
    return var2;
  }

  function set1(uint256 val) override external {
    var1 = val;
  }

  function set2(uint256 val) override external {
    var2 = val;
  }

  fallback() external {
    var1 = 5;
  }
}

