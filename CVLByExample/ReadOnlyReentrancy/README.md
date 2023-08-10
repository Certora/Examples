# Read Only Reentrancy

This directory contains two versions of a "bank" contract and a spec that applies the `readOnlyReentrancy` builtin rule to them.

## Incorrect Code
In `VulnerableBank.sol` the rule `readOnlyReentrancy` fails because of a possible Read-Only Reentrancy weakness at external call site at file `contracts/VulnerableBank.sol`, in function `withdraw()`.

This contract can be checked by running: 
```certoraRun certora/conf/BuiltinROReentrancyVulnerableBank.conf```

## Correct Code
The correct version is `VulnerableBankFixed.sol` the weakness was fixed by moving the update of balances before the external call.

This contract can be verified by running: 
```certoraRun certora/conf/BuiltinROReentrancyVulnerableBankFixed.conf```