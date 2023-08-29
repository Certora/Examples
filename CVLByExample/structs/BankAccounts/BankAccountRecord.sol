
library BankAccountRecord{


    struct BankAccount {
        uint256 accountNumber;
        uint256 accountBalance; 
    }
    // blacklistedAccount
    struct EmptyAccount {
        address id;
        uint256 account;
    }

    struct Customer {
        address id;
        BankAccount[] accounts;
    }
   
}

