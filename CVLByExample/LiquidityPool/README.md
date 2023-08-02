# Liquidity Pool Example

Example Certora verification for a simple multi-contract system.

The main contract is `Pool.sol`. There are several configuration files that run the Prover with different run arguments.

## Incorrect Configurations
### Pool    
    Configuration - `JustPool.conf`

    ERC20FixedWithout linking, the `integrityOfDeposit` rule will not pass, because the
    `deposit` and `balanceOf` methods are unresolved and the prover allows them to return arbitrary values.

    See [the multicontract section of the user guide][guide] for a complete
    discussion of this example.

    [guide] https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html

    
    Failing rules:
    `integrityOfDeposit`

    Commands to run:
    ```certoraRun certora/conf/JustPool.conf```

### Flashloan
    Configuration - `FlashLoanTransfer.conf`

    With the `DISPATCHER` summary, the Prover will assume that the recipient
    of the `executeOperation` method could be any contract in the scene that
    implements `executeOperation`.  The outcome of verification therefore
    depends on the set of contracts provided on the scene.
    
    See [the multicontract section of the user guide][guide] for a complete
    discussion of this example.
    
    [guide]: https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html#working-with-unknown-contracts
        
    Failing rules:
    `flashLoanIncreasesBalance`

    Commands to run:
    ```certoraRun certora/conf/FlashLoanTransfer.conf```

## Correct Configurations:

### Pool
Run:
```certoraRun certora/conf/Pool.conf``` (note: requires solc v0.8.2 due to `USDT.sol`)

```certoraRun certora/conf/WithLinking.conf```

```certoraRun certora/conf/WithFlexibleLinked.conf```

### Flashloan
Run:
```certoraRun certora/conf/FlashLoanTrivial.conf```

```certoraRun certora/conf/FlashLoanNoDispatcher.conf```

