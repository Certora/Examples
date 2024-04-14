methods {
    function setBorrowing(uint256, bool) external envfree;
    function isBorrowing(uint256) external returns bool envfree;
}


// checks the integrity of set Borrowing function and correct retrieval of the corresponding getter
rule setBorrowing(uint256 reserveIndex, bool borrowing)
{	
	setBorrowing(reserveIndex, borrowing);
	assert isBorrowing(reserveIndex) == borrowing, "unexpected result";
}