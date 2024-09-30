# Demonstrating `address` Call Function

## Overview

This repository provides an example of the use of the `address` call function in CVL. The example shows how to use `address` type variables to call methods on contracts.

## Solidity Contracts

This example includes two simple Solidity contracts, `A` and `B`, each implementing a `foo` function that returns a different constant value.

### Contract A

```solidity
contract A {
    function foo() external pure returns (uint) { return 1; }
}
```

### Contract B

```solidity
contract B {
    function foo() external pure returns (uint) { return 2; }
}
```

## Specification

The specification demonstrates how to use the `address` call function to interact with the `foo` functions implemented in contracts `A` and `B`.

### Specification

```cvl
using A as a;
using B as b;

rule AddressCall {
    env e;
    address x;
    assert x.foo(e) >= 1 && x.foo(e) <= 2;
}
```

### Specification Breakdown

- **Rule `AddressCall`**:
  - This rule uses the `address` variable `x` to call the `foo` function.
  - The rule asserts that when `x` calls the `foo` function, the returned value must be between `1` and `2`, which are the possible return values from contracts `A` and `B`.

## Key Points

- **`address` Call Function**: This example illustrates how to use an `address` type variable to call functions on contracts that are associated with those addresses. This approach allows for dynamic dispatch, where the call is resolved based on the actual contract implementation.

## How to Run the Example

1. **Run Certora Prover**:
   - Command:
     ```bash
     certoraRun AddressCall.conf
     ```

2. **Check the Output**: The execution shows how the rule behaves when `x` calls the `foo` function on contracts `A` and `B`.

### Execution Links

- [Certora Run Output](https://prover.certora.com/output/1512/31a901837d034437bfbed9b2dadb0655?anonymousKey=8df67c153280c4371299a79d94e422f065ff9383)
