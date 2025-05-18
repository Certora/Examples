// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MainContract 
{
    address currentBidder;
    uint256 public currentBid;

    // At the entrance to `bid` address(this).balance is already increased by msg.value,
    // so the receiver gets  `msg.value + address(this).balance` before.
    // This reverts only if msg.value < address(this).balance
    function bid() public payable
    {
        require(msg.value >= address(this).balance);
        payable(currentBidder).transfer(address(this).balance);
        currentBidder = msg.sender; 
        currentBid = msg.value;
    }
}