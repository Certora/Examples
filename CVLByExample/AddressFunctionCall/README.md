# Certora Example: Demonstrating `address` Call Function and Default Case Handling

## Overview

This repository provides an example of the use of the `address` call function in CVL. The example shows how to use `address` type variables to call methods on contracts.

## Solidity Contracts

This example includes 3 simple Solidity contracts, `A`, `B`, and `C`, the first two implementing a `foo` function that returns a different constant value, and the `C` which does not have an implementation of `foo`.

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

### Contract C

```solidity
contract C {
    function bar() external pure returns (uint) { return 3; }
}
```

## Specification

The specification demonstrates how to use the `address` call function to interact with the `foo` functions implemented in contracts `A` and `B`.

### Specification

```cvl
using A as a;
using B as b;
using C as c;

rule AddressCall {
    env e;
    address x;

    assert x.foo(e) >= 1 && x.foo(e) <= 2;

    assert x != c;
    assert x.foo(e) == 1 => x == a;
    assert x.foo(e) == 2 => x == b;
}
```

### Specification Breakdown

**Rule `AddressCall`**

- The rule asserts that when `x` calls the `foo` function, the returned value must be between `1` and `2`, depending on whether `x` points to `A` or `B`.
- The rule then demonstrates how only the cases where `x` points to one of `A` or `B` are considered at all, and specifically `C` is not an option because it doesn't implement a `foo` function.

## Key Points

- **`address` Call Function**: This example illustrates how to use an `address` type variable to call functions on contracts that are associated with those addresses. This approach allows for dynamic dispatch, where the call is resolved based on the actual contract implementation.

- **Default Case Handling**: The rule demonstrates that only the cases where the `address` variable points to a valid contract that implements the given function are considered.

## How to Run the Example

1. **Run Certora Prover**:
   - Command:

     ```bash
     certoraRun AddressCall.conf
     ```

2. **Check the Output**: The execution shows how both rules behave, with the `AddressCall` rule passing and the `AddressCallDefaultCase` rule violating.

### Execution Links

- [Certora Run Output](https://prover.certora.com/output/97560/450f6bac559e464fb77123f37a8ccc0c?anonymousKey=743f130067fe3be2f4464f12efedebc762fa58ca)
