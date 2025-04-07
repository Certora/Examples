# Data Invariant Example

This folder shows a **simplified** demonstration of the new `requireInvariant` semantics in Certora’s CVL. We have:

1. A **Solidity contract** (`DataInvariant.sol`) that allows negative balances to appear.
2. A **CVL specification** (`DataInvariant.spec`) that declares an invariant requiring **nonnegative** balances.
3. A **configuration file** (`DataInvariant.conf`) used to run the Certora Prover with our spec.

Under the **old** semantics, the invariant won't be enforced at the time the hook triggered, leading to a **false passing** invariant execution. Under the **new** `requireInvariant` semantics, the invariant is checked at rule boundaries or after calls/havocs for strong invariants, correctly **failing** when a negative balance occurs.

## Overview

- **`DataInvariant.sol`**  
  A contract that tracks `balance[a]` for each address and includes the `breakInvariant` function.

- **`DataInvariant.spec`**  
  - **Invariant**: `alwaysPositive(address a)` states `currentContract.balance[a] >= 0`.
    The invariant is violated when `breakInvariant` is called under the new semantics but not under the old semantics.
  - **Hook**: When the contract reads `accessInvariant[user]`, we call a CVL function `safeAssumptions(user)` which has a `requireInvariant alwaysPositive(user)`.
## How to Run

1. **Command** the Solidity file and run the Certora Prover using the provided config:
   ```bash
   certoraRun DataInvariant.conf
   ```

## Execution Under the Old Semantic
See the Certora Prover output:
https://vaas-stg.certora.com/output/1512/b774667137d348039ab86be0f3a1b8f8?anonymousKey=cbd717f02b7ea78a275518c7c4ae340282789318
- Expected outcome: The invariant verified incorrectly, allowing negative balances as long as they occur in the transaction but not after the transaction. This leads to incorrect assumptions about the state of the contract.

## Execution Under the New Semantic
See the Certora Prover output:
https://vaas-stg.certora.com/output/1512/09d15b32556c469f9173b33b41e01711?anonymousKey=c1369211cc8d991e1f345d9012ef655dfb495d05
- Expected outcome: The invariant correctly violated when a negative balance arises. This leads to incorrect assumptions about the state of the contract.
