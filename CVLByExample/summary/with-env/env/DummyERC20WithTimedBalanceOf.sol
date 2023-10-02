contract DummyERC20WithTimedBalanceOf {
  function balanceOf(address user) public view virtual returns (uint256 r) {
    assert(false); // STUB! Should be summarized
  }

  function callBalanceOf(address user) public view returns (uint256 ){
    return balanceOf(user);
  }
}
