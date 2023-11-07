# Storage Comparison Examples
This directory illustrates storage comparison (`storage.spec`).
It includes an example specification for comparing `lastStorage` and `nativeBalances`.
The spec demonstrates:
1. Changes in storage in case of successful/unsuccessful transactions.
2. Changes in `lastStorage` when changing data structures of the current contract.
3. The relation between the balances of the sender and the receiver of a transaction.
4. Comparison of 
    - the full storage 
    - storage of a specific contract 
    - storage of nativeBalances

## Failing rules:
- `withdrawDoesNotAffectNativeBalancesShouldFail` - fails because when the amount withdrawn is positive the storage changes.
- `ghostStorageComparison` - fails because comparing storage includes the storage for ghosts and the ghost storage for the number of operations changes with each operation.

Run this configuration via:

```certoraRun certora/conf/runStorage.conf```
[Report of this run](https://prover.certora.com/output/1902/658391048d1c49849074fe64f92e6b94?anonymousKey=659d643f47eda07a4978061d30b1d81d700372fc)

