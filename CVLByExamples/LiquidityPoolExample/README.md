# Liquidity Pool Example

Example Certora verification for a simple multi-contract system.

The main contract is `Pool.sol`. There are several configuration files that run the Prover with different run arguments.

## Incorrect Configurations
`Pool.sol` without additional files.

### Pool
Failing rules:
`integrityOfDeposit`

Commands to run:
```certoraRun certora/conf/JustPool.conf```

### Flashloan
Failing rules:
`flashLoanIncreasesBalance`

Commands to run:
```certoraRun certora/conf/FlashLoanTransfer.conf```



## Correct Configurations:

### Pool
Run:
```certoraRun certora/conf/Pool.conf``` (note: requires solc v0.8.2)

```certoraRun certora/conf/WithLinking.conf```

```certoraRun certora/conf/WithFlexibleLinked.conf```

### Flashloan
```certoraRun certora/conf/FlashLoanTrivial.conf```

```certoraRun certora/conf/FlashLoanNoDispatcher.conf```

