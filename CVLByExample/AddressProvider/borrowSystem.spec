
using CollateralERC20 as collateralToken;
using BorrowERC20 as borrowToken;

methods {
    function userCollateralAmount(address) external returns (uint256) envfree; 
    function collateralToken.balanceOf(address) external returns (uint256) envfree; 
    //ERC20
    function _.transfer(address to, uint value) external => DISPATCHER(true) ;
	function _.transferFrom(address from, address to, uint value) external => DISPATCHER(true);
}

rule totalCollateralOfUser(uint256 borrowAmount, uint256 collateralAmount) {
    env e; 
    uint256 innerAccounting = userCollateralAmount(e.msg.sender);
    uint256 externalBalance = collateralToken.balanceOf(e.msg.sender);

    borrow(e, borrowAmount, collateralAmount);
    
    assert innerAccounting + externalBalance == userCollateralAmount(e.msg.sender) + collateralToken.balanceOf(e.msg.sender);
}