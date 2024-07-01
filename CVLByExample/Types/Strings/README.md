# String Comparison in CVL

## Overview

This README introduces a new feature in CVL that allows for direct string comparison. This feature enables you to perform string equality checks within CVL rules, making it easier to validate contract logic involving strings.

## Why This Feature?

### Problem

Previously, comparing strings in CVL required cumbersome workarounds or conversions, which could be error-prone and complex. This made it difficult to assert string-based invariants or properties directly within CVL.

### Solution

The new string comparison feature in CVL simplifies the process by allowing direct string equality checks. This makes your verification code more readable and reduces potential errors, providing a more straightforward way to validate string-related logic.

## How to Use

### Syntax

Use the `==` operator to compare strings directly in your CVL rules. This feature works with both string literals and string variables returned by your smart contract functions.

## Example Usage

Here’s an example demonstrating how to use string comparison in CVL:

```solidity
contract String {
    function getBlurp() public returns (string memory) {
        return "Blurp";
    }
}
```

In the above contract, the `getBlurp` function returns the string "Blurp".

Now, let's use the new string comparison feature in CVL to assert that the returned string matches the expected value:

```cvl
rule cvlStringEqComparisonToEVMType {
    env e;
    string r1;

    string r2 = "Blurp";
    r1 = getBlurp(e);

    assert r1 == r2, "Should succeed";
}
```

In this example:

- **`string r1`**: A variable to store the string returned by the `getBlurp` function.
- **`string r2`**: A variable to store the expected string "Blurp".
- **`assert r1 == r2`**: Asserts that the string returned by `getBlurp` is equal to "Blurp". If the strings are equal, the assertion succeeds; otherwise, it fails with the message "Should succeed".

### Example Execution

To execute this example and verify the string comparison, use the following command:

```bash
certoraRun String.conf
```

### Verification Link

You can review the verification results for this example [here](https://prover.certora.com/output/1512/f072c50b7bc94e0f8b987fcbfc09baa9?anonymousKey=2c2dc74a750e240f621a81f46ab0ad1bbbcca7f0).