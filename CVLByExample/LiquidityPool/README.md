# Liquidity Pool Example

Example Certora Prover verification for a simple multi-contract system.

The main contract is `Pool.sol`. There are several configuration files that run the Prover with different run arguments.

## Incorrect Configurations
### Pool    
    Configuration - `runJustPool.conf`

    Command to run:
    ```certoraRun certora/conf/runJustPool.conf```

    [A report of this run](https://prover.certora.com/output/1902/d4269f13ea5f4b1e8f992c7163b8c347?anonymousKey=e30eebdb5364651f210c030eef6ab47aff64aa8e)

    Without linking, the `integrityOfDeposit` rule fails, because the `deposit` and `balanceOf` methods are unresolved and the prover allows them to return arbitrary values.

    View [the multi-contract section of the user guide](https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html) for a complete discussion of this example.

    Failing rules:
    `integrityOfDeposit`

### Flashloan
    - Configuration - `runFlashLoanTransfer.conf`

        Command to run:
        ```certoraRun certora/conf/runFlashLoanTransfer.conf```

        [A report of this run](https://prover.certora.com/output/1902/fe8df7d789294f669e3227d24b54a5b1?anonymousKey=3856de0b1fadb117128976104480007b2aefd7c9)

        With the `DISPATCHER` summary, the Prover assumes that the recipient
        of the `executeOperation` method can be any contract in the scene that
        implements `executeOperation`.  The outcome of verification therefore
        depends on the set of contracts provided on the scene.
        
        See [the multi-contract section of the user guide](https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html#working-with-unknown-contracts) for a complete discussion of this example.
            
        Failing rules:
        `flashLoanIncreasesBalance`
    

## Correct Configurations

### Pool
Run:
```certoraRun certora/conf/runPool.conf``` 
[A report of this run](https://prover.certora.com/output/1902/a292c83831784a0c861003f635f6dd0b?anonymousKey=d61f700385c4d9ba4deeafb43f392ae2b588af42)

```certoraRun certora/conf/runWithLinking.conf```
[A report of this run](https://prover.certora.com/output/1902/3cfbed4ad68f465b82438ecd48250d5c?anonymousKey=17353f9eea7972711f4181ca6b14cb8414b8e6d4)

```certoraRun certora/conf/runWithFlexibleLinked.conf```
[A report of this run](https://prover.certora.com/output/1902/f8f52d549c104d07b9a991b99a0b1c92?anonymousKey=7c414fb9a9e35a227cfbc466f7511eac605a1045)

### Flashloan
Run:
```certoraRun certora/conf/runFlashLoanTrivial.conf```
[A report of this run](https://prover.certora.com/output/1902/5f44ac96808749e19cc5c2ff5c1091f3?anonymousKey=3dc20fabed4e64eadb37aca12d05d810d307e6cd)

```certoraRun certora/conf/runFlashLoanNoDispatcher.conf```
[A report of this run](https://prover.certora.com/output/1902/90cb64691d464f199c0c0b2ac393bbdb?anonymousKey=3a1dc2d5332c2b87ba98695818c6d32ec8c53c31)
 
The rule `flashLoanIncreasesBalance` passes vacuously because there are no contracts in the scene that implement the `executeOperation` method.

