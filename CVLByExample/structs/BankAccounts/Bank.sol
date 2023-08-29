import "./BankAccountRecord.sol";


contract Bank {
    mapping(address => BankAccountRecord.Customer) public _customers;

    // Axiliary array for indexing into the customer map.
    address[] private _customerAddresses;

    uint256 private _totalSupply;

    mapping (address => uint) m; //remove
	uint x;

	mapping (uint => address[]) foo; //remove

    // Custormers with zero balance.
    BankAccountRecord.EmptyAccount[] public cannotWithdraw;// blacklist
    // owner can add to blaklist 

    address _owner; 

    event Received(address, uint256);
    receive() external payable {
        emit Received(msg.sender, msg.value);
    }

    fallback() external payable {  
    }

    function canWithdraw(BankAccountRecord.Customer memory c, uint256 account) public pure returns(bool) {
        require(account < c.accounts.length);
        return c.accounts[account].accountBalance > 0;
    }

    // Fill the array of empty accounts.
    /* function addToBlacklist(address a, account i) {
        require msg.sender == _owner; 
        cannotWithdraw.push()
        ...
    }
    */
    function withZeroBalance() external  {
        require (cannotWithdraw.length == 0);
        for (uint256 i; i < _customerAddresses.length; i++) {
            for (uint256 j = 0; j < _customers[_customerAddresses[i]].accounts.length; j++)
            if (!canWithdraw(_customers[_customerAddresses[i]], j)){
                cannotWithdraw.push(BankAccountRecord.EmptyAccount(_customerAddresses[i], j));
            }
        }
    }

    function addCustomer(BankAccountRecord.Customer calldata c) external {
        _customers[c.id] = c;
        _customerAddresses.push(c.id);

    }

    function getCustomer(address a) external view returns(BankAccountRecord.Customer memory) {
        return _customers[a];
    }

    function totalSupply() external view returns(uint256){
        return _totalSupply;
    }

    // Deposit amount to account number `account` of msg.sender
    function deposit(uint256 amount, uint256 account) public payable {
        require( address(this) != msg.sender );
        require(account < _customers[msg.sender].accounts.length);
        _customers[msg.sender].accounts[account].accountBalance += amount;
        _totalSupply += amount;
    }

    // transfer `amount` from acount number `fromAccount` of msg.sender to account `toAccount` of `to`.
    function transfer(address to, uint256 amount, uint256 fromAccount, uint256 toAccount) public {
        require(fromAccount < _customers[msg.sender].accounts.length);
        require(toAccount < _customers[to].accounts.length);
        require(_customers[msg.sender].accounts[fromAccount].accountBalance > amount);
        _customers[msg.sender].accounts[fromAccount].accountBalance -= amount;
        _customers[to].accounts[toAccount].accountBalance += amount;
    }

    function withdraw(uint256 account) public returns (bool)  {
        require(account < _customers[msg.sender].accounts.length);
        // uint256 amount = _customers[msg.sender].accounts[account].accountBalance;
        uint256 amount = balanceOfAccount(msg.sender, account);
        require( amount > 0);
        // _customers[msg.sender].accounts[account].accountBalance = 0;
        _burn(msg.sender, amount, account);
        (bool success,) = payable(msg.sender).call{value: amount}("");
        require (success);
        // bool success = payable(msg.sender).send(amount);
        return success;
    }

    // Returns sum of all accounts of customer with id a.
    function balanceOf(address a) external view returns (uint256) {
        uint256 sum = 0;
        for (uint256 i = 0; i < _customers[a].accounts.length; i++)
            sum += _customers[a].accounts[i].accountBalance;
        return sum;
    }

    // Returns the balance of account `account` of customer a.
    function balanceOfAccount(address a, uint256 account) public view returns (uint256) {
        require(account < _customers[a].accounts.length);
        return _customers[a].accounts[account].accountBalance;
    }

    function ercBalance() public view returns (uint256) {
        return msg.sender.balance;
    }

    function init_state() public pure {}

    function _burn(address user, uint256 amount, uint256 account) internal {
        require(account < _customers[user].accounts.length);
        require(amount <= _customers[user].accounts[account].accountBalance);
         _totalSupply -= amount;
        _customers[user].accounts[account].accountBalance -= amount;
    }

}