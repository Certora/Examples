# Data Invariant Example

This folder shows a **simplified** demonstration of the new `requireInvariant` semantics in Certora’s CVL. We have:

1. A **Solidity contract** (`DataInvariant.sol`) that allows negative balances to appear.
2. A **CVL specification** (`DataInvariant.spec`) that declares an invariant requiring **nonnegative** balances.
3. A **configuration file** (`DataInvariant.conf`) used to run the Certora Prover with our spec.

> **Note:** The invariant is not enforced at the time the hook is triggered in versions **before 8**, but it is enforced globally in versions **from 8 on**.

## Overview

- **`DataInvariant.sol`**  
  A contract that tracks `balance[a]` for each address and includes the `breakInvariant` function.

- **`DataInvariant.spec`**  
  - **Invariant**: `alwaysPositive(address a)` states `currentContract.balance[a] >= 0`.
    The invariant is violated when `breakInvariant` is called under the semantics from version 8 on but not under the semantics before version 8.
  - **Hook**: Whenever the contract reads `accessInvariant[user]` (i.e., an SLOAD on `accessInvariant[user]`), we call a CVL function `safeAssumptions(user)` which has a `requireInvariant alwaysPositive(user)`.

**Explanation of `requireInvariant` semantics:**  
- In versions **before 8**, `requireInvariant` was only enforced at the specific location where it was used (inside the hook, when `accessInvariant[user]` is read). This means the invariant is not guaranteed to hold globally—only at the hook point.
    - a) Negative balances can exist during a transaction, as long as the invariant holds at the hook location.
- In versions **from 8 on**, the `requireInvariant` command is enforced globally—meaning the invariant must hold before any code of a rule or invariant is executed, not just at the hook.
    - b) Negative balances are never allowed at any point where the invariant is expected to hold, so the violation is detected.

## How to Run

1. **Command** the Solidity file and run the Certora Prover using the provided config:
   ```bash
   certoraRun DataInvariant.conf
   ```

## Execution Before Version 8
See the Certora Prover output:
https://vaas-stg.certora.com/output/1512/b774667137d348039ab86be0f3a1b8f8?anonymousKey=cbd717f02b7ea78a275518c7c4ae340282789318
- Expected outcome: The invariant is only checked at the hook, so negative balances can exist temporarily during a transaction, leading to incorrect assumptions about the state of the contract.

## Execution From Version 8 On
See the Certora Prover output:
https://vaas-stg.certora.com/output/1512/09d15b32556c469f9173b33b41e01711?anonymousKey=c1369211cc8d991e1f345d9012ef655dfb495d05
- Expected outcome: The invariant is enforced globally, so any negative balance is detected as a violation, ensuring the contract state always satisfies the invariant.
