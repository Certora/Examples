# TransientStorage Example with transient field syntax

## Overview
This folder contains a smart contract named `TransientTest` that implements a simple lock via a transient boolean field. The spec file demonstrate how we can use the `Tstore` and `Tload` hooks to hook on accesses to such fields, and shows also that we can use direct storage access from CVL on them as well.

## Executions

1. **Certora Run for TransientStorage**
    - Command:
        ```bash
        certoraRun Default.conf --server production
        ```
    - Execution Link: [Certora Run Output](https://prover.certora.com/output/950033/96f75ac15d9346bd995b581283f90a84?anonymousKey=19abd76348fe169eca42f406c5da5d9fff3da1a9)


For a comprehensive guide on Certora Verification Language, refer to [Certora Documentation](https://docs.certora.com).