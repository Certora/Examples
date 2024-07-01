import "./BankAccountRecord.sol";


contract Bank {
    mapping(address => BankAccountRecord.Customer) public _customers;

    uint256 private _totalSupply;

    // Specific accounts blacklisted by owner 
    BankAccountRecord.IdAccount[] public blackList;
    // Only owner can add to blacklist 
    address _owner; 

    constructor() {
        _owner = msg.sender;
    }

    // Owner can blacklist users, denying them to withdraw or transfer 
    function addToBlackList(address a, uint256 i) external returns(uint256)  {
        require (msg.sender == _owner); 
        blackList.push(BankAccountRecord.IdAccount(a, i));
        return blackList.length - 1;
    }
    
    function isBlacklisted(address user, uint256 acc) public returns(bool)  {
        for (uint256 i; i < blackList.length; i++) {
            if (blackList[i].id == user && blackList[i].account == acc ) {
                return true; 
            }
        }
        return false;
     }

    // Add a new customer 
    function addCustomer(BankAccountRecord.Customer calldata c) external {
        require(_customers[c.id].accounts.length == 0 && c.accounts.length == 0);
        // make sure c.id is not a customer already 
        require(_customers[c.id].id == address(0));
        _customers[c.id] = c;
    }
    function getCustomer(address a) external view returns(BankAccountRecord.Customer memory) {
        return _customers[a];
    }

    function isCustomer(address a) public view returns(bool) {
        return _customers[a].id == a;
    }

    // adds the next available account number for a user, returns the new account number
    function addAccount(address user) external returns (uint256 newAccount) {
        require (isCustomer(user));
        newAccount = _customers[user].accounts.length;
        _customers[user].accounts.push( BankAccountRecord.BankAccount(newAccount, 0));
    }

    function totalSupply() external view returns(uint256){
        return _totalSupply;
    }

    // Deposit amount to account number `account` of msg.sender
    function deposit(uint256 account) public payable {
        require (isCustomer(msg.sender));
        require(account < _customers[msg.sender].accounts.length);
        _customers[msg.sender].accounts[account].accountBalance += msg.value;
        _totalSupply += msg.value;
    }

    // transfer `amount` from account number `fromAccount` of msg.sender to account `toAccount` of `to`.
    function transfer(address to, uint256 amount, uint256 fromAccount, uint256 toAccount) public {
        require( !isBlacklisted(msg.sender, fromAccount));
        require(fromAccount < _customers[msg.sender].accounts.length);
        require(toAccount < _customers[to].accounts.length);
        require(_customers[msg.sender].accounts[fromAccount].accountBalance >= amount);
        _customers[msg.sender].accounts[fromAccount].accountBalance -= amount;
        _customers[to].accounts[toAccount].accountBalance += amount;
    }

    function withdraw(uint256 account) public returns (bool)  {
        require( !isBlacklisted(msg.sender, account));
        require(account < _customers[msg.sender].accounts.length);
        uint256 amount = balanceOfAccount(msg.sender, account);
        require( amount > 0);
        _burn(msg.sender, amount, account);
        (bool success,) = payable(msg.sender).call{value: amount}("");
        require (success);
        return success;
    }

      function _burn(address user, uint256 amount, uint256 account) internal {
         _totalSupply -= amount;
        _customers[user].accounts[account].accountBalance -= amount;
    }

    // Returns sum of all accounts of customer with id a.
    function balanceOf(address a) external view returns (uint256) {
        uint256 sum = 0;
        for (uint256 i = 0; i < _customers[a].accounts.length; i++)
            sum += _customers[a].accounts[i].accountBalance;
        return sum;
    }

    // Returns the balance of account `account` of user.
    function balanceOfAccount(address user, uint256 account) public view returns (uint256) {
        return _customers[user].accounts[account].accountBalance;
    }

    function getNumberOfAccounts(address user) public view returns (uint256) {
        return  _customers[user].accounts.length;
    }
    
}
