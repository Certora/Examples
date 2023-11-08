# ERC20 Example

Example Certora verification for ERC20 contracts.

## Incorrect Code
For the contract `contracts/broken/ERC20.sol` 
the following rules fail:

1. `balancesBoundedByTotalSupply` - fails for functions `burn`, `deposit`, and `mint`.

2. `totalSupplyIsSumOfBalances` - fails for functions `deposit` and `withdraw`.

The fault of the code for these failures is
`deposit` and `withdraw` update `_balances[msg.sender]` but do not update `_totalSupply` accordingly.

## Incorrect Spec
The faults of the spec are:
- The function `transferFrom(address,address,uint)` is defined in the method block of `ERC20.spec` as
   `envfree` but it refers to `env` so cannot be defined as such.
- The invariant `balancesBoundedByTotalSupply` checks the sum of balances of `alice` and `bob` and therefore assumes
   that the invariant holds in the pre-state only for `alice` and `bob`. The counter example demonstrates a
   deposit by another player that is not restricted in the pre state, to `bob`, which makes the sum of balances of `alice` and `bob` larger than `totalSupply``.
   **Note**
   This invariant is implied by the stronger invariant `totalSupplyIsSumOfBalances` because if `totalSupply`
   is equal to the sum of all balances, then the sum of any two balances is less than `totalSupply`.
- The invariant `totalSupplyIsSumOfBalances` **is** inductive but fails because of the fault of 
   `deposit` and `withdraw` described above.
- `requireHidesOverflow()` passes although there is an overflow in depositAmount because `require_uint256(amount1 + amount2))` assumes there is no overflow.


This version can be checked by running:
```certoraRun certora/conf/runERC20.conf```

[The Prover report of this run](https://prover.certora.com/output/1902/7993f66f45bf4126a5a2e6beda750ca1?anonymousKey=4e0b260893a8b711bda17c6b2ca8ac6232c1107e)

## Correct Code
`contracts/correct/ERC20Fixed.sol` is a version in which the rule above failures were fixed. the corrections in the code are:

Updated _totalSupply in deposit()and in withdraw().

## Correct Spec
The corrections in the spec are:

- Removing the incorrect envfree. 
- Removing the redundant invariant balancesBoundedByTotalSupply.
- The rule catchOverflow() fails because depositAmount uses `unchecked` and therefore is not checking for overflow. The `assert_uint256(amount1 + amount2))` catches the overflow.

It can be checked by running:
```certoraRun certora/conf/runERC20Fixed.conf```

[The Prover report of this run](https://prover.certora.com/output/1902/8bb768a5872f4df7945ae63100a6346d?anonymousKey=e906b35f849559095e1fb704a28db80f40b56bb7)
