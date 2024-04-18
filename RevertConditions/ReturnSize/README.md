# Revert On Return Size Example

## Overview
This repository contains a smart contract named `ReturnSize` that includes a function called `callerFunction`. This function takes a contract address and a uint as arguments, relying on the implementation of `calledFunction` within the provided contract address to execute certain logic based on the input uint. The purpose of this example is to demonstrate revert condition based on the unersolved call return size and for completion shows the utilization of the CVL prover argument flag `-superOptimisticReturnsize`. by adding the flag the Prover takes into account only values where return size is as expected.

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
    - Execution Link: [Certora Run Output without the flag](https://prover.certora.com/output/1512/c163456edf4b4d538043862d48bfbf87?anonymousKey=f8bab8f76b9cd434ef816ab599187f81e23ff71b)
    - The analysis conducted reveals that the summarized call to the `calledFunction` function resulted in a revert due to the return size: tacReturnsize!!58<0x40.

    - Execution Link: [Certora Run Output with the flag](https://prover.certora.com/output/1512/f9b2ff3a37de437e9f134f84e6844ad8?anonymousKey=c9e92c302b880cd04d9b2fca196643adec5e0d56)
    - As expected, the revert cause was eliminated, and the rule was verified as expected.

For a comprehensive guide on Certora Verification Language, please refer to the [Certora Documentation](https://docs.certora.com).