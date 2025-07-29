# Rerouting Summaries for Storage Pointers

## Overview

This example demonstrates **rerouting summaries**, a CVL feature that allows summarizing internal functions that take storage pointers as parameters. This is particularly useful when dealing with complex storage structures like mappings and arrays that cannot be easily converted between EVM and CVL representations.

## Problem Statement

Internal functions that accept storage pointers as parameters (especially mappings) can not be summarized to a CVL function as of a few limitations,

1. Storage pointers cannot be converted when returned from EVM to CVL.
2. If we are dealing with mappings as parameters, there's no way to enumerate all key-value pairs

## Solution: Rerouting Summaries

A workaround is rerouting summaries that allows CVL specs to redirect internal function calls to external library methods:

```cvl
function Contract.internalFunction(...) internal => SomeLibrary.externalMethod(...)
```

The internal call is automatically rewritten to make an external delegate call to the library method, where storage pointers can be freely accessed and will correctly read/write the caller's storage.

## Files

- **`StoragePointerExample.sol`** - Contract with internal functions using storage pointers
- **`StoragePointerExample.spec`** - CVL specification with rerouting summaries
- **`StoragePointerExample.conf`** - Verification configuration

## Contract Structure

### Main Contract: `StoragePointerExample`

- **Storage**: `mapping(address => uint256[]) userDataArrays` - Main storage mapping
- **Internal Function**: `updateStorageInternal()` - Takes storage pointer and updates data
- **External Function**: `updateUserData()` - Public interface that calls internal function

### Library: `ReroutingLibrary`

- **Reroute Target**: `rerouteStorageUpdate()` - External function that handles the actual storage operations

## Key CVL Features Demonstrated

### 1. Rerouting Summary Syntax

```cvl
methods {
    function StoragePointerExample.updateStorageInternal(
        mapping(address => uint256[]) storage storageRef,
        address user,
        uint256[] memory newData
    ) internal returns (uint256[] memory) => ReroutingLibrary.rerouteStorageUpdate(storageRef, user, newData);
}
```

### 2. Storage Pointer Handling

The rerouting allows the library function to:
- Accept storage references as parameters
- Read from and write to the original contract's storage
- Maintain storage consistency across the rerouted call

### 3. Verification Rules

- **`testReroutingSummary`** - Verifies the rerouting works correctly
- **`testDataIntegrity`** - Ensures data isolation between different users
- **`testArrayBounds`** - Validates array length consistency

## Running the Verification

```bash
certoraRun StoragePointerExample.conf
```

## Expected Results

The verification should demonstrate that:

1. ✅ Internal function calls are successfully rerouted to the library
2. ✅ Storage operations work correctly through the rerouting
3. ✅ Data integrity is maintained across different storage locations
4. ✅ Array bounds and lengths are handled properly

## Benefits of Rerouting Summaries

1. **Handles Complex Storage** - Works with mappings and nested structures
2. **Maintains Storage Semantics** - Proper read/write access to original storage
3. **Simplifies Verification** - No need for complex EVM↔CVL conversions
4. **Flexible Summarization** - Can model complex internal logic externally

## Related Documentation

For more information on CVL and verification techniques, see:
- [Certora Documentation](https://docs.certora.com)