# Percentage Math

This example is based on [Aave's PercentageMath implementation and testing](https://github.com/aave-dao/aave-v3-origin/blob/97356e32e3c5392a995dfdf5a67f45e286eb77f4/tests/core/PercentageMath.t.sol#L21-L46).

We have added two additional, intentionally incorrect versions of `test_percentMul/Div_fuzz`:
* `test_percentMul/Div_fuzz_no_expectRevert` - This version omits `vm.expectRevert()`, demonstrating how the report appears when the fuzz test fails due to an unexpected revert.
* `test_percentMul/Div_fuzz_wrong_assert` - This version modifies the assert statement, showing how the report appears when the fuzz test fails due to an actual counterexample.

To run this example, use:
```certoraRun PercentageMath.conf```

[View the report for this run.](https://prover.certora.com/output/15800/70e5d5141ce34e4eae0f9966b78b34d9?anonymousKey=40a3a0266ff277d769a873681b1fc7829b0b5c55)

*Note: Foundry Fuzz Testing Integration is currently in an early alpha phase.*