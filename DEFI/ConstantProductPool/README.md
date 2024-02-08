# Constant Product Pool
This directory contains two versions of the `ConstantProductPool` contract based on [Trident](https://medium.com/certora/exploiting-an-invariant-break-how-we-found-a-pool-draining-bug-in-sushiswaps-trident-585bd98a4d4f).

To model a system with two ERC20 tokens, find an example implementation of an ERC20 token in `contracts/ERC20.sol`, and two "dummy" contracts inheriting from it, `contracts/DummyERC20A.sol` and `contracts/DummyERC20B.sol`. 
These two dummy ERC20s and the Constant Product Pool contract under test are provided to the Certora Prover. 

Refer to `certora/conf/runBroken.conf` and `certora/conf/runFixed.conf` for more information on how the Prover is configured. 

## Incorrect Code

`ConstantProductPool.sol` is a faulty version with the following failing rules:

-    `integrityOfSwap` - There is a switch between the token and the recipient arguments in `swap`:
            (Should be: `transfer(recipient, tokenOut, amountOut);`)

-    `noDecreaseByOther` - There is a switch between the token and the recipient arguments in `burnSingle`.

-    `balanceGreaterThanReserve` - This invariant also catches the bug in which there is a switch between the token and the recipient in `burnSingle`:
            (Should be `transfer(recipient, tokenOut, amountOut);`)

-    `integrityOfTotalSupply` - This invariant catches the original bug in Trident where the amount to be received is computed as a function of the balances and not the reserves.

-    `monotonicityOfMint` - There is a bug in mint where the LP tokens of the first depositor are incorrectly computed.
 The less the transfers, the more LP-tokens received. 

- The invariant `sumFunds` - fails because of the bugs exposed by the above rules.

To check this version, run: 
```certoraRun runBroken.conf```

[The report of the run](https://prover.certora.com/output/15800/2987524d197447f4944e13ed519390f9?anonymousKey=d09bc4f46c5bab5a51296938fbffeb9fcac03252)

## Correct Code

`ConstantProductPoolFixed.sol` - a version in which the bug in swap is fixed and all the rules pass.
 
This contract can be verified by running: 
```certoraRun runFixed.conf```

[The report of the run](https://prover.certora.com/output/15800/b1ed0c02f9d0409fbaed4485f5b23a56?anonymousKey=a48319976eedda3ebf0e7c3eabe1ead2e02c809f)
