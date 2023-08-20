contract AuctionFixed 
{

    address currentBidder;
    uint256 public currentBid;

    // At the entrance to `bid` the reciever balance is already increased by msg.value,
    // so the receiver gets  msg.value + address(this).balance before.
    // This reverts only if msg.value < address(this).balance
    function bid() public payable
    {
        require(msg.value >= currentBid);
        payable(currentBidder).transfer(currentBid);
        currentBidder = msg.sender; 
        currentBid = msg.value;
    }
}