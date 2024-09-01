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
This example is a full spec for LiquidityPool.

To run this use:
```certoraRun runFullPool.conf```

[A report of this run](https://prover.certora.com/output/1512/b84b2123fc1f447ba6cff06d8e07552c?anonymousKey=9917501bc57d897a7ec341a2521b30d92237f95d)

[UnsatCores](https://prover.certora.com/output/1512/ce180e9d91464a3a9271cb5bf7119125/UnsatCoreVisualisation.html?anonymousKey=88059d4e9f56250f609546f0b77ebc3ed819509d)

[Mutation test for this spec](https://mutation-testing.certora.com/?id=66c71fdd-9a1d-44e4-b084-d8d4c3de9e61&anonymousKey=e157a2be-ed9d-4d30-90bb-06b6bee05daf)

This spec discoverd a bug on PoolBroken.sol in rule sharesRoundingTripFavoursContract:
If it depolyed with underlaying asset it could get stolen by the first depositor.
A fixed version located in Pool.sol.

The Bug fixed by calculating deposit amount and use it in the conversions instead of the contract underlying asset.
The invariants noClientHasSharesWithMoreValueThanDepositedAmount, depositedAmountLessThanContractUnderlyingAsset
As been added to make sure the fix is valid. 


## Flashloan
With the `DISPATCHER` summary, the Prover assumes that the recipient
of the `executeOperation` method can be any contract in the scene that
implements `executeOperation`.  The outcome of verification therefore
depends on the set of contracts provided on the scene. In this example
we show how.

See [the multi-contract section of the user guide](https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html#working-with-unknown-contracts) for a complete discussion of this example.

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


## Strong/Weak Invariants FlashLoan

In this example, we use the `flashLoan` function to demonstrate the difference between strong and weak invariants.

### Invariant

```cvl
depositedAmount() <= underlying.balanceOf(currentContract)
filtered { f -> f.selector == sig:flashLoan(address,uint256).selector }
{
    preserved with(env e) {
        require e.msg.sender != currentContract;
    }
}
```

### Strong Invariant

The strong invariant performs the following verification process:

```solidity
function flashLoan(address receiverAddress, uint256 amount) nonReentrant() public {     
    require Inv;  // <----- start block 1     
    uint256 totalPremium = calcPremium(amount);
    require(totalPremium != 0);
    uint256 amountPlusPremium = amount + totalPremium;
    asset.transferFrom(address(this), msg.sender, amount);
    depositedAmount -= amount;
    assert Inv;  // <----- end block 1
    require(IFlashLoanReceiver(receiverAddress).executeOperation(amount, totalPremium, msg.sender), 'P_INVALID_FLASH_LOAN_EXECUTOR_RETURN');  // <--- HAVOC_ALL
    require Inv;  // <----- start block 2
    asset.transferFrom(msg.sender, address(this), amountPlusPremium);
    depositedAmount += amountPlusPremium;
    assert Inv;  // <----- end block 2
}
```

In summary, the strong invariant ensures that the invariant holds during both block 1 and block 2 of the function execution. By induction, the Prover assumes that the external call may modify the contract storage but that the invariant holds afterward. 

This version of the invariant holds during the verification process.

### Weak Invariant

The weak invariant performs the following verification process:

```solidity
require Inv;  // <----- start block 1
function flashLoan(address receiverAddress, uint256 amount) nonReentrant() public {          
    uint256 totalPremium = calcPremium(amount);
    require(totalPremium != 0);
    uint256 amountPlusPremium = amount + totalPremium;
    asset.transferFrom(address(this), msg.sender, amount);
    depositedAmount -= amount;
    require(IFlashLoanReceiver(receiverAddress).executeOperation(amount, totalPremium, msg.sender), 'P_INVALID_FLASH_LOAN_EXECUTOR_RETURN');  // <--- HAVOC_ECF
    asset.transferFrom(msg.sender, address(this), amountPlusPremium);
    depositedAmount += amountPlusPremium;
}
assert Inv;  // <----- end block 1
```

In general, the weak invariant ensures that the invariant holds after a function finishes where external call are modeled according to the definitions provided (or the Prover's defaults) 

This version of the invariant does not hold during the verification process due to the fact the havoc call manipulated the deposited amount value and make it higher than the underlying asset of the pool.
full details are shown in the following rule report.


### Execution

Command to run:
```shell
certoraRun strongInv.conf
```

[A report of this run](https://prover.certora.com/output/1512/f46d506c29e843de96df149f8b6d84ed?anonymousKey=9ddb286c9aa8932f75f7ff139fc43d9e075ae991)

### Documentation

For more details on invariants, see the [Certora Invariants Documentation](https://docs.certora.com/en/latest/docs/cvl/invariants.html).
