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
```certoraRun runERC20Broken.conf```

[The Prover report of this run](https://prover.certora.com/output/15800/bd5b3b7d90eb4dfa9a1c0449c5f374aa?anonymousKey=eac1c44973b044ea82f96dde4179de341e81bd49)

## Correct Code
`contracts/correct/ERC20Fixed.sol` is a version in which the rule above failures were fixed. the corrections in the code are:

Updated _totalSupply in deposit()and in withdraw().

## Correct Spec
The corrections in the spec are:

- Removing the incorrect envfree. 
- Removing the redundant invariant balancesBoundedByTotalSupply.
- The rule catchOverflow() fails because depositAmount uses `unchecked` and therefore is not checking for overflow. The `assert_uint256(amount1 + amount2))` catches the overflow.

It can be checked by running:
```certoraRun runERC20Fixed.conf```

[The Prover report of this run](https://prover.certora.com/output/15800/c15d9887881c4dd79c1c474cff5a3463?anonymousKey=81e208dee08aa35e805a111bbfdbf7ea693d7ca4)

## Full Spec

This example is a full spec for ERC20.
To run this use:
```certoraRun runERC20Full.conf```

[The Prover report of this run](https://prover.certora.com/output/15800/cbb6dba5639f4a1799f6367da9c5119d?anonymousKey=68ae2f8dc5dbe158ccdb34ea4794244f4fcb14ac)

You can also run a [mutation test](https://docs.certora.com/en/latest/docs/gambit/index.html) on this example using:
```certoraMutate --conf mutation.conf```

[Mutation report for this run](https://mutation-testing.certora.com?id=c95fc217-3300-4323-a379-08b99421ca06&anonymousKey=932faa90-d711-4a6b-b4d6-eb5a58f8455a)


See https://docs.certora.com for a complete guide.