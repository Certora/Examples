# Immutable

## Overview

In this verification process, we focus on the `Immutable.sol` smart contract, which interacts with an `Owner.sol` contract. The idea of this example is to show how we handle immutable access in CVL.

## Files

### `runImmutable.conf`

This configuration file sets the stage for our verification process. Here's what it does:

- **Contract to Verify**:
  - `Immutable.sol`

- **Linking**:
  - `Immutable:OWNER=Owner`

### `Immutable.spec`

This specification file lays out the rules to ensure the immutability of variables in `Immutable.sol`. Here's what we're checking:

- **Owner Variable**:
  - We ensure that the private `OWNER` variable in `Immutable.sol` remains unchanged when accessed via linking or direct storage access.

- **Public Variable**:
  - We verify that the public `MY_UINT` variable in `Immutable.sol` remains unchanged when accessed via direct storage access or a getter function.

### `Immutable.sol`

- **Constants**:
  - `OWNER`: This is a private immutable variable representing the owner, set during contract deployment.
  - `MY_UINT`: This is a public immutable variable holding a uint value, also set during deployment.

## Results

Check out the results [here](https://prover.certora.com/output/1512/24590eb03fe647e2928e1c8f13b3346f?anonymousKey=a1887c59ab6beb2c901e42bea28fa333d930b39c).


## How to execute
```bash
certoraRun runImmutable.conf
```
