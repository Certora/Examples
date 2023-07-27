# ERC20 Example

Example Certora verification for ERC20 contracts.

## Incorrect Code
For the contract `contracts/broken/ERC20.sol` 
the following rules fail:

`balancesBoundedByTotalSupply` - fails for functions `burn`, `deposit`, and `mint`.
`totalSupplyIsSumOfBalances` - fails for functions `deposit` and `withdraw`.

These rules fail for the following reasons:
1. `deposit` updates `_balances[msg.sender]` but does not update `_totalSupply` accordingly.
2. `withdraw updates `_balances[msg.sender]` but does not update `_totalSupply` accordingly.

## Incorrect Spec
1. The function `transferFrom(address,address,uint)` is defined in the method block of `ERC20.spec` as
   `envfree` but it refers to `env` so cannot be defined as such.
2. The invariant `balancesBoundedByTotalSupply` checks the balances of `alice` and `bob` and therefore assumes
   that the invariant holds in the pre-state only for `alice` and `bob` so there is a counter example with a 
   different sender. 

This version can be checked by running:
```certoraRun certora/conf/ERC20.conf```

[The Prover report of this run](https://prover.certora.com/output/1902/0f92c84924ff4a67b4b23747595f2d98?anonymousKey=2bb886e487aa83d1fa16eb07ed67404cb92fca9f)

## Correct Spec

`contracts/correct/ERC20Fixed.sol` is a version in which the above failures were fixed.

It can be checked by running:
```certoraRun certora/conf/ERC20Fixed.conf```

[The Prover report of this run](https://vaas-stg.certora.com/output/1902/b8098c82fc064cf8b4d5fd994351c61d/)

