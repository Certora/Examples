# Structs used in Bank.

MAX_ACCOUNT: constant(uint256) = 10

struct BankAccount:
    accountNumber: uint256
    accountBalance: uint256 

struct Customer:
    id: address
    accounts: BankAccount[10] 

# blacklistedAccount
struct IdAccount:
    id: address
    account: uint256

def setIdAccount(a: address, acc: accout) -> IdAccount:
    return IdAccount({id: a, account: i})
