# TransientStorage Example

## Overview
This folder contains a smart contract named `MockMutexer` that implements a reentrancey guard  mechanism using the `TransientStorage` new opcodes `tstore` and `tload`. The contract includes a modifier `contractLock` that allows the contract creator to guard desired functions against reentrancey attack. The example demonstrates new CVL feature which is `ALL_TSTORE` and `ALL_TLOAD` hooks that can be used to reason on such guard that build upon `TransientStorage`.

## Executions

1. **Certora Run for TransientStorage**
    - Command:
        ```bash
        certoraRun runTransientStorage.conf --server production --prover_version master
        ```
    - Execution Link: [Certora Run Output](https://prover.certora.com/output/1512/0362daef729843af98ea61bbb035093e?anonymousKey=0857e953173dc7f9bc1137ee4520cb16903fb71f)


For a comprehensive guide on Certora Verification Language, refer to [Certora Documentation](https://docs.certora.com).