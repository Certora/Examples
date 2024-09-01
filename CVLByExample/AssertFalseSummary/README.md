# Certora Example: Demonstrating `ASSERT_FALSE` Default Summary in Dispatch List

## Overview

This repository provides an example to demonstrate the usage of the `ASSERT_FALSE` default summary in a dispatch list. This example shows how mapping the default behavior of an unresolved call to `ASSERT_FALSE` ensures that the specification will fail if the call cannot be properly resolved.

## Solidity Contracts

This example includes two simple Solidity contracts: `A` and `Dummy`.

### Contract A

```solidity
contract A {
    function execute(address x, bytes calldata data) external {
        (bool success, ) = x.call(data);
    }
}
```

### Contract Dummy

```solidity
contract Dummy {}
```

### Contract Details

- **Contract A**: Implements the `execute` function, which makes an external call to a given address `x` with provided call data `data`.
- **Contract Dummy**: A placeholder contract with no implemented functions. It serves to demonstrate how unresolved calls are handled when no appropriate implementation exists.

## Specification

The specification demonstrates the use of the `ASSERT_FALSE` default summary in a dispatch list to handle unresolved calls.

### Specification

```cvl
methods {
     unresolved external in A.execute(address x, bytes calldata data) => DISPATCH [
        Dummy._
    ] default ASSERT_FALSE;
}

rule AssertFalse {
    env e;
    address x;
    bytes data;
    currentContract.execute(e, x, data);
    assert true;
} 
```

### Specification Breakdown

1. **Methods Block**:
   - **`unresolved external in A.execute(address x, bytes calldata data)`**: Specifies how unresolved external calls in the `execute` function of contract `A` should be handled.
   - **`DISPATCH [ Dummy._ ]`**: Indicates that any unresolved call should first attempt to match against functions in contract `Dummy`.
   - **`default ASSERT_FALSE`**: If no match is found, the specification will default to `ASSERT_FALSE`, causing an assertion failure.

2. **Rule `AssertFalse`**:
   - This rule is designed to fail. It calls `execute` and expects the unresolved call to result in an `ASSERT_FALSE` because `Dummy` does not implement any function that matches the call.
   - **`assert true;`**: This line is intentionally unreachable; the rule should fail before it reaches this point due to the `ASSERT_FALSE` in the dispatch list.

## Key Points

- **`ASSERT_FALSE` Default Summary**: This example illustrates how using `ASSERT_FALSE` as the default summary in a dispatch list ensures that any unresolved call without a matching implementation will cause the verification to fail.

## How to Run the Example

1. **Run Certora Prover**:
   - Command:
     ```bash
     certoraRun AssertFalse.conf
     ```

2. **Check the Output**: The execution shows that the rule `AssertFalse` fails, demonstrating that the `ASSERT_FALSE` default summary correctly causes a specification failure when no appropriate function implementation is found.

### Execution Link
[Certora Run Output](https://prover.certora.com/output/1512/833e5d3150fc481a9c0bc5f816b9e8e8?anonymousKey=33e2ef368ab2521850c7ae186c3bcc7d4d1c4b63)