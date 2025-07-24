# Sorted Array Invariant Example

This folder illustrates how the **new** `requireInvariant` semantics handle a **sorted array** property more accurately than the old semantics. We have:

## Key Points

- **Version < 8 semantics**: Using `requireInvariant` in non-boundary contexts (e.g., hooks, summaries) could lead to false verification results. The invariant might be incorrectly considered satisfied inline, missing real violations.
- **Version >= 8 semantics**: `requireInvariant` is enforced only at valid rule boundaries (e.g., after function calls, subcalls, or havocs if `strong`). This ensures that violations are properly detected.

---

## Example Overview

### Solidity Contract: `SortedArray.sol`
- **`arr`**: Public array, intended to remain sorted.
- **`insert(uint256 val)`**: Inserts `val` into the correct position in ascending order.
- **`remove(uint256 index)`**: Removes the element at `index`, shifting subsequent elements.
- **`readAt(uint256 index)`**: Returns `arr[index]`, used to trigger CVL read hooks.

### CVL Specification
- **Invariant**:  
  `isSorted(uint256 i)` requires that for each valid `i`, `arr[i] <= arr[i+1]`.
- **Hooks**:  
  On every read or write to `arr[index]`, `requireInvariant isSorted(index)` is invoked.

---

## Demonstration: Correctness and Bug Detection

### Correct Implementation

- **Old semantics**:  
  [View Output](https://prover.certora.com/output/40726/1636fb234bc74a1bba7f7ee9678b9c4f/?anonymousKey=ff15dfcf8a4da66107d4d7c7f04a49416e992b4d)  
  *May incorrectly verify even if the array is temporarily unsorted.*

- **New semantics**:  
  [View Output](https://prover.certora.com/output/40726/5811d2a30ded4dcea82460a2d1d080ac/?anonymousKey=f296e69f8f0ea379cfba6801f1e4fee8f4d39c91)  
  *Correctly enforces the invariant at rule boundaries.*

### Buggy Implementation

- **Old semantics**:  
  [View Output](https://prover.certora.com/output/40726/ca7307d763104f8abdc1dc900d1c4e5e/?anonymousKey=2b6d5374b36f9e4990c7d825e6c9bb8a292db9d8)  
  *Fails to catch the violation.*

- **New semantics**:  
  [View Output](https://prover.certora.com/output/40726/006db65557f94285af8bdbe0b8d1408f/?anonymousKey=abefdb1b51401cc4ed93ef57e70f4ed5b43bf579)  
  *Correctly detects the violation.*

---

## How to Run

1. Make sure you have the Certora CLI installed.
2. Run the specification:
   ```bash
   certoraRun SortedArray.conf
   ```

---
