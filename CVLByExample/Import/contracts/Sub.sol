import './Base.sol';

contract Sub is Base {
	function plusSevenSomeUInt() public returns(bool) {
		someUInt = someUInt + 7;
		return true;
	}

	function twiceSomeUInt() public returns(uint256) {
		return 2 * someUInt;
	}
}