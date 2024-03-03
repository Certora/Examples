/**
 * @title Structs Example
 *
 * This is an example reasoning about structs.
 * The spec contains examples for:
 * 1. Referencing a struct and its fields.
 * 2. method block including methods passing structs as arguments and returning structs.
 * 3. method block entry for a default getter.
 * 4. method block entry returning a struct as a tuple.
 * 5. structs in cvl functions - passing and returning.
 * 6. struct as a parameter of preserved function.
 */
 

using Bank as bank;  // bank is the same as currentContract.

methods {
     /// Definition of a user-defined solidity method returning a struct
    function getCustomer(address a) external returns(BankAccountRecord.Customer) envfree;
    /// Definition of a compiler-generated method returning a struct as a tuple 
    function blackList(uint256) external returns (address, uint) envfree;
    /// Definition of a function with struct as an argument 
    function addCustomer(BankAccountRecord.Customer) external envfree;

    function balanceOf(address)        external returns(uint) envfree;
    function balanceOfAccount(address, uint) external returns(uint) envfree;
    function totalSupply()             external returns(uint) envfree;
    function getNumberOfAccounts(address) external returns (uint256) envfree;
    function isCustomer(address) external returns (bool) envfree;
}

/** 
 Comparison of full structs is not supported. Each field should be compared instead.
 Here only the id field is compared because arrays (accounts field) cannot be compared.
 */
function integrityOfCustomerInsertion(BankAccountRecord.Customer c1) returns bool {
    addCustomer(c1);
    BankAccountRecord.Customer c = getCustomer(c1.id);
    return (c.id == c1.id);
}

/**
 Calling a solidity method returning a struct.
 @param a - customer's address
 @param accountId - account number
 */
 function getAccount(address a, uint256 accountInd) returns BankAccountRecord.BankAccount {
    BankAccountRecord.Customer c = bank.getCustomer(a);
    return c.accounts[accountInd];
}

/// returning a struct as a tuple.
function getAccountNumberAndBalance(address a, uint256 accountInd) returns (uint256, uint256) {
    env e;
    BankAccountRecord.Customer c = getCustomer(a);
    BankAccountRecord.BankAccount account = getAccount(e.msg.sender, accountInd);
    return (account.accountNumber, account.accountBalance)  ;
}

/**
 You can define rule parameters of a user defined type.
 */
rule correctCustomerInsertion(BankAccountRecord.Customer c1){
    bool correct = integrityOfCustomerInsertion(c1);
    assert (correct, "Bad customer insertion");
}

/// Example for assigning to a tuple.
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

/// Example for struct parameter and  nested struct member reference
rule witnessForIntegrityOfTransferFromCustomerAccount(BankAccountRecord.Customer c) {
    env e;
    uint256 accountNum;
    address to;
    uint256 toAccount;

    require c.accounts[accountNum].accountBalance > 0;
    transfer(e, to, assert_uint256(c.accounts[accountNum].accountBalance/2), accountNum, toAccount);
    satisfy c.accounts[accountNum].accountBalance < balanceOfAccount(to, toAccount);
}

/// Assignment to a struct. 
/// The term getCustomer(a).id is not supported yet.
rule integrityOfCustomerKeyRule(address a, method f) {
    env e;
    calldataarg args;
    BankAccountRecord.Customer c = getCustomer(a);  
    require c.id == a || c.id == 0;
    f(e,args);
    assert c.id == a || c.id == 0;
}


/// Represent the sum of all accounts of all users
/// sum _customers[a].accounts[i].accountBalance 
ghost mathint sumBalances {
    init_state axiom sumBalances == 0;
}

/// Mirror on a struct _customers[a].accounts[i].accountBalance
ghost mapping(address => mapping(uint256 => uint256)) accountBalanceMirror {
    init_state axiom forall address a. forall uint256 i. accountBalanceMirror[a][i] == 0;
}


/// Number of accounts per user 
ghost mapping(address => uint256) numOfAccounts {
    // assumption: it's infeasible to grow the list to these many elements.
    axiom forall address a. numOfAccounts[a] < max_uint256;
    init_state axiom forall address a. numOfAccounts[a] == 0;
}

/// Store hook to synchronize numOfAccounts with the length of the customers[KEY address a].accounts array.
/// We need to use (offset 32) here, as there is no keyword yet to access the length.
hook Sstore _customers[KEY address user].(offset 32) uint256 newLength STORAGE {
    if (newLength > numOfAccounts[user])
        require accountBalanceMirror[user][require_uint256(newLength-1)] == 0 ;   
    numOfAccounts[user] = newLength;
}

/**
 An internal step check to verify that our ghost works as expected, it should mirror the number of accounts.
 Once the sload is defined, this invariant becomes a tautology  
 */
invariant checkNumOfAccounts(address user) 
    numOfAccounts[user] == bank.getNumberOfAccounts(user);

/// This Sload is required in order to eliminate adding unintializaed account balance to sumBalances.
/// (offset 32) is the location of the size of the mapping. It is used because the field `size` is not yet supported in cvl.  
hook Sload uint256 length _customers[KEY address user].(offset 32) STORAGE {
    require numOfAccounts[user] == length; 
}

/// hook on a complex data structure, a mapping to a struct with a dynamic array
hook Sstore _customers[KEY address a].accounts[INDEX uint256 i].accountBalance uint256 new_value (uint old_value) STORAGE {
    require  old_value == accountBalanceMirror[a][i]; // Need this inorder to sync on insert of new element  
    sumBalances =  sumBalances + new_value - old_value ;
    accountBalanceMirror[a][i] = new_value;
}

/// Sload on a struct field.
hook Sload uint256 value  _customers[KEY address a].accounts[INDEX uint256 i].accountBalance   STORAGE {
    // when balance load, safely assume it is less than the sum of all values
    require to_mathint(value) <= sumBalances;
    require to_mathint(i) <= to_mathint(numOfAccounts[a]-1);
}

/// Non-customers have no account.
invariant emptyAccount(address user) 
     !isCustomer(user) => ( 
        getNumberOfAccounts(user) == 0 &&
         (forall uint256 i. accountBalanceMirror[user][i] == 0 )) ; 

/// struct as a parameter of preserved function.
invariant totalSupplyEqSumBalances()
    to_mathint(totalSupply()) == sumBalances 
    {
        preserved addCustomer(BankAccountRecord.Customer c) 
        {
            requireInvariant emptyAccount(c.id);
        }
    }

/// Comparing nativeBalances of current contract.
invariant solvency()
    totalSupply() <= nativeBalances[currentContract] {
        // safely assume that Bank doesn't call itself
        preserved with (env e){ 
            require e.msg.sender != currentContract;
        }
    }
