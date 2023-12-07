from BankAccountRecord import Customer
from BankAccountRecord import IdAccount
from BankAccountRecord import BankAccount
from BankAccountRecord import MAX_ACCOUNT
from BankAccountRecord import setIdAccount

_customers: public(HashMap[address, Customer])

_totalSupply: uint256 

# Specific accounts blacklisted by owner 
blackList: public(IdAccount[10])

# Only owner can add to blacklist 
_owner: address 

@external
def __init__():
    self._owner = msg.sender

# Owner can blacklist users, denying them to withdraw or transfer 
@external
def addToBlackList(a: address, i: uint256) -> uint256:  
    assert msg.sender == self._owner, "msg.sender != _owner" 
    newId: IdAccount = setIdAccount(a, i)
    # from documentation doesn't work newId: IdAccount = IdAccount({id:= a, account:= i})
    self.blackList.append(newId)
    return self.blackList.length - 1

@external
def isBlacklisted(user: address, acc: uint256) -> bool:
    for i in range(self.blackList.length):
        if self.blackList[i].id == user and self.blackList[i].account == acc: 
            return True 
    return False

# Add a new customer 
@external
def addCustomer(c: Customer):
    assert self._customers[c.id].accounts.length == 0 and c.accounts.length == 0, "illegal account"
    # make sure c.id is not a customer already 
    assert self._customers[c.id].id == address(0), "The customer c.id already exists"
    self._customers[c.id] = c

@external
@view
def getCustomer(a: address) -> Customer:
    return self._customers[a]

@external
@view
def isCustomer(a: address) -> bool:
    return self._customers[a].id == a

# adds the next available account number for a user, returns the new account number
@external
def addAccount(user: address) -> uint256:
    assert self.isCustomer(user), "Customer user does not exist"
    newAccount = self._customers[user].accounts.length
    self._customers[user].accounts.append( BankAccount(newAccount, 0))

@external
@view
def totalSupply() -> uint256:
    return self._totalSupply

# Deposit amount to account number `account` of msg.sender
@external
@payable
def deposit(account: uint256):
    assert self.isCustomer(msg.sender), "Customer msg.sender does not exist"
    assert account < self._customers[msg.sender].accounts.length, "account does not exist"
    self._customers[msg.sender].accounts[account].accountBalance += msg.value
    self._totalSupply += msg.value


# transfer `amount` from account number `fromAccount` of msg.sender to account `toAccount` of `to`.
@external
def transfer(to: address, amount: uint256, fromAccount: uint256, toAccount: uint256):
    assert not self.isBlacklisted(msg.sender, fromAccount), "fromAccount is blackListed"
    assert fromAccount < self._customers[msg.sender].accounts.length, "fromAccount does not exist"
    assert toAccount < self._customers[to].accounts.length
    assert self._customers[msg.sender].accounts[fromAccount].accountBalance >= amount
    self._customers[msg.sender].accounts[fromAccount].accountBalance -= amount
    self._customers[to].accounts[toAccount].accountBalance += amount

@external
def withdraw(account: uint256) -> bool:
    assert not isBlacklisted(msg.sender, account)
    assert account < self._customers[msg.sender].accounts.length
    amount: uint256 = self.balanceOfAccount(msg.sender, account)
    assert amount > 0
    _burn(msg.sender, amount, account)
    # was payable(msg.sender)
    success: bool = raw_call(msg.sender, "", value=amount)
    assert success[0], "withdraw failed"
    return success[0]

@internal
def _burn(user: address, amount: uint256, account: uint256):
    self._totalSupply -= amount
    self._customers[user].accounts[account].accountBalance -= amount

# Returns sum of all accounts of customer with id a.
@external
@view
def balanceOf(a: address) -> uint256:
    sum: uint256 = 0
    for i in range(self._customers[a].accounts.length):
        sum += self._customers[a].accounts[i].accountBalance
    return sum

# Returns the balance of account `account` of user.
@external
@view
def balanceOfAccount(user: address, account: uint256) -> uint256:
    return self._customers[user].accounts[account].accountBalance

@external
@view
def getNumberOfAccounts(user: address) -> uint256:
    return  self._customers[user].accounts.length
