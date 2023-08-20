contract AuctionFixed 
{
    address public Owner = msg.sender;
    address currentBidder;

    // At the entrance to `bid` the reciever balance is already increased by msg.value,
    // so the receiver gets  msg.value + address(this).balance before.
    // This reverts only if msg.value < address(this).balance
    function bid(address to, uint256 origBalance) public payable
    {
        require (msg.value >= origBalance);
        payable(to).transfer(origBalance);
        currentBidder = msg.sender; 
    }
}