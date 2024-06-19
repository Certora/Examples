# onTransactionBoundary

## Overview

This README introduces a new feature: `preserved onTransactionBoundary` for handling invariants involving transient storage in smart contracts. This feature ensures that your invariants remain sound and robust even when transient storage is reset at the end of a transaction.

## Why This Feature?

### Problem

In scenarios where transient storage is reset, contracts can violate their expected invariants. Traditional tools might miss these violations, risking unsoundness and security issues.

### Solution

The `preserved onTransactionBoundary` feature adds an extra step in the invariant verification process, ensuring that invariants hold even when transient storage is reset.

## How to Use

### Syntax

Use the new `preserved onTransactionBoundary` block to define conditions that must hold true when transient storage resets.

## Example Usage

Here’s how the feature is used in the following example:

```solidity
invariant isUnlocked(env e) 
    getLock(e) == 0;

invariant deltaZeroWhenUnlocked(env e)
    getLock(e) == 0 => getDelta(e) == 0;

invariant deltaEqualsStorage(env e)
    getDelta(e) == currentContract.storageValue
{
    preserved onTransactionBoundary with(env e2) {
        requireInvariant isUnlocked(e2);
        requireInvariant deltaZeroWhenUnlocked(e2);
    }
}
```

In this example:

- **`isUnlocked(env e)`**: Ensures that the lock is not engaged (`getLock(e) == 0`).
- **`deltaZeroWhenUnlocked(env e)`**: Ensures that if the lock is not engaged (`getLock(e) == 0`), the delta must be zero (`getDelta(e) == 0`).
- **`deltaEqualsStorage(env e)`**: Ensures that the delta matches the current contract’s storage value.

The `preserved onTransactionBoundary` block is used to reinforce these invariants, verifying that they hold true even if the transient storage is reset.

### Example Execution

To execute the example with the new feature, use the following command:

```bash
certoraRun WithPreservedOnTransaction.conf
```

### Verification Link

You can review the verification results [here](https://prover.certora.com/output/1512/a2864876bbe34603938fdec9e892a6b8?anonymousKey=3d3107a11d56a51ba53e2e341b8cc762ce15de65).

### Verification Link Without the preserved onTransactionBoundary

You can review the verification results without using the `preserved onTransactionBoundary` feature [here](https://prover.certora.com/output/1512/1ec1f5724fd54c6cb2847fff9cb75a1a?anonymousKey=ad4123afe1d80b9b00087756d2b83ad7204523df).

As you can see, the invariant `deltaEqualsStorage` doesn't hold due to the reset of the transient storage.