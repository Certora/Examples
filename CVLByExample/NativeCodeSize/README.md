# Certora Example: Demonstrating `nativeCodesize` Mapping

## Overview

This repository provides an example to demonstrate the usage of the `nativeCodesize` mapping in CVL. The `nativeCodesize` mapping is used to determine whether an Ethereum address is a contract address or an Externally Owned Account (EOA) by checking the size of the code stored at the address.

## Solidity Contract

The Solidity contract `Dummy` is a minimal example used to illustrate the concept of `nativeCodesize` in CVL.

```solidity
pragma solidity ^0.8.0;

contract Dummy {
}
```

### Contract Details

- **Dummy**: A simple smart contract with no functions or state variables. It serves as a placeholder to demonstrate how Certora can verify properties related to contract addresses and EOAs using `nativeCodesize`.

### Spec

```cvl
rule nativeCodesizeContractExample(env e) {
    assert e.msg.sender == currentContract => nativeCodesize[e.msg.sender] != 0;
}

rule nativeCodesizeEOAExample(env e) {
    assert nativeCodesize[e.msg.sender] == 0 => e.msg.sender != currentContract;
}
```

### Spec Breakdown

1. **Rule `nativeCodesizeContractExample`**: This rule asserts that if the `msg.sender` is the current contract (`currentContract`), then `nativeCodesize` of `msg.sender` should not be zero. This is because contract addresses have non-zero code size.

2. **Rule `nativeCodesizeEOAExample`**: This rule asserts that if the `nativeCodesize` of `msg.sender` is zero, then `msg.sender` cannot be the current contract. This implies that `msg.sender` is an Externally Owned Account (EOA) since EOAs have zero code size.

## Key Points

- **`nativeCodesize` Mapping**: The `nativeCodesize` mapping is used to check the size of the code at a given address. A non-zero code size indicates a contract address, while a zero code size indicates an EOA.
  
- **Differentiating Addresses**: By using the `nativeCodesize` mapping, the CVL specification can differentiate between contract addresses and EOAs, enabling more precise verification of contract properties.

## How to Run the Example
   - Command:
     ```bash
     certoraRun NativeCodesize.conf
     ```
 **Check the Output**: The execution shows that both rules pass, demonstrating the correct usage of the `nativeCodesize` mapping to differentiate between contract addresses and EOAs.

### Execution Link
For an example of the output, you can check the execution link: [Certora Run Output](https://prover.certora.com/output/1512/dc42013689734ddeb8bff847b1199675?anonymousKey=7dcb6507a00ef37fa2aa01ffa383cdcda6ed488d)


For further details on Certora Verification Language and best practices, please refer to the [Certora Documentation](https://docs.certora.com).