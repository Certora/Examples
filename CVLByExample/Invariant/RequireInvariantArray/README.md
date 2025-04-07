# Sorted Array Invariant Example

This folder illustrates how the **new** `requireInvariant` semantics handle a **sorted array** property more accurately than the old semantics. We have:

1. A **Solidity contract** (`SortedArray.sol`) that maintains an ascending-ordered array.
2. A **CVL specification** that enforces a **“isSorted”** invariant using a **read hook**.

Under the **old semantics**, the solver might incorrectly treat the invariant as satisfied inline, potentially missing real violations. Under the **new semantics**, the invariant is enforced at valid rule boundaries, catching unsorted states properly.

---

## Overview

### `SortedArray.sol`
- **`arr`**: A public array to remain sorted.
- **`insert(uint256 val)`**: Inserts `val` into the correct position in ascending order.
- **`remove(uint256 index)`**: Removes the element at `index`, shifting subsequent elements.
- **`readAt(uint256 index)`**: Returns `arr[index]`, triggering our CVL read hook.

### Specification Highlights
- **`invariant isSorted(uint256 i)`**  
  Requires that for each valid `i`, `arr[i] <= arr[i+1]`.  
- **`hook Sload ... arr[INDEX uint256 index]`**  
  Whenever `readAt(index)` is called, a CVL function `safeSortedAssumption(index)` invokes `requireInvariant isSorted(index)`.

In **old semantics**, the check might be **inline**, potentially passing even if the array is temporarily unsorted. In **new semantics**, the captured indices are enforced at rule boundaries or after subcalls/havocs if `strong`, ensuring violations are caught.

---

## Comparing Execution Outputs

- **Old Semantics**  
  [View Output](https://vaas-stg.certora.com/output/1512/784d8a16d9c748ad980619483fe391b0?anonymousKey=4754ecd79909b410927a0af9c3d77afda15d6534)  
  Result: The invariant may appear verified even in scenarios where the array is in fact unsorted (inside the transaction context).

- **New Semantics**  
  [View Output](https://vaas-stg.certora.com/output/1512/7cfd8d2823634113b906b60cba100e30?anonymousKey=176275751817ac50ed1647bc9bed70b700680b42)  
  Result: Any genuine violation of sortedness is caught at rule boundaries, causing the verification to fail correctly.

---

## How to Run
1. Use the Certora CLI:
   ```bash
   certoraRun SortedArray.conf
