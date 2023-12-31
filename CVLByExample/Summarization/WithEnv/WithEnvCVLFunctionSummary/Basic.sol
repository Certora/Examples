contract Basic {
	mapping (address => uint) public balance;

	uint256 public totalSupply;


	function key() internal returns (uint) {
		return msg.value;
	}

	function getBalance(address a) external returns(uint256) {
		return balance[a];
	}
	
	function decr() public returns(uint256) {
		balance[msg.sender]--;
		totalSupply--;
		return 1;
	}
	
	function reduceBalance(uint256 amount) public returns (uint256 amountOut)  {
		uint256 poolBalance = balance[address(this)];
		require (poolBalance != 0);
		amountOut = amount;
		require (amountOut != 0);
		require(amountOut <= balance[msg.sender]);
		balance[msg.sender] -= amountOut;
		balance[address(this)] += amountOut;
    }

	function callReduceBalance(uint256 amount) public returns (uint256 amountOut)  {
		return reduceBalance(amount);
	}

}
