contract Auction 
{
    event BidEvent(address from);
    function bid() public
    {
        emit BidEvent(msg.sender);
    }
}