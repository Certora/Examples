// A fix for VulnerableBank, based on [Ethernaut course](https://dev.to/nvn/ethernaut-hacks-level-10-re-entrancy-42o9) ,  

contract Bank {
    mapping (address => uint256) public userBalances;


    function deposit() external payable {
        userBalances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) external {
        uint256 balance = userBalances[msg.sender];
        require(balance >= amount, "Insufficient balance");
        userBalances[msg.sender] -= amount;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Failed to send Ether");

    }

    
}