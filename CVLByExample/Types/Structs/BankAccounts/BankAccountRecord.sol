
library BankAccountRecord{

    struct BankAccount {
        uint256 accountNumber;
        uint256 accountBalance; 
    }

    struct Customer {
        address id;
        BankAccount[] accounts;
    }

    // blacklistedAccount
    struct IdAccount {
        address id;
        uint256 account;
    }
   
}

