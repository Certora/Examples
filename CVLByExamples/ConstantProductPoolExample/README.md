# Constant Product Pool
This directory contains two versions of the `ConstantProductPool` contract, as inspired by [Trident](https://medium.com/certora/exploiting-an-invariant-break-how-we-found-a-pool-draining-bug-in-sushiswaps-trident-585bd98a4d4f).

To model a system with two ERC20 tokens, there is an example implementation of an ERC20 token in `contracts/ERC20.sol`, and two "dummy" contracts inheriting from it, `contracts/DummyERC20A.sol` and `contracts/DummyERC20B.sol`. 
These two dummy ERC20s and the Constant Product Pool contract under test are provided to the Certora Prover. 

See `certora/conf/runBroken.conf` and `certora/conf/runFixed.conf` for more information on how the Prover is configured. 

## Incorrect Code

`ConstantProductPool.sol` is a faulty version with the following failing rules:

-    `integrityOfSwap` - there is a switch between the token and the recipient arguments in `swap`:
            (Should be: `transfer(recipient, tokenOut, amountOut);`)

-    `noDecreaseByOther` - there is a switch between the token and the recipient arguments in `burnSingle`.

-    `balanceGreaterThanReserve` - This invariant also catches the bug in which there is a switch between the token and the recipient in `burnSingle`:
            (Should be `transfer(recipient, tokenOut, amountOut);`)

-    `integrityOfTotalSupply` - This invariant catches the original bug in Trident where the amount to receive is computed as a function of the balances and not the reserves.

-    `monotonicityOfMint` - there is a bug in mint where the LP tokens of the first depositor are not computed correctly and the less he transfers the more LP-tokens he receives. 

This version can be checked by running: 
```certoraRun certora/conf/runBroken.conf```

## Correct Code

`ConstantProductPoolFixed.sol` - a version in which the bug in swap is fixed and all the rules pass.
 
This contract can be verified by running: 
```certoraRun certora/conf/runFixed.conf```
