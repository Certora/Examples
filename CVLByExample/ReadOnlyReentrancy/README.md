# Read Only Reentrancy

This directory contains two versions of a "bank" contract and a spec that applies the `readOnlyReentrancy` builtin rule to them.

## Incorrect Code
In `VulnerableBank.sol` the rule `readOnlyReentrancy` fails because of a possible Read-Only Reentrancy weakness at external call site at file `contracts/VulnerableBank.sol`, in function `withdraw()`.

This contract can be checked by running: 
```certoraRun certora/conf/runBuiltinROReentrancyVulnerableBank.conf```

[A report of this run](https://prover.certora.com/output/1902/6aa4f737e4434e33877696ca30ed4167?anonymousKey=30fa0e2f7941116692d5972337edf6e380b67faf)

## Correct Code
The correct version is `VulnerableBankFixed.sol` the weakness was fixed by moving the update of balances before the external call.

This contract can be verified by running: 
```certoraRun certora/conf/BuiltinROReentrancyVulnerableBankFixed.conf```

[A report of this run](https://prover.certora.com/output/1902/ba6e0019d98a40eb9841f509e6cde5c2?anonymousKey=27d4425bb1d0cb00a4bd413c3a11bf77cfb4d757)