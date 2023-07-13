# LiquidityPoolExample

Example Certora verification for a simple multi-contract system.

This repository is a work in progress; see [the Certora Tutorial][tutorial] and
[the Certora Documentation][docs] in the mean time.

[tutorial]: https://github.com/Certora/Tutorials
[docs]: https://docs.certora.com/

The main contract is 'Pool.sol`. There are several configuration files that run the prover with different
run arguments.

`Pool.sol` without additional files
Failing rules:
integrityOfDeposit

Command to run:
```certoraRun certora/conf/JustPool.conf```

```certoraRun certora/conf/FlashLoanTransfer.conf```



Correct configurations:

Commands to run:
```certoraRun certora/conf/Pool.conf```

```certoraRun certora/conf/WithLinking.conf```

```certoraRun certora/conf/WithFlexibleLinked.conf```

```certoraRun certora/conf/FlashLoanTrivial.conf```

```certoraRun certora/conf/FlashLoanNoDispatcher.conf```

