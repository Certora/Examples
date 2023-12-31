contract Interest {
  uint256 numDays;
  uint256 interest;
  mapping(address => uint256) principals;
  // decimals 18
 uint256 constant public e = 2718300000000000000;

  function balance(address account) public view returns (uint256) {
    return continuous_interest(principals[account], interest, numDays);
  }

  function advanceDays(uint256 n) public {
    numDays = numDays + n;
  }

  function continuous_interest(uint256 p, uint256 r, uint256 t)
      internal pure returns (uint256) {
    return p * e ^ (r * t);
  }
}
