# Contract Alias Example

## Overview
This repository contains a smart contract named `ContractA` that implements the `Always1` function. The example demonstrates a new CVL (Certora Verification Language) feature which involves using a contract alias from an imported specification file. In this example, we have implemented a contract alias in the `Imported.spec` file and then utilized it in the `ContractAlias.spec` file to perform summarization on the `Always1` function.

## Executions

1. **Certora Run for contract alias**
    - **Command:**
        ```bash
        certoraRun ContractAlias.conf
        ```
    - **Execution Link:** [Certora Run Output](https://prover.certora.com/output/1512/7a7f575e9ce642b1a6a9c858bee09b53?anonymousKey=65196df8553cfc54b341c0e25c224e564700db08)

As observed, the summarization using the alias worked as expected, with the rule verifying for always being the value `2` instead of `1` as defined in the contract.

For a comprehensive guide on Certora Verification Language, refer to the [Certora Documentation](https://docs.certora.com).