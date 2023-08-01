contract BankAccounts{

    mapping(address => Customer) _customers;

    uint256 private _totalSupply;

    struct BankAccount {
        uint   accountNumber;
        uint256 balance; 
    }

    struct Customer {
        // string name;
        uint id;
        BankAccount account;
    }

    function canWithdraw(Customer calldata c) external pure returns(bool) {
        return c.account.balance > 0;
    }

    function getCustomer(address a) external view returns(Customer memory) {
        return _customers[a];
    }

    function totalSupply() external view returns(uint256){
        return _totalSupply;
    }

    function deposit(uint256 amount) public payable {
        _customers[msg.sender].account.balance += amount;
        _totalSupply += amount;
    }

    function transfer(address to, uint256 amount) public {
        require(_customers[msg.sender].account.balance > amount);
        _customers[msg.sender].account.balance -= amount;
        _customers[to].account.balance += amount;
    }

    function withdraw() public returns (bool success)  {
        uint256 amount = _customers[msg.sender].account.balance;
        _customers[msg.sender].account.balance = 0;
        _burn(msg.sender, amount);
        success = msg.sender.send(amount);
    }

    function balanceOf(address a) external view returns (uint balance) {
        return _customers[a].account.balance;
    }

    function ercBalance() public view returns (uint256) {
        return msg.sender.balance;
    }

    function init_state() public pure {}

    function _burn(address user, uint256 amount) internal {
        // _totalSupply -= amount;
        _customers[user].account.balance -= amount;
    }
	 
}

