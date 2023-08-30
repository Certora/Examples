/***
 * # Structs Example
 *
 * This is an example specification for using structs.
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
    function balanceOf(address)        external returns(uint) envfree;
    function balanceOfAccount(address a, uint account) external returns(uint) envfree;
    function totalSupply()             external returns(uint) envfree;
    function getCustomer(address a) external returns(BankAccountRecord.Customer) envfree;
    // Define a tuple of the struct fields as the return type for a function returning a struct. 
    // Regardless of the function being envfree.
    function blackList(uint256) external returns (address, uint) envfree;
    function addCustomer(BankAccountRecord.Customer) external envfree;
    function canWithdraw(BankAccountRecord.Customer c, uint256) external returns(bool) envfree;
    function _.receiveCash() external => DISPATCHER(true);
}

//// Basic rules ////////////////////////////////////////////////////
// Comparision of full structs is not supported. Each field should be compared instead.
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

// transfer from blackList must revert.
// rule canTransferOnlyIfCanWithdrawShouldPass() {
//     env e;
//     address from;
//     address to;
//     address black;
//     uint256 account;
//     uint256 toAccount;
//     uint256 amount;
//     uint256 ind;
//     uint256 newAccount;

//     addToBlacklist(e, black, newAccount); 
//     require amount > 0;
//     from, account = blackList(ind);
//     BankAccountRecord.EmptyAccount fa;

//     // Assigment of structs, e.g. fa = EmptyAccount(e.msg.sender, account) is not supported in order to avoid overriding.
//     // `require` is used instead.
//     require fa.id == e.msg.sender && e.msg.sender == from;
//     require fa.account == account;
//     transfer(e, to, amount, fa.account, toAccount);
//     assert (lastReverted, "transfer from an empty account did not revert");
// }

// Accounts in blacklist have zero balance.
// Example for assigning a struct to a tupple.
rule balanceOfEmptyAccountIsZeroShouldPass() {
    env e;
    address from;
    address a;
    uint256 account;
    uint256 account1;
    uint256 amount;
    uint256 ind = addToBlackList(e, a, account1);
    from, account = blackList(ind);
    assert (balanceOfAccount(from, account) == 0, "Customer in black list has non-zero balance.");
}

// Example for struct parameter and for nested struct member reference
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
rule integrityOfCustomerKeyRule(address a){
    BankAccountRecord.Customer c = getCustomer(a); 
    assert c.id == a;
}

// invariant integrityOfCustomerKey(address a)

//     getCustomer(a).id == a;

// The type BankAccountRecord.Customer is not allowed as the key or output type of a ghost mapping.
// ghost mapping(address => BankAccountRecord.Customer) mirroredCustomers {
//         init_state axiom forall address a. forall uint256 account. mirroredCustomers[a].accounts[account].accountBalance == 0;
// }

ghost mathint sumBalances {
    init_state axiom sumBalances == 0;
    // axiom forall address a. forall address b. forall uint256 i. forall uint256 j. 
    //         ((a == b && i == j) => sumBalances >= to_mathint(mirroredCustomers[a].accounts[i].accountBalance)) &&
    //         ((a != b || i  != j) => sumBalances >= 
    //                 (balanceOfMirrored[a].accounts[i].accountBalance + balanceOfMirrored[b].accounts[j].accountBalance));
    // axiom forall address a. forall address b. forall address c. forall uint256 i. forall uint256 j. forall uint256 k. 
    //     ((a != b || i != j) && (a != c || i != k) && (b != c || j != k)) =>
    //     sumBalances >= (balanceOfMirrored[a].accounts[i].accountBalance + balanceOfMirrored[b].accounts[j].accountBalance + 
    //            balanceOfMirrored[c].accounts[k].accountBalance);
}

// invariant balanceEqualMirrored(address a, uint256 i)
//     bank.customers[a].accounts[i].accountBalance == balanceOfMirrored[a].accounts[i].accountBalance;


hook Sstore _customers[KEY address a].accounts[INDEX uint256 i].accountBalance uint256 new_value (uint old_value) STORAGE {
    // when balance changes, update ghost
    sumBalances = sumBalances + new_value - old_value;
}

invariant totalSupplyEqSumBalances()
    to_mathint(totalSupply()) == sumBalances;
