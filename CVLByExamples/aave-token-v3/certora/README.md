## Verification Overview
The current directory contains Certora's formal verification of AAVE's V3 token.
In this directory you will find three subdirectories:

1. specs - Contains all the specification files that were written by Certora for the token code. We have created two spec files, `base.spec`, `delegate.spec`, `erc20.spec` and `general.spec`.
- `base.spec` contains method declarations, CVL functions and definitions used by the main specification files
- `delegate.spec` contains rules that prove various delegation properties
- `erc20.spec` contains rules that prove ERC20 general rules, e.g. correctness of transfer and others
- `general.spec` contains general delegation invariants, e.g. sum of delegated and undelegated balances equals to 
total supply  

2. scripts - Contains all the necessary run scripts to execute the spec files on the Certora Prover. These scripts composed of a run command of Certora Prover, contracts to take into account in the verification context, declaration of the compiler and a set of additional settings. 
- `verifyDelegate.sh` is a script for running `delegate.spec`
- `verifyGeneral.sh` is a script for running `general.spec`
- `erc20.sh` is a script for running `erc20.spec`

3. harness - Contains all the inheriting contracts that add/simplify functionalities to the original contract.
We use two harnesses:
- `AaveTokenV3Harness.sol` used by `erc20.sh` and `delegate.sh`. It inherits from the original AaveV3Token 
contract and adds a few getter functions.

- `AaveTokenV3HarnessStorage.sol` used by `general.sh`. It uses a modified a version of AaveV3Token contract
where the `delegationState` field of the `_balances` struct is refactored to be of type uint8 instead of
`DelegationState` enum. This is done in order to bypass a current limitation of the tool and write a hook
on the `delegationState` field (hooks don't support enum fields at the moment)


</br>

---

## Running Instructions
To run a verification job:

1. Open terminal and `cd` your way to the main aave-token-v3 directory

2. Run the script you'd like to get results for:
    ```
    sh certora/scripts/verifyDelegate.sh
    sh certora/scripts/verifyGeneral.sh
    sh certora/scripts/erc20.sh
    ```
