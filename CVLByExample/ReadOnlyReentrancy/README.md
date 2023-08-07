# Read Only Reentrancy

This directory contains four versions of a "bank" contract and a spec that applies the `readOnlyReentrancy` builtin rule to them.

## Incorrect Versions
In `VulnerableBank.sol` and `VulnerableBankOther.sol` the rule `readOnlyReentrancy` fails because of a possible Read-Only Reentrancy weakness at external call site in function `withdraw()`.


These contracts can be checked by running: 
```certoraRun certora/conf/BuiltinROReentrancyVulnerableBank.conf```
```certoraRun certora/conf/BuiltinROReentrancyVulnerableBankOther.conf```
respectively

## Correct Code
The correct versions are `VulnerableBankFixed.sol` `VulnerableBankOtherFixed.sol` where the weakness was fixed by moving the update of balances before the external call.

This contract can be verified by running: 
```certoraRun certora/conf/BuiltinROReentrancyVulnerableBankFixed.conf```
```certoraRun certora/conf/BuiltinROReentrancyVulnerableBankOtherFixed.conf```

