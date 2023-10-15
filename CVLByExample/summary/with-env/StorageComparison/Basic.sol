contract Basic {
	mapping (address => uint) public balance;
	// uint public x;

	uint256 public totalSupply;

	// mapping (uint => address[]) foo;

	function key() internal returns (uint) {
		return msg.value;
	}

	function getBalance(address a) external returns(uint256) {
		return balance[a];
	}
	
	// function incr(uint256 amount) public {
	// 	balance[msg.sender] += amount;
	// 	foo[key()].push(msg.sender);
	// 	totalSupply += amount
	// }

	function decr() public returns(uint256) {
		balance[msg.sender]--;
		// foo[key()].pop();
		totalSupply--;
		return 1;
	}

	// function internalDecr() internal {
	// 	balance[msg.sender]--;
	// 	foo[key()].pop();
	// 	totalSupply--;
	// }
	
	// Should change to something more realistic
	function reduceBalance(uint256 amount) public returns (uint256 amountOut)  {
		uint256 poolBalance = balance[address(this)];
		require (poolBalance != 0);
		amountOut = amount;
		require (amountOut != 0);
		require(amountOut <= balance[msg.sender]);
		// decr(amountOut);
		balance[msg.sender] -= amountOut;
		balance[address(this)] += amountOut;
    }

	function callReduceBalance(uint256 amount) public returns (uint256 amountOut)  {
		return reduceBalance(amount);
	}

}
