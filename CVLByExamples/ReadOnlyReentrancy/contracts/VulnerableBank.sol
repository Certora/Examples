contract VulnerableBank {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be positive");
        balances[msg.sender] += msg.value;
    }

    function eth() external view returns(uint){
        return address(this).balance;
    }

    function withdraw(uint256 amount) external {
        require(amount > 0, "withdrawal amount must be positive");
        require(this.isAllowedToWithdraw(msg.sender, amount), "insufficient balance");
        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require (success, "Withdrawal failed");
        balances[msg.sender] -= amount; 
    }

    function isAllowedToWithdraw(address user, uint256 amount) external view returns (bool) {
        return balances[user] >= amount;
    }
}