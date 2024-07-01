pragma solidity ^0.8.20;

import "./IERC20.sol";

contract TrusterLenderPool {
    event FallbackCalled(address sender, uint value, bytes data);

    IERC20 public damnValuableToken;

    constructor (address tokenAddress) public {
        damnValuableToken = IERC20(tokenAddress);
    }

    function flashLoan(
        uint256 borrowAmount,
        address borrower,
        address target,
        bytes calldata data
    )
        external
    {
        uint256 balanceBefore = damnValuableToken.balanceOf(address(this));
        require(balanceBefore >= borrowAmount, "Not enough tokens in pool");
        
        damnValuableToken.transfer(borrower, borrowAmount);
        (bool success, ) = target.call(data);
        require(success, "External call failed");

        uint256 balanceAfter = damnValuableToken.balanceOf(address(this));
        require(balanceAfter >= balanceBefore, "Flash loan hasn't been paid back");
    }

    fallback() external payable {
        emit FallbackCalled(msg.sender, msg.value, msg.data);
        revert("Invalid call. Use flashloan(uint256,address,address,bytes).");
    }
}
