/***
 * # Structs Example
 *
 * This is an example reasoning about structs.
 TODO - explain more what's in the spec:
 * referencing a strcut
 * method block
 * method block for default getter
* strcts in cvl function - passing and returning
* 

 * Passing struct as argument to solidity + cvl = with addCustomer 
 * todo : pass struct to cvl function compareCustomer 
 * Solidity Returning struct: - done

* Returning struct from default getter - canTransferOnlyIfCanWithdrawShouldPass
    blacklist(a) will return tuple - done
 * hook on struct + ghost 
    totalSupply == sum(_customers[Key a].accounts[INDEX i].balance)
 */
 

using Bank as bank;

methods {
     // Definition of a user-defined method returning a struct 
    function getCustomer(address a) external returns(BankAccountRecord.Customer) envfree;
 
    // Definition of a user-defined method returning a struct as a tuple 
    function blackList(uint256) external returns (address, uint) envfree;
    // Definition of a function with struct as an argument 
    function addCustomer(BankAccountRecord.Customer) external envfree;
    
    
    function balanceOf(address)        external returns(uint) envfree;
    function balanceOfAccount(address, uint) external returns(uint) envfree;
    function totalSupply()             external returns(uint) envfree;
    function getNumberOfAccounts(address) external returns (uint256) envfree;
    function isCustomer(address) external returns (bool) envfree;
}

//// Basic rules ////////////////////////////////////////////////////
// Comparison of full structs is not supported. Each field should be compared instead.
// Here only the id field is compared because arrays (accounts field) cannot be compared.
function integrityOfCustomerInsertion(BankAccountRecord.Customer c1) returns bool {
    addCustomer(c1);
    BankAccountRecord.Customer c = getCustomer(c1.id);
    return (c.id == c1.id);
}

function getAccount(address a, uint256 accountInd) returns BankAccountRecord.BankAccount {
    BankAccountRecord.Customer c = getCustomer(a);
    return c.accounts[accountInd];
}

function getAccountNumberAndBalance(address a, uint256 accountInd) returns (uint256, uint256) {
    env e;
    BankAccountRecord.Customer c = getCustomer(a);
    BankAccountRecord.BankAccount account = getAccount(e.msg.sender, accountInd);
    return (account.accountNumber, account.accountBalance)  ;
}

rule withdrawAllEmptiesAccount(uint256 accountInd){
    env e;
    BankAccountRecord.BankAccount account = getAccount(e.msg.sender, accountInd);
    withdraw(e, accountInd);
    assert balanceOfAccount(e.msg.sender, accountInd) == 0;
}

rule correctCustomerInsertion(BankAccountRecord.Customer c1){
    bool correct = integrityOfCustomerInsertion(c1);
    assert (correct, "Bad customer insertion");
}



// Example for assigning a struct to a tuple.
rule updateOfBlacklist() {
    env e;
    address user;
    address user1;
    uint256 account;
    uint256 account1;

    uint256 ind = addToBlackList(e, user, account);
    user1, account1 = blackList(ind);
    assert (user == user1 && account == account1, "Customer in black list is not the one added.");
}

// Example for struct parameter and  nested struct member reference
rule witnessForIntegrityOfTransferFromCustomerAccount(BankAccountRecord.Customer c) {
    env e;
    uint256 accountNum;
    address to;
    uint256 toAccount;

    require c.accounts[accountNum].accountBalance > 0;
    transfer(e, to, assert_uint256(c.accounts[accountNum].accountBalance/2), accountNum, toAccount);
    satisfy c.accounts[accountNum].accountBalance < balanceOfAccount(to, toAccount);
}

// Assignment to struct. 
// getCustomer(a).id is not supported yet.
rule integrityOfCustomerKeyRule(address a, method f) {
    env e;
    calldataarg args;
    BankAccountRecord.Customer c = getCustomer(a);  
    require c.id == a || c.id == 0;
    f(e,args);
    assert c.id == a || c.id == 0;
}


// Represent the sum of all accounts of all users
// sum _customers[a].accounts[i].accountBalance 
ghost mathint sumBalances {
    init_state axiom sumBalances == 0;
}

//mirror on a struct _customers[a].accounts[i].accountBalance
ghost mapping(address => mapping(uint256 => uint256)) accountBalanceMirror {
    init_state axiom forall address a. forall uint256 i. accountBalanceMirror[a][i] == 0;
}

//number of account per user 
ghost mapping(address => uint256) numOfAccount {
    // assumption: it's infeasible to grow the list to these many elements.
    axiom forall address a. numOfAccount[a] < 0xffffffffffffffffffffffffffffffff;
    init_state axiom forall address a. numOfAccount[a] == 0;
}

// Store hook to synchronize numOfAccount with the length of the customers[KEY address a].accounts array. 
// We need to use (offset 32) here, as there is no keyword yet to access the length.
hook Sstore _customers[KEY address user].(offset 32) uint256 newLength STORAGE {
    if (newLength > numOfAccount[user])
        require accountBalanceMirror[user][require_uint256(newLength-1)] == 0 ;   
    numOfAccount[user] = newLength;
}

/**
 @title an internal step check to verify that our ghost works as expected, it should mirror the number of accounts.
 Note: once this rule is proven it is safe to have this as a require on the sload .
 Once the sload is defined, thiss invariant becomes a tautology  
**/
invariant checkNumOfAccount(address user) 
    numOfAccount[user] == getNumberOfAccounts(user);
   
hook Sload uint256 length _customers[KEY address user].(offset 32) STORAGE {
    require numOfAccount[user] == length; 
}


// hook on a complex data structure, a mapping to a struct with a dynamic array
hook Sstore _customers[KEY address a].accounts[INDEX uint256 i].accountBalance uint256 new_value (uint old_value) STORAGE {
    require  old_value == accountBalanceMirror[a][i]; //need this to sync on insert of new element  
    sumBalances =  sumBalances + new_value - old_value ;
    accountBalanceMirror[a][i] = new_value;
}

hook Sload uint256 value  _customers[KEY address a].accounts[INDEX uint256 i].accountBalance   STORAGE {
    // when balance load, safely assume it is less than the sum of all values
    require to_mathint(value) <= sumBalances;
    require to_mathint(i) <= to_mathint(numOfAccount[a]-1);
}


invariant emptyAccount(address user) 
     !isCustomer(user) => getNumberOfAccounts(user) == 0; 

invariant totalSupplyEqSumBalances()
    to_mathint(totalSupply()) == sumBalances 
    {
        /* bug in preserve with code. todo - use preserved on function  and remove redundant require in code
        preserved addCustomer(BankAccountRecord.Customer xxx) 
        {
            requireInvariant emptyAccount(0);
        }
        */
    }

invariant solvency()
    totalSupply() <= nativeBalances[currentContract] {
        // safely assume that Bank doesn't call itself
        preserved with (env e){ 
            require e.msg.sender != currentContract;
        }
    }

