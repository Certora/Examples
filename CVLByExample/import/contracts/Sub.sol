import './Base.sol';

contract Sub is Base {
	function plusSevenSomeUInt() public returns(bool) {
		someUInt = someUInt + 7;
		return true;
	}
}