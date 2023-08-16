This directory demonstrates using solidity structs in cvl.

## Default configuration
###Failing rules:
- `storageChangesByWithdrawWithPossibleRevertShouldFail` - fails because in the case of revert the storage does not change.
- `withdrawDoesNotAffectNativeBalancesShouldFail` - fails because when the amount withdrawn is positive the storage changes.

Run this configuration via:

```certoraRun certora/conf/runBankAccount.conf```

## Configuration with `optimisticFallback`
This configuration uses the prover argument `-optimisticFallback = true` which makes the withdraw take effect also in the case of a revert.

Run this configuration via:

```certoraRun certora/conf/runBankAccountFixed.conf```
