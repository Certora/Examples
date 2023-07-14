# Liquidity Pool Example

Example Certora verification for a simple multi-contract system.

The main contract is `Pool.sol`. There are several configuration files that run the Prover with different run arguments.

## Incorrect Configurations
`Pool.sol` without additional files.

Failing rules:
`integrityOfDeposit`

Commands to run:
```certoraRun certora/conf/JustPool.conf```

```certoraRun certora/conf/FlashLoanTransfer.conf```



## Correct Configurations:

Run:
```certoraRun certora/conf/Pool.conf```

```certoraRun certora/conf/WithLinking.conf```

```certoraRun certora/conf/WithFlexibleLinked.conf```

```certoraRun certora/conf/FlashLoanTrivial.conf```

```certoraRun certora/conf/FlashLoanNoDispatcher.conf```

