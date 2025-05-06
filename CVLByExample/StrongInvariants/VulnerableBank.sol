// based on [Ethernaut course](https://dev.to/nvn/ethernaut-hacks-level-10-re-entrancy-42o9) ,  
// includes reentrancy vulnerabilities

contract VulnerableBank {
    mapping (address => uint256) public userBalances;


    function deposit() external payable {
        userBalances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) external {
        uint256 balance = userBalances[msg.sender];
        require(balance >= amount, "Insufficient balance");
        (bool success, ) = msg.sender.call{value: amount}("");
        userBalances[msg.sender] -= amount;
        require(success, "Failed to send Ether");

    }

    
}