
// Contract to be imported
contract Base {

	uint256 public someUInt;
	
	constructor() public {
		someUInt = 7;
	}
	function minusSevenSomeUInt() public {
		someUInt = someUInt - 7;
	}

}