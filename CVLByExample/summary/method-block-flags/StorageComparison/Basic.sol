contract Basic {
	mapping (address => uint) public balance;
	uint public x;

	uint256 public totalSupply;

	mapping (uint => address[]) foo;

	function key() internal returns (uint) {
		return msg.value;
	}

	function getBalance(address a) external returns(uint256) {
		return balance[a];
	}
	
	function incr() external {
		x++;
		balance[msg.sender]++;
		foo[key()].push(msg.sender);
		totalSupply++;
	}

	function decr() external {
		x--;
		balance[msg.sender]--;
		foo[key()].pop();
		totalSupply--;
	}

	function internalDecr() internal {
		x--;
		balance[msg.sender]--;
		foo[key()].pop();
		totalSupply--;
	}

	// struct Foo {
	// 	uint a;
	// 	uint b;
	// }

	// struct WithNesting {
	// 	Foo c;
	// }

	// Foo atRoot;
	// WithNesting atRoot2;

	// struct TightlyPacked {
	// 	uint8 x;
	// 	uint8 y;
	// }

	// struct EvenTighter {
	// 	TightlyPacked w;
	// 	uint8 z;
	// }

	// EvenTighter t;

	// function incrStructField() external {
	// 	atRoot.a++;
	// }

	// function incrNestedStructField() external {
	// 	atRoot2.c.a++;
	// }

	// function incrTightlyPackedStruct() external {
	// 	t.w.y++;
	// }

	function transfer(address target, uint amount) external {
		require(amount >= balance[msg.sender]);
		balance[msg.sender] -= amount;
		balance[target] += amount;
	}

	function butThenAlsoSend(address payable to) external payable {
		(bool rc, bytes memory data) = to.call{value: msg.value}(abi.encodeWithSignature("receiveCash()"));
		require(rc);
	}

	function receiveCash() external payable {
	}

	function sharesToAmount(uint256 shares) public view virtual returns (uint256) {
     uint256 poolBalance=balance[address(this)];  
     return shares * poolBalance / totalSupply;  
  }

	// Should change to something more realistic
	function withdraw(uint256 amount) public returns (uint256 amountOut)  {
		uint256 poolBalance = balance[address(this)];
		require (poolBalance != 0);
		amountOut = amount;
		require (amountOut != 0);
		require(amountOut + 1 <= balance[msg.sender]);
		internalDecr();
		balance[msg.sender] -= amountOut;
		balance[address(this)] += amountOut;
    }

	// function maybeRevert(uint y) external {
	// 	if(y == 3) {
	// 		revert();
	// 	}
	// 	x += y;
	// }
}
