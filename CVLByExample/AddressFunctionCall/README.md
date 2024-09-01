# Certora Example: Demonstrating `address` Call Function and Default Case Handling

## Overview

This repository provides an example of the use of the `address` call function in CVL. The example shows how to use `address` type variables to call methods on contracts and demonstrates what happens when an address is not properly constrained, leading to the triggering of the `assert false` default case.

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

The specification demonstrates how to use the `address` call function to interact with the `foo` functions implemented in contracts `A` and `B`, and also handles cases where the address is not properly constrained.

### Specification

```cvl
using A as a;
using B as b;

rule AddressCall {
    env e;
    address x;
    require x == a || x == b;
    assert x.foo(e) >= 1 && x.foo(e) <= 2;
}

rule AddressCallDefaultCase {
    env e;
    address x;
    assert x.foo(e) >= 1 && x.foo(e) <= 2;
}
```

### Specification Breakdown

1. **Rule `AddressCall`**:
   - This rule ensures that the `address` variable `x` is either the address of contract `A` or contract `B`.
   - The rule asserts that when `x` calls the `foo` function, the returned value must be between `1` and `2`, depending on whether `x` points to `A` or `B`.

2. **Rule `AddressCallDefaultCase`**:
   - This rule does not constrain `x` to specific addresses. 
   - If `x` is not `A` or `B`, it triggers the default case, which would result in an `assert false`, demonstrating the importance of correctly constraining address variables in your spec.

## Key Points

- **`address` Call Function**: This example illustrates how to use an `address` type variable to call functions on contracts that are associated with those addresses. This approach allows for dynamic dispatch, where the call is resolved based on the actual contract implementation.
  
- **Default Case Handling**: The `AddressCallDefaultCase` rule highlights the importance of constraining address variables to known contract addresses to avoid triggering unintended assertions or failures.

## How to Run the Example

1. **Run Certora Prover**:
   - Command:
     ```bash
     certoraRun AddressCall.conf
     ```

2. **Check the Output**: The execution shows how both rules behave, with the `AddressCall` rule passing and the `AddressCallDefaultCase` rule violating.

### Execution Links

- [Certora Run Output](https://prover.certora.com/output/1512/e34c4192698448e08b5d7ec5e201633e?anonymousKey=96a78912f5348bff7f69ac6843eacaa25c16f72e)