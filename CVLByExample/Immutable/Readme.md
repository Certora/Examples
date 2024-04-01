# Immutable Handling in Certora

This document outlines the procedure for handling immutable variables in CVL. Immutable variables play a crucial role in smart contract development, and ensuring their correct handling is essential for security and correctness. This README provides examples, execution instructions, and potential pitfalls related to immutable variables when using Certora.

## Overview

The Immutable example demonstrates how Certora handles immutable variables in smart contracts. Immutable variables are those whose values cannot be changed once assigned.

## 1. Linking To Public Immutable

### Execution contracts:

1. `Immutable.sol`.
2. `Owner.sol`.

### Execution spec:
`Immutable.spec`

### Execution Command:

```bash
certoraRun runImmutable.conf --server production --prover_version master
```

### Results:

Track the progress and view detailed results at [Certora Prover](https://prover.certora.com).

## 2. Linking To Private Immutable

### Execution contracts:

1. `PrivateImmutable.sol`.
2. `Owner.sol`.

### Execution spec:
`Immutable.spec`

### Execution Command:

```bash
certoraRun runPrivateImmutable.conf --server production --prover_version master
```

### Raise Error:

```bash
CRITICAL: [main] ERROR ALWAYS - Found errors in Immutable.spec:
CRITICAL: [main] ERROR ALWAYS - Error in spec file (Immutable.spec:16:29): could not type expression "OWNER(e)", message: No function-like entry for OWNER was found in the symbol table. Perhaps something was misspelled?
CRITICAL: [main] ERROR ALWAYS - Error in spec file (Immutable.spec:18:28): could not type expression "OWNER(e)", message: No function-like entry for OWNER was found in the symbol table. Perhaps something was misspelled?
```

## 3. Immutable Variable Hooks

### Issue Description:

When attempting to add hooks and ghosts to immutable variables, a critical error occur, indicating a problem with the specification file.

### Error Message:

```bash
CRITICAL: [main] ERROR ALWAYS - Error in spec file (Immutable.spec:10:1): named pattern root 'MY_UINT' is not defined: did you spell something wrong? Note, named slots are only supported from solc 0.5.13 onward.
CRITICAL: Encountered an error running Certora Prover:
CVL specification syntax and type check failed
```

## 4. Proving Assumptions on Immutable Variables

### Specification and Contract Example:

#### Specification (spec):

```solidity
// verified
rule HavocProoved(env e){
    require MY_UINT(e) == 5;
    assert getMyUint() == 6;
}
```

#### Contract:

```solidity
uint public immutable MY_UINT;

constructor() {
    OWNER = Owner(msg.sender);
    MY_UINT = 2;
}

function getMyUint() public view returns (uint) {
    return MY_UINT + 1;
}
```

## 5. Direct Storage Access Support
Works only if the private immutable variable is being used in external function.

### Execution Command:

```bash
certoraRun runPrivateImmutableDirectStorageAccess.conf --server production --prover_version master
```

### Results:

View detailed results at [this link](https://prover.certora.com/output/1512/a46f910d922a4068954d09ba377b6e72?anonymousKey=ebb0e3bac716ec48d9e600beaf4afa5094a19144).