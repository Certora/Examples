# Simple Dapp Testing

This example is based on [a Cyfrin repo](https://github.com/Cyfrin/fuzz-testing-on-foundry). It features a Solidity contract named `SimpleDapp`, which allows users to deposit and withdraw Ether (ETH). The contract functions as a basic ETH vault, enabling users to securely deposit funds and withdraw them later.

Additionally, there is a fuzz test contract named `SimpleDappTest`, designed to verify the functionality of the deposit and withdrawal methods. It ensures, in particular, that a user cannot withdraw more than their deposited amount.

To run this example, use:
```certoraRun SimpleDappTest.conf```

[View the report for this run.](https://prover.certora.com/output/15800/7faf69fd82034fe8824393078c63ead2?anonymousKey=27031765775db06bc5e3bf4f3fc87be556bb59b1)

*Note: Foundry Fuzz Testing Integration is currently in an early alpha phase.*  


*Note: In this example we use `foundry.toml` to manage dependencies and remappings, in other examples we also use `remappings.txt` for the same purpose.
