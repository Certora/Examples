This directory demonstrates using nativeBalances.

## FailingRules


Run this configuration via:

```certoraRun certora/conf/runBankAccount.conf```

## Configuration with `optimisticFallback`
This configuration uses the prover argument `-optimisticFallback = true` which makes the withdraw take effect also in the case of a revert.

Run this configuration via:

```certoraRun certora/conf/runBankAccountFixed.conf```
