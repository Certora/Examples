# Revert On Return Size Example

## Overview
This repository contains a smart contract named `TargetCall` that includes a function called `forward`. This function trigger a `execute` function of a target contract that was set in the constructor. The purpose of this example is to demonstrate revert condition based on the TargetCall,
the compiler adds a check that the called target is a contract (checks the code size) but the prover can pass it regular address which cause the function to revert.

## Executions

1. **Certora Run Command**
    - Command:
        ```bash
        certoraRun TargetCall.conf
        ```

2. **Results Analysis**
    - Execution Link: [Certora Run Output](https://prover.certora.com/output/1512/4fe1e430860341aeb29dd19aa47c5e5e?anonymousKey=b49ee3115e09aad558bfd6f27ee974e2c4233e40)
    - The analysis conducted reveals that the `execute` function resulted in a revert due to the target contract not being contract address: tacRC!!53==0x0.

For a comprehensive guide on Certora Verification Language, please refer to the [Certora Documentation](https://docs.certora.com).