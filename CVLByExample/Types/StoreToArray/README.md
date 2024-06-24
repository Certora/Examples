# Storing Values Directly to an Array

## Overview

This README introduces a new feature in CVL that enables direct assignment of values to array elements. This feature simplifies the process of storing and verifying array elements, enhancing the efficiency and clarity of your smart contract verification.

## Why This Feature?

### Problem

Previously, storing values directly into arrays within CVL rules required multiple steps or indirect methods, leading to more complex and less readable code.

### Solution

The new feature allows you to store values directly into array elements using tuple assignments, making the code more straightforward and easier to maintain.

## How to Use

### Syntax

You can use tuple assignment to directly store values into array elements. This feature is particularly useful when dealing with functions that return multiple values which need to be assigned to specific elements in an array.

## Example Usage

Here’s an example demonstrating how to store values directly to an array:

```solidity
contract StoreToArray {
    function tuple() public returns (uint256, uint256){
        return (2, 2);
    }
}
```

In this contract, the `tuple` function returns a tuple `(2, 2)`.

Now, let's use CVL to verify that the returned value is correctly stored in an array element:

```cvl
ghost mapping(uint256 => uint256) userArray;

rule returnTuple(env e, uint256 y) {
    (userArray[y],_) = tuple(e);
    assert userArray[y] == 2;
}
```

In this example:

- **`ghost mapping(uint256 => uint256) userArray`**: Defines a ghost mapping to simulate an array in CVL.
- **`(userArray[y],_) = tuple(e)`**: Directly assigns the first element of the tuple returned by `tuple` to `userArray[y]`.
- **`assert userArray[y] == 2`**: Asserts that the value stored in `userArray[y]` is `2`.

### Example Execution

To execute this example and verify the array assignment, use the following command:

```bash
certoraRun StoreToArray.conf
```

### Verification Link

You can review the verification results for this example [here](https://prover.certora.com/output/1512/7c3d2bca534746f5b7c9e01915cf5cda?anonymousKey=691dcfaf3ecc7e099d1fbba0943494cac5c4aa21).