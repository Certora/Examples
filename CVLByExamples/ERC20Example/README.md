# ERC20Example

Example Certora verification for ERC20 contracts.

This is a work in progress; see [the Certora Tutorial][tutorial] and
[the Certora Documentation][docs] in the mean time.

[tutorial]: https://github.com/Certora/Tutorials
[docs]: https://docs.certora.com/

For the contract `contracts/broken/ERC20.sol` 
The following rules fail:

balancesBoundedByTotalSupply - fails for functions burn, deposit, mint.
totalSupplyIsSumOfBalances - fails for functions deposit and withdraw.

This version can be verified by running

    ```certoraRun certora/conf/ERC20.conf```



