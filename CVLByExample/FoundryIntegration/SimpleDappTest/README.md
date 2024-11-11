# Simple Dapp Testing
In this example we have a Solidity contract, called `SimpleDapp`, allows users to deposit and withdraw Ether (ETH). This contract is essentially a simple ETH vault where users can safely deposit and later withdraw their funds. 

We also have a fuzz test contract called `SimpleDappTest`. It tests the functionality of the deposit and withdraw functions, ensuring that a user cannot withdraw more than they have deposited.

To run this example, use:
```certoraRun SimpleDappTest.conf```
[Report of this run.](https://vaas-stg.certora.com/output/15800/95791d707c564ad786ccbe5b7ce38e38?anonymousKey=e9903bf39567da6b8dd74d6a5091cdcd63bd6e39)

*NOTE: This Foundry Fuzz Testing Integrations is in early alpha stages.*
