
library BankAccountRecord{

    // // Axiliary array for indexing into the customer map.
    // address[] private _customerAddresses;

    // uint256 private _totalSupply;

    // // Custormers with zero balance.
    // EmptyAccount[] public cannotWithdraw;
   

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
   
}

