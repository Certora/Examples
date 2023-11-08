abstract contract ReentrancyGuard {
    bool internal locked;

    modifier noReentrant() {
        require(!locked, "No re-entrancy");
        locked = true;
        _;
        locked = false;
    }
}


contract BankGuardFixed is ReentrancyGuard {
    mapping (address => uint256) private userBalances;

    function withdrawAll() external noReentrant{
        uint256 balance = getUserBalance(msg.sender);
        require(balance > 0, "Insufficient balance");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Failed to send Ether");

        userBalances[msg.sender] = 0;
    }

    function withdraw(uint256 amount) external noReentrant {
        uint256 balance = getUserBalance(msg.sender);
        require(balance >= amount, "Insufficient balance");
        (bool success, ) = msg.sender.call{value: amount}("");
        userBalances[msg.sender] -= amount;
        require(success, "Failed to send Ether");

    }

    function getBalance() external view returns (uint256){
        return address(this).balance;
    }

    function getUserBalance(address _user) public view returns (uint256) {
        return userBalances[_user];
    }
}