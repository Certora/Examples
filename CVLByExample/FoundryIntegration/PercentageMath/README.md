# Percentage Math
This example is based on [Aave's PercentageMath implementation and testing](https://github.com/aave-dao/aave-v3-origin/blob/97356e32e3c5392a995dfdf5a67f45e286eb77f4/tests/core/PercentageMath.t.sol#L21-L46).

We added 2 more versions of `test_percentMul/Div_fuzz` which are intentionally incorrect:
* `test_percentMul/Div_fuzz_no_expectRevert` - Removed `vm.expectRevert()` to show how the report looks like when the fuzz test fails due to revert.
* `test_percentMul/Div_fuzz_wrong_assert` - Changed the assert to show how the report looks like when the fuzz test fails due to actual counter example.

To run this example, use:
```certoraRun PercentageMath.conf```
[Report of this run.](https://vaas-stg.certora.com/output/15800/666c55d4f8b84d1d8756e555ce399e21?anonymousKey=35611638299c531f9b3303c309ae998a32fc7fc8)

*NOTE: This Foundry Fuzz Testing Integrations is in early alpha stages.*
