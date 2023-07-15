# ERC20 Example

Example Certora verification for ERC20 contracts.

## Incorrect Code
For the contract `contracts/broken/ERC20.sol` 
the following rules fail:

`balancesBoundedByTotalSupply` - fails for functions `burn`, `deposit`, and `mint`.
`totalSupplyIsSumOfBalances` - fails for functions `deposit` and `withdraw`.

This version can be checked by running:
```certoraRun certora/conf/ERC20.conf```



