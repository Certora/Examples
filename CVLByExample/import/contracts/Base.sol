pragma solidity ^0.5.0;

contract Base {

	uint256 public someUInt;
	
	constructor() public {
		someUInt = 7;
	}
	function minusSevenSomeUInt() public {
		someUInt = someUInt - 7;
	}

}