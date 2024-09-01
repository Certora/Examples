# Certora Example: Demonstrating `address` Call Function

## Overview

This repository provides an example of the use of the `address` call function in CVL. The example shows how to use `address` type variables to call methods and perform checks on contracts that implement those methods.

## Solidity Contracts

This example includes two simple Solidity contracts, `A` and `B`, each implementing a `balaceOf` function that returns a different constant value.

### Contract A

```solidity
contract A {
    function balaceOf() external pure returns (uint) { return 1; }
}
```

### Contract B

```solidity
contract B {
    function balaceOf() external pure returns (uint) { return 2; }
}
```

## Specification

The specification demonstrates how to use the `address` call function to interact with the `balaceOf` functions implemented in contracts `A` and `B`.

### Specification

```cvl
using A as a;
using B as b;

rule AddressCall {
    env e;
    address x;
    require x == a || x == b;
    assert x == a => x.balaceOf(e) == 1;
    assert x == b => x.balaceOf(e) == 2;
}
```

## Key Points

- **`address` Call Function**: This example illustrates how to use an `address` type variable to call functions on contracts that are associated with those addresses. This approach allows for dynamic dispatch, where the call is resolved based on the actual contract implementation.

## How to Run the Example

1. **Run Certora Prover**:
   - Command:
     ```bash
     certoraRun AddressCall.conf
     ```

2. **Check the Output**: The execution shows that the rule `AddressCall` passes, demonstrating the correct usage of the `address` call function to interact with different contract implementations.

### Execution Link
[Certora Run Output](https://prover.certora.com/output/1512/22658bf6864441d8986dba87b92fc927?anonymousKey=bc8dc7b9432ef3870a1289872545f8ce3cef112f)