# TransientStorage Example

## Overview
This folder contains a smart contract named `MockMutexer` that implements a reentrancey guard  mechanism using the `TransientStorage` new opcodes `tstore` and `tload`. The contract includes a modifier `contractLock` that allows the contract creator to guard desired functions against reentrancey attack. The example demonstrates new CVL feature which is `ALL_TSTORE` and `ALL_TLOAD` hooks that can be used to reason on such guard that build upon `TransientStorage`.

## Executions

1. **Certora Run for TransientStorage**
    - Command:
        ```bash
        certoraRun runTransientStorage.conf --server production --prover_version master
        ```
    - Execution Link: [Certora Run Output](https://prover.certora.com/output/1512/fccdea39442a44b187ec6f502813dfc0?anonymousKey=a9adfb33e16e37ab6ad2467a0fd8b89a4b644f86)


For a comprehensive guide on Certora Verification Language, refer to [Certora Documentation](https://docs.certora.com).