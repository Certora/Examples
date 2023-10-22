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
```certoraRun certora/conf/runBroken.conf```

[The report of the run](https://prover.certora.com/output/1902/206cfd2b17554c37b63a0a14351173fb?anonymousKey=abfb3eb8b573c04edce65e7f5e8cce5864d4bdfd)

## Correct Code

`ConstantProductPoolFixed.sol` - a version in which the bug in swap is fixed and all the rules pass.
 
This contract can be verified by running: 
```certoraRun certora/conf/runFixed.conf```

[The report of the run](https://prover.certora.com/output/1902/8e5f8be3cf154f708d36dcf5ec36f464?anonymousKey=cbbb8307d1b0820ea289fe2f84ce5244aed0a35b)
