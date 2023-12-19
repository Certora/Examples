# Structs
This directory demonstrates using solidity structs in cvl (`structs.spec`).

Run this configuration via:

```certoraRun runStructs.conf```

[A report of this run](https://prover.certora.com/output/15800/bbf09a10c42f4e079c83924e5a151889?anonymousKey=140bc095391fe70aa2664291aa5ef6d19ab748a7)

The invariant `checkNumOfAccounts` passes vacuously because of the Sload on `_customers` length.

