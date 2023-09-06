contract AuctionFixed 
{

    address currentBidder;
    uint256 public currentBid;

    // At the entrance to `bid` address(this).balance is already increased by `msg.value`,
    // So the balance of currentContract >= currentBid and therefore the transfer succeeds.
    // This reverts only if msg.value < address(this).balance
    function bid() public payable
    {
        require(msg.value >= currentBid);
        payable(currentBidder).transfer(currentBid);
        currentBidder = msg.sender; 
        currentBid = msg.value;
    }
}