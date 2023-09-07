This directory demonstrates using solidity structs in cvl (`structs.spec`) and storage changes (`storage.spec`).


## Storage Examples
### Default configuration
###Failing rules:
- `storageChangesByWithdrawWithPossibleRevertShouldFail` - fails because in the case of revert the storage does not change.
- `withdrawDoesNotAffectNativeBalancesShouldFail` - fails because when the amount withdrawn is positive the storage changes.
- `witnessNativeBalanceChangesByWithdraw` - fails because of the unresolved function in `withdraw`.

Run this configuration via:

```certoraRun certora/conf/runBankAccount.conf```

## Configuration with `optimisticFallback`
This configuration uses the prover argument `-optimisticFallback = true` which makes the withdraw take effect also in the case of a revert.
The rules that fail with the default configuration and pass with this configuration:
- `witnessStorageChangesByWithdraw`
- `storageAfterTwoWithdrawFromInitShouldPass`

Run this configuration via:

```certoraRun certora/conf/runBankAccountFixed.conf```
