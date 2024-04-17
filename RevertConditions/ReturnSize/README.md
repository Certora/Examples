# Revert On Return Size Example

## Overview
This repository contains a smart contract named `ReturnSize` that includes a function called `callerFunction`. This function takes a library address and a uint as arguments, relying on the implementation of `calledFunction` within the provided library address to execute certain logic based on the input uint. The purpose of this example is to demonstrate the utilization of the CVL prover argument flag `-superOptimisticReturnsize`. This flag ensures that the correct number of return values is obtained from a NONDET (non-deterministic) unresolved call, thereby preventing a revert scenario in such instances.

**NOTE:** For additional information about the flag, please refer to the [Certora Documentation](https://docs.certora.com/en/latest/docs/prover/cli/options.html#prover-args-optimisticreturnsize-true).

## Usage

1. Add `--prover_args '-superOptimisticReturnsize true'` to the execution command.
2. Add `"prover_args": ['-superOptimisticReturnsize true']` to the configuration file.

## Executions

1. **Certora Run Command**
    - Command:
        ```bash
        certoraRun ReturnSize.conf
        ```

2. **Results Analysis**
    - Execution Link: [Certora Run Output without the flag](https://prover.certora.com/output/1512/05d2f376fbce4684b83384837534f3fb?anonymousKey=392672bc72c8fd06f5fc25ba18cb3b7c0670bbd6)
    - The analysis conducted reveals that the summarized call to the `calledFunction` function resulted in a revert due to the return size: tacReturnsize!!58<0x40.

    - Execution Link: [Certora Run Output with the flag](https://prover.certora.com/output/1512/d5758fe61f18406fa0e5ba1a526f2ad7?anonymousKey=f8606f5110a588d340aabac635fe5e530ec1c248)
    - As expected, the revert cause was eliminated, and the rule was verified as expected.

For a comprehensive guide on Certora Verification Language, please refer to the [Certora Documentation](https://docs.certora.com).