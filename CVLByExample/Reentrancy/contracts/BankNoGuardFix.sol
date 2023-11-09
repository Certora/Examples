

contract BankNoGuardFix  {
    mapping (address => uint256) private userBalances;

    function withdrawAll() external {
        uint256 balance = getUserBalance(msg.sender);
        require(balance > 0, "Insufficient balance");
        userBalances[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Failed to send Ether");
    }

    function withdraw(uint256 amount) external  {
        uint256 balance = getUserBalance(msg.sender);
        require(balance >= amount, "Insufficient balance");
        userBalances[msg.sender] -= amount;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Failed to send Ether");

    }

    function getBalance() external view returns (uint256){
        return address(this).balance;
    }

    function getUserBalance(address _user) public view returns (uint256) {
        return userBalances[_user];
    }
}