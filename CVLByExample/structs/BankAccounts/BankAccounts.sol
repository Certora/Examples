contract BankAccounts{

    mapping(address => Customer) public _customers;

    // Axiliary array for indexing into the customer map.
    address[] private _customerAddresses;

    uint256 private _totalSupply;

    // Custormers with zero balance.
    EmptyAccount[] public cannotWithdraw;

    struct BankAccount {
        uint256   accountNumber;
        uint256 balance; 
    }

    struct EmptyAccount {
        address id;
        uint256 account;
    }

    struct Customer {
        // string name;
        address id;
        BankAccount[] accounts;
    }

    function canWithdraw(Customer memory c, uint256 account) public pure returns(bool) {
        require(account < c.accounts.length);
        return c.accounts[account].balance > 0;
    }

    // Fill the array of empty accounts.
    function withZeroBalance() external  {
        require (cannotWithdraw.length == 0);
        for (uint256 i; i < _customerAddresses.length; i++) {
            for (uint256 j = 0; j < _customers[_customerAddresses[i]].accounts.length; j++)
            if (!canWithdraw(_customers[_customerAddresses[i]], j)){
                cannotWithdraw.push(EmptyAccount(_customerAddresses[i], j));
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

    // Deposit amount to account number `account` of msg.sender
    function deposit(uint256 amount, uint256 account) public payable {
        require(account < _customers[msg.sender].accounts.length);
        _customers[msg.sender].accounts[account].balance += amount;
        _totalSupply += amount;
    }

    // transfer `amount` from acount number `fromAccount` of msg.sender to account `toAccount` of `to`.
    function transfer(address to, uint256 amount, uint256 fromAccount, uint256 toAccount) public {
        require(fromAccount < _customers[msg.sender].accounts.length);
        require(toAccount < _customers[to].accounts.length);
        require(_customers[msg.sender].accounts[fromAccount].balance > amount);
        _customers[msg.sender].accounts[fromAccount].balance -= amount;
        _customers[to].accounts[toAccount].balance += amount;
    }

    function withdraw(uint256 account) public returns (bool success)  {
        require(account < _customers[msg.sender].accounts.length);
        uint256 amount = _customers[msg.sender].accounts[account].balance;
        _customers[msg.sender].accounts[account].balance = 0;
        _burn(msg.sender, amount, account);
        success = payable(msg.sender).send(amount);
        return success;
    }

    // Returns sum of all accounts of customer with id a.
    function balanceOf(address a) external view returns (uint256 balance) {
        uint256 sum = 0;
        for (uint256 i = 0; i < _customers[a].accounts.length; i++)
            sum += _customers[a].accounts[i].balance;
        return sum;
    }

    // Returns the balance of account `account` of customer a.
    function balanceOfAccount(address a, uint256 account) external view returns (uint256 balance) {
        require(account < _customers[a].accounts.length);
        return _customers[a].accounts[account].balance;
    }

    function ercBalance() public view returns (uint256) {
        return msg.sender.balance;
    }

    function init_state() public pure {}

    function _burn(address user, uint256 amount, uint256 account) internal {
        require(account < _customers[user].accounts.length);
         _totalSupply -= amount;
        _customers[user].accounts[account].balance -= amount;
    }
	 
}

