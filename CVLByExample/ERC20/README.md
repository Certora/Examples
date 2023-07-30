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
```certoraRun certora/conf/runERC20.conf```

[The Prover report of this run](https://prover.certora.com/output/1902/d6a8960c7d86450ba5345b073f587ec2?anonymousKey=dab741a3726843b0143b35c3f3d5961b43384759)

## Correct Spec

`contracts/correct/ERC20Fixed.sol` is a version in which the above failures were fixed.

It can be checked by running:
```certoraRun certora/conf/runERC20Fixed.conf```

[The Prover report of this run](https://prover.certora.com/output/1902/c08ded2b830a4696b115b33baece1cb0?anonymousKey=7fbb3ba5b671d89278be7fb60ab85c92cddd4bae)

