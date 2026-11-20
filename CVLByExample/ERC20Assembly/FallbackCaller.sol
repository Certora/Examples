// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract FallbackCaller {
    function callFallback(address to, uint256 amount, uint256 gas) external payable returns (bool) {
        require(msg.value == amount, "must transfer native amount");
        (bool success, ) = to.call{gas: gas, value: amount}("");
        /// If call wasn't successful, send ETH back to sender
        if(!success) {
            payable(msg.sender).transfer(amount);
        }
        return success;
    }
}
