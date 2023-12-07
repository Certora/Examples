# Liquidity Pool Example

Example Certora Prover verification for a simple multi-contract system.

The main contract is `Pool.sol`. There are several configuration files that run the Prover with different run arguments.

## Pool
### Incorrect Configuration    
Configuration - `JustPool.conf`

Command to run:
```certoraRun JustPool.conf```

[A report of this run](https://prover.certora.com/output/1902/d4269f13ea5f4b1e8f992c7163b8c347?anonymousKey=e30eebdb5364651f210c030eef6ab47aff64aa8e)

new report: https://vaas-stg.certora.com/output/99814/1af146f27d1141d28d74bf6331677424?anonymousKey=b571503757685a501a1f56fe27e612234debe816

Without linking, the `integrityOfDeposit` rule fails, because the `deposit` and `balanceOf` methods are unresolved and the prover allows them to return arbitrary values.

View [the multi-contract section of the user guide](https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html) for a complete discussion of this example.

Failing rules:
`integrityOfDeposit`

### Fixed Configurations
```certoraRun WithLinking.conf```
[A report of this run](https://prover.certora.com/output/1902/3cfbed4ad68f465b82438ecd48250d5c?anonymousKey=17353f9eea7972711f4181ca6b14cb8414b8e6d4)

new report: https://vaas-stg.certora.com/output/99814/50a391df73384d23bebefd7fd157f1a2?anonymousKey=d32464a62dce0c362c58da87edf6bc97f852e2ea

```certoraRun WithFlexibleLinked.conf```
[A report of this run](https://prover.certora.com/output/1902/f8f52d549c104d07b9a991b99a0b1c92?anonymousKey=7c414fb9a9e35a227cfbc466f7511eac605a1045)

new report: https://vaas-stg.certora.com/output/99814/eb5ec5d397674956995752f47d0f3a2b?anonymousKey=1533a7bf708e75202767c1eb689065fe534797d5

### Full Spec
Run:
```certoraRun Pool.conf```
[A report of this run](https://vaas-stg.certora.com/output/99814/caa0e3170d3240f0830defbb48a76b12?anonymousKey=3f8a0305082babeee6cde0ce4e793e313cb7031f)


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

[A report of this run](https://vaas-stg.certora.com/output/99814/e7232c0fe25d4ef8826cd09c1e7c25f4?anonymousKey=74ab04cb863a2785b8b7db341afee5f3ee8f09dd)


### Trivial Receiver
This example will verify the spec with only a trivial `FlashLoanReceiver` implementation.

Command to run:
```certoraRun FlashLoanTrivial.conf```

[A report of this run](https://vaas-stg.certora.com/output/99814/22eb5242661f400ea396de8ba4abbdd2?anonymousKey=65d43f448782e7a7858957d6bba04fdf358314a8)


### Malicious Receiver
This example will verify the spec with a malicious receiver that transfers the money from the pool. 

Command to run:
```certoraRun FlashLoanTransfer.conf```

[A report of this run](https://vaas-stg.certora.com/output/99814/5568d1bd3071449b9641c34b6b408513?anonymousKey=97ec29267287ea7257ba7f079d5c54e30178cd35)

Configuration - `FlashLoanTransfer.conf`

Command to run:
```certoraRun FlashLoanTransfer.conf```

[A report of this run](https://prover.certora.com/output/1902/fe8df7d789294f669e3227d24b54a5b1?anonymousKey=3856de0b1fadb117128976104480007b2aefd7c9)
