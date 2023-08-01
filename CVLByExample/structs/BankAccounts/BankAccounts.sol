contract BankAccounts{

    mapping(address => Customer) public _customers;

    address[] private _customerAddresses;

    uint256 private _totalSupply;

    FullAccount[] cannotWithdraw;

    struct BankAccount {
        uint   accountNumber;
        uint256 balance; 
    }

    struct FullAccount {
        address id;
        uint account;
    }

    struct Customer {
        // string name;
        address id;
        BankAccount[] accounts;
    }

    function canWithdraw(Customer memory c, uint account) public pure returns(bool) {
        require(account < c.accounts.length);
        return c.accounts[account].balance > 0;
    }

    function withZeroBalance() external  {
        for (uint i; i < _customerAddresses.length; i++) {
            for (uint j = 0; j < _customers[_customerAddresses[i]].accounts.length; j++)
            if (!canWithdraw(_customers[_customerAddresses[i]], j)){
                cannotWithdraw.push(FullAccount(_customerAddresses[i], j));
            }
        }
    }

    function addCustomer(Customer calldata c) external {
        _customers[c.id] = c;
        _customerAddresses.push(c.id);

    }

    function getCustomer(address a) external view returns(BankAccounts.Customer memory) {
        return _customers[a];
    }

    function totalSupply() external view returns(uint256){
        return _totalSupply;
    }

    function deposit(uint256 amount, uint account) public payable {
        require(account < _customers[msg.sender].accounts.length);
        _customers[msg.sender].accounts[account].balance += amount;
        _totalSupply += amount;
    }

    function transfer(address to, uint256 amount, uint fromAccount, uint toAccount) public {
        require(fromAccount < _customers[msg.sender].accounts.length);
        require(toAccount < _customers[to].accounts.length);
        require(_customers[msg.sender].accounts[fromAccount].balance > amount);
        _customers[msg.sender].accounts[fromAccount].balance -= amount;
        _customers[to].accounts[toAccount].balance += amount;
    }

    function withdraw(uint account) public returns (bool success)  {
        require(account < _customers[msg.sender].accounts.length);
        uint256 amount = _customers[msg.sender].accounts[account].balance;
        _customers[msg.sender].accounts[account].balance = 0;
        _burn(msg.sender, amount, account);
        // success = msg.sender.send(amount);
    }

    function balanceOf(address a) external view returns (uint balance) {
        uint sum = 0;
        for (uint i = 0; i < _customers[a].accounts.length; i++)
            sum += _customers[a].accounts[i].balance;
        return sum;
    }

    function balanceOfAccount(address a, uint account) external view returns (uint balance) {
        require(account < _customers[a].accounts.length);
        return _customers[a].accounts[account].balance;
    }

    function ercBalance() public view returns (uint256) {
        return msg.sender.balance;
    }

    function init_state() public pure {}

    function _burn(address user, uint256 amount, uint account) internal {
        require(account < _customers[user].accounts.length);
         _totalSupply -= amount;
        _customers[user].accounts[account].balance -= amount;
    }
	 
}

