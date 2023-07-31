# ERC20 Example

Example Certora verification for ERC20 contracts.

## Incorrect Code
For the contract `contracts/broken/ERC20.sol` 
the following rules fail:

1. `balancesBoundedByTotalSupply` - fails for functions `burn`, `deposit`, and `mint`.

2. `totalSupplyIsSumOfBalances` - fails for functions `deposit` and `withdraw`.

The fault of the code for these failures is that
`deposit` and `withdraw` update `_balances[msg.sender]` but do not update `_totalSupply` accordingly.

## Incorrect Spec
The faults of the spec for these failures:
1. The function `transferFrom(address,address,uint)` is defined in the method block of `ERC20.spec` as
   `envfree` but it refers to `env` so cannot be defined as such.
2. The invariant `balancesBoundedByTotalSupply` checks the sum of balances of `alice` and `bob` and therefore assumes
   that the invariant holds in the pre-state only for `alice` and `bob`. The counter example demonstrates a
   deposit by another player, that is not restricted in the pre state, to `bob`, what makes the sum of balances of `alice` and `bob` larger than `totalSupply``.
   Note that this
   invariant is implied by the stronger invariant `totalSupplyIsSumOfBalances` because if `totalSupply`
   is equal to the sum of all balances, then the sum of any two balances is less than `totalSupply`.
3. The invariant `totalSupplyIsSumOfBalances` **is** inductive but it fails because of the fault of 
   `deposit` and `withdraw` described above.

This version can be checked by running:
```certoraRun certora/conf/runERC20.conf```

[The Prover report of this run](https://prover.certora.com/output/1902/75fc2841d5c3439db9a49b4598947ee0?anonymousKey=a7a3cfa3287f811997f58cebc03b80674349902e)

## Correct Spec

`contracts/correct/ERC20Fixed.sol` is a version in which the above failures were fixed.

It can be checked by running:
```certoraRun certora/conf/runERC20Fixed.conf```

[The Prover report of this run](https://prover.certora.com/output/1902/c08ded2b830a4696b115b33baece1cb0?anonymousKey=7fbb3ba5b671d89278be7fb60ab85c92cddd4bae)

