
pragma solidity ^0.8.0;

interface IERC20 {
	function transfer(address to, uint value) external;
	function transferFrom(address from, address to, uint value) external;
}


contract Config {

    IERC20 borrowToken;
    IERC20 collateralToken;

    function getBorrowToken() external view returns (IERC20) {
        return borrowToken;
    }
    function getCollateralToken() external view returns (IERC20){
        return collateralToken;
    }
}