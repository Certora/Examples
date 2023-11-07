contract DummyERC20WithTimedBalanceOf {
  mapping(address => uint256) private _balances;

  function balanceOf(address user) public view returns (uint256 r) {
    require (_balances[user] > 0); 
  }

  function callBalanceOf(address user) public view returns (uint256 ){
    return balanceOf(user);
  }

  /**
     * @dev See {IERC20-transfer}.
     *
     * Requirements:
     *
     * - `recipient` cannot be the zero address.
     * - the caller must have a balance of at least `amount`.
     */
    function transfer(address recipient, uint256 amount)
        public
        returns (bool)
    {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        uint256 senderBalance = _balances[sender];
        require(
            senderBalance >= amount,
            "ERC20: transfer amount exceeds balance"
        ); 
        unchecked {
            _balances[sender] = senderBalance - amount;
        }
        _balances[recipient] += amount;

    }

  
}
