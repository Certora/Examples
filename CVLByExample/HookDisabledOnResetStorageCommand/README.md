# Certora Example: Demonstrating Hooks and `reset_storage`

## Overview

This repository contains an example that demonstrates how hooks behave in CVL when the `reset_storage` command is used. The example uses a simple Solidity contract named `BankReset` and a CVL specification to show that hooks do not get triggered when storage is reset.

## Solidity Contract

The Solidity contract `BankReset` is a straightforward smart contract with a `mapping` that represents funds held by different addresses and a public state variable `dontUseMe`:

```solidity
pragma solidity ^0.8.0;

contract BankReset {
    mapping (address => uint256) public funds;
    uint256 public dontUseMe;
}
```

### Contract Details

- **`funds`**: A mapping that stores the amount of funds each address has in the contract.
- **`dontUseMe`**: A public state variable intended to demonstrate that hooks aren't triggered when storage is reset.

## Spec

The specification provides two key elements:

1. **Hook Definition**: Specifies a hook that triggers on any storage update to the `dontUseMe` variable.
2. **Rule Definition**: Uses `reset_storage` to demonstrate that hooks are not triggered during storage reset.

### Specification

```cvl
hook Sstore currentContract.dontUseMe uint256 newVal (uint256 oldVal) {
    assert false, "the hook shouldn't be called";
}

rule resetZeroesAllFunds(address to, uint256 amount) {
    env e;
    require exists address a. currentContract.funds[a] > 0;
    reset_storage currentContract;
    assert forall address a. currentContract.funds[a] == 0, "all funds should be zero";
}
```

### Specification Breakdown

- **Hook `Sstore`**: This hook is set to trigger on any storage write (`Sstore`) to the variable `dontUseMe`. However, it contains an assertion `assert false` to demonstrate that if it actually invoked the rule will get a violation.
  
- **Rule `resetZeroesAllFunds`**: This rule verifies that after using the `reset_storage` command on the `BankReset` contract, all funds are zeroed out. It starts by ensuring that there exists at least one address with non-zero funds, then resets the storage and asserts that all funds are zero.

## Key Points

- **Hooks and `reset_storage`**: The main point of this example is to show that when the `reset_storage` command is executed, it does not trigger any hooks, even if the storage slots are affected.

## How to Run the Example

1. **Run Certora Prover**: 
   - Command:
     ```bash
     certoraRun BankReset.conf
     ```

3. **Check the Output**: The execution show that the rule `resetZeroesAllFunds` passes, and the hook `Sstore` for `dontUseMe` is never triggered as expected.

### Execution Link

For an example of the output, you can check the execution link: [Certora Run Output](https://prover.certora.com/output/1512/985319a08a424a6e81b8e1dcd9836848?anonymousKey=0ee6ab56949403b32b14f84c4d76ac08eb9acede)


For further details on Certora Verification Language and best practices, please refer to the [Certora Documentation](https://docs.certora.com).