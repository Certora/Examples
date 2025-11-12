# Demonstrating Calling an internal function directly from CVL

## Overview

This repository provides an example of calling internal functions directly from a CVL specification file.

## Solidity Contracts

This example includes a simple Solidity contract, `A`, which has a few internal functions with different signatures

### Contract A

```solidity
contract A {
    struct S {
        int i;
    }

    S s;

    function anInternalFunction() internal returns (uint) { return 0; }
    function summarizedInternal() internal returns (uint) { return 0; }

    function internalFunctionWithStorageInput(S storage _s) internal { s = _s; }
    function internalFunctionWithStorageOutput() internal returns (S storage) { return s; }
}
```

## Specification

The specification demonstrates how one can call the internal functions directly from spec.

### Specification

```cvl
methods {
    function summarizedInternal() internal returns (uint) => cvlSummary();
    // function anInternalFunction() internal returns (uint) envfree; <-- This will fail compilation: 'The envfree qualifier is not allowed on internal functions'
}

function cvlSummary() returns (uint) {
    return 1;
}

rule internalFunctionCall {
    env e;

    assert anInternalFunction(e) == 0;
    assert summarizedInternal(e) == 1;

    // A.S s;
    // internalFunctionWithStorageInput(e, s); <-- This will fail compilation: 'could not type expression "internalFunctionWithStorageInput(e,s)", message: Cannot call internal function internalFunctionWithStorageInput from spec because input parameter '_s' has storage location'
    // internalFunctionWithStorageOutput(e); <-- This will fail compilation: 'could not type expression "internalFunctionWithStorageOutput(e)", message: Cannot call internal function internalFunctionWithStorageOutput from spec because output parameter #0 has storage location'
}
```

### Specification Breakdown

- **`methods` block**:
  - Summarize the internal function `summarizedInternal` to a CVL function that returns a constant `1`.
  - Demonstrates that one cannot declare an internal function as `envfree`.

- **Rule `internalFunctionCall`**:
  - Call the internal function `anInternalFunction`. Notice how the syntax is exactly the same as calling an external function.
  - Call the internal function `summarizedInternal`. This call demonstrates that in contrast to how external function calls work, where the contract
  implementation is always inlined when the function is called from spec (even if it has a summary), in the internal function case the summary will be inlined.
  - Demonstrate that calling internal functions with input or output parameters with `storage` location won't compile.

## How to Run the Example

1. **Run Certora Prover**:
   - Command:
     ```bash
     certoraRun InternalFunctionCall.conf
     ```

2. **Check the Output**: The execution shows how the internal function (or its summary) is inlined in the CVL rule.

### Execution Links

- [Certora Run Output](https://prover.certora.com/output/97560/85cdc83bc611411da28ac63f76e2e445?anonymousKey=64077f14f694570579878704b14adb86c7581724)
