# Teams contracts and spec - invariants examples

This folder holds an example for using invariants.
The main contract [Teams.sol](Teams.sol) implements a teams management
interface [ITeams.sol](ITeams.sol). The spec [Teams.spec](Teams.spec) uses
only invariants in the verification of the contract.
The spec also provides examples for using preserved blocks.

## Running the spec
To run the spec on the correct implementation, enter the following from
this folder ([Teams folder](./)):
```bash
certoraRun correct.conf
```

To check the buggy implementation of [ITeams.sol](ITeams.sol) found
in [TeamsBugs.sol](TeamsBugs.sol), run:
```bash
certoraRun buggy.conf
```
