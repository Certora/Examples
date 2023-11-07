# Structs
This directory demonstrates using solidity structs in cvl (`structs.spec`).


Run this configuration via:

```certoraRun certora/conf/runStructs.conf```

[A report of this run](https://prover.certora.com/output/1902/7465fa9a92ff47ec82d5673ad7a46803?anonymousKey=5107d6a4f583955dea934eabb2abc88a66de51d8)

The invariant `checkNumOfAccounts` passes vacuously because of the Sload on `_customers` length.

