# Immutable Example README

The Immutable example showcases how to handle Immutable variables in CVL.

## First Linking to immutable variable works only if the variable is declared public.

### Public Linking Execution (Immutable.sol):

To execute on public linking (Immutable.sol), follow these steps:

```bash
certoraRun runImmutable.conf --server production --prover_version master
```

The process involves compiling Immutable.sol and exposing internal function information. The job is then submitted to the server. Track the progress and view results at [Certora Prover](https://prover.certora.com). Once completed, the detailed results will be available at [this link](https://prover.certora.com/output/1512/4fcdf5f50e6a4746a0fa72e6b7f35f51?anonymousKey=ac111a02702ff2ac73842ae71208ad0ec8f3378c).

### Private Linking Execution (PrivateImmutable.sol - same spec):

For private linking execution (PrivateImmutable.sol), use the following command:

```bash
certoraRun runPrivateImmutable.conf --server production --prover_version master
```

During this process, Owner.sol and PrivateImmutable.sol are compiled, and internal function information is exposed. However, if an error occurs, such as linking to a variable OWNER that doesn't exist in PrivateImmutable, the Certora Prover will report the issue.

```bash
CRITICAL: Encountered an error running Certora Prover:
Link to a variable OWNER that doesn't exist in the contract PrivateImmutable, neither as a state variable nor as an immutable.
```

## Second: Immutable Variable Hooks

The hook on the Immutable variable may encounter issues. When attempting to add the specified hook and ghost, execution results in a critical error. The error indicates a problem with the specification file, particularly with the named pattern root 'MY_UINT.' Ensure compatibility with solc version 0.5.13 or later.

```bash
ghost uint ghostUint256;

hook Sload uint256 _MY_UINT currentContract.MY_UINT STORAGE {
    require ghostUint256 == _MY_UINT;
}

rule UintNeverChengedUsingGhost(env e, method f, calldataarg args){
    uint256 currentGhost = ghostUint256;
    f(e, args);
    assert currentGhost == ghostUint256;
}

CRITICAL: [main] ERROR ALWAYS - Error in spec file (Immutable.spec:10:1): named pattern root 'MY_UINT' is not defined: did you spell something wrong? Note, named slots are only supported from solc 0.5.13 onward.
CRITICAL: Encountered an error running Certora Prover:
CVL specification syntax and type check failed
```


## Third: Proving Assumptions on Immutable Variables

Proving assumptions on Immutable variables is demonstrated with the following spec and contract:

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

## Fifth: Direct Storage access doesn't support (without throwing explained error)

```bash
rule DirectStorageAccess(env e){
    assert currentContract.MY_UINT ==2;
}

CRITICAL: Found errors
CRITICAL: Encountered an error running Certora Prover:
CVL specification syntax and type check failed
```