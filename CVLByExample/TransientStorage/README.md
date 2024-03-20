# TransientStorage Example

## Overview
This folder contains a smart contract named `MockMutexer` that implements a reentrancey guard  mechanism using the `TransientStorage` new opcodes `tstore` and `tload`. The contract includes a modifier `contractLock` that allows the contract creator to guard desired functions against reentrancey attack. The example demonstrates new CVL feature which is `ALL_TSTORE` and `ALL_TLOAD` hooks that can be used to reason on such guard that build upon `TransientStorage`.

## Executions

1. **Certora Run for TransientStorage**
    - Command:
        ```bash
        certoraRun runTransientStorage.conf --server production --prover_version master
        ```
    - Execution Link: [Certora Run Output](https://prover.certora.com/output/1512/24c43c368dae4faba7838a42db38b758?anonymousKey=b552bb927ceab0f44804a1ad9b8d9e431721ba28)


For a comprehensive guide on Certora Verification Language, refer to [Certora Documentation](https://docs.certora.com).