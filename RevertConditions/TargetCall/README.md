# Revert On Return Size Example

## Overview
This repository hosts a smart contract named `TargetCall`, featuring a function called `forward`. This function initiates the `execute` function of a specified target contract, set during the constructor invocation. The purpose of this example is to illustrate a revert condition based on the `TargetCall`. The compiler includes a check ensuring that the called target is a contract (verifies the code size). However, the prover can bypass this check by passing a regular address, resulting in a revert of the function.

## Executions

1. **Certora Run Command**
    - Command:
        ```bash
        certoraRun TargetCall.conf
        ```

2. **Results Analysis**
    - Analysis Link: [Certora Run Output](https://prover.certora.com/output/1512/4fe1e430860341aeb29dd19aa47c5e5e?anonymousKey=b49ee3115e09aad558bfd6f27ee974e2c4233e40)
    - The analysis indicates that the `execute` function resulted in a revert due to the target contract not being a contract address: `tacRC!!53==0x0`.

3. **Certora Run Command**
    - Command:
        ```bash
        certoraRun TargetCallLinking.conf
        ```

4. **Results Analysis**
    - Analysis Link: [Certora Run Output solved with linking](https://prover.certora.com/output/1512/4f7a2d93e65b478db352300ad1cfdeb9?anonymousKey=68143f3c3b01a2c07143602ba5da7ff4fd28fce4)
    - The analysis indicates that the `execute` function wasn't reverted this time due to the use of linking to the actual contract implementation, ensuring that the target address is indeed a contract.

For an in-depth guide on Certora Verification Language, please consult the [Certora Documentation](https://docs.certora.com).