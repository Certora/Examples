contract Auction 
{
    address public Owner = msg.sender;
    address currentBidder;

    // At the entrance to `bid` the reciever balance is already increased by msg.value,
    // so the receiver gets  msg.value + address(this).balance before.
    // This reverts only if msg.value < address(this).balance
    function bid(address to) public payable
    {
        require (msg.value >= address(this).balance);
        payable(to).transfer(address(this).balance);
        currentBidder = msg.sender; 
    }
}