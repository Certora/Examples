# Liquidity Pool Example

Example Certora Prover verification for a simple multi-contract system.

The main contract is `Pool.sol`. There are several configuration files that run the Prover with different run arguments.

## Pool
### Incorrect Configuration    
Configuration - `JustPool.conf`

Command to run:
```certoraRun JustPool.conf```

[A report of this run](https://prover.certora.com/output/15800/4f7dce6f812d442c8f63d418d900c9da?anonymousKey=5123a95b7bc1bf2b7ad4477db98d3ee0396bb9ce)

Without linking, the `integrityOfDeposit` rule fails, because the `deposit` and `balanceOf` methods are unresolved and the prover allows them to return arbitrary values.

View [the multi-contract section of the user guide](https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html) for a complete discussion of this example.


### Fixed Configurations
```certoraRun WithLinking.conf```
[A report of this run](https://prover.certora.com/output/15800/2b99f9c5d89c4b68937ff28f5f1c37e9?anonymousKey=795fbaf1a0c88259d362f286e4c04cafcd096971)


```certoraRun WithFlexibleLinked.conf```
[A report of this run](https://prover.certora.com/output/15800/58865a8c625c484c861e84b3e1c144e1?anonymousKey=e9d3041c2b0d2179fefed833f15663010e7c7b50)


### Full Spec
Run:
```certoraRun Pool.conf```
[A report of this run](https://prover.certora.com/output/15800/d334ef766b4e42f2a9285ed2bd12307f?anonymousKey=e46391e835ef8ffae1adc9f13d2fd3ff50a5ef2c)


## Flashloan
With the `DISPATCHER` summary, the Prover assumes that the recipient
of the `executeOperation` method can be any contract in the scene that
implements `executeOperation`.  The outcome of verification therefore
depends on the set of contracts provided on the scene. In this example
we show how.

See [the multi-contract section of the user guide](https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html#working-with-unknown-contracts) for a complete discussion of this example.

### Vacuous Rule
This example will verify the spec with no valid dispatchers on the scene; this will treat the method as a `HAVOC_ALL` summary. The rule is vacuous.

Command to run:
```certoraRun FlashLoanNoDispatcher.conf```

[A report of this run](https://prover.certora.com/output/15800/3ea6afb6b1c943b88c9f03d6bba5bc98?anonymousKey=db9d6c66345146546b60b4545e4af858296f2a76)


### Trivial Receiver
This example will verify the spec with only a trivial `FlashLoanReceiver` implementation.

Command to run:
```certoraRun FlashLoanTrivial.conf```

[A report of this run](https://prover.certora.com/output/15800/fbce8f9c08b342ecbc092f866ef06e3a?anonymousKey=183be851fe7b6f36e2de0063498f0697cc1ae6ca)


### Malicious Receiver
This example will verify the spec with a malicious receiver that transfers the money from the pool. 

Command to run:
```certoraRun FlashLoanTransfer.conf```

[A report of this run](https://prover.certora.com/output/15800/369ebb72bb20457e9856d1b5950330ef?anonymousKey=badcb6d6ba4411745bf47efa0f19ad7b9c00b362)
