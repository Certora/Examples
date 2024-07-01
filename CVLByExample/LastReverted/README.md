# Last Reverted

Some properties are required to reason about revert cases.
In this example we have a minimal implementation of ERC20 in `ERC20.sol` and we want to verify the conditions that makes the `transfer` and `approve` functions revert. In other words we want to verify that these functions will revert if and only if certain conditions are met and never in any other case (maybe excluding some invalid states). We can achieve this by using `@withrevert` and `lastReverted`.

As default, the Prover ignores reverting paths. We can signal the prover to not do that by calling the function while adding `@withrevert`.
Example:
Instead of:
```
transfer(e, recipient, amount)
```
We'll write:
```
transfer@withrevert(e, recipient, amount);
```
The prover will then store whether the function reverted in a special variable called `lastReverted`.

You can run the spec `RevertingConditions.spec` using:
```
certoraRun RevertingConditions.conf
```

[Report of this run](https://vaas-stg.certora.com/output/15800/a94059c2cbdb48f4916b79a39a3369b1?anonymousKey=0eafe130683f88d017ac61b4e18c60c1e42b6e8b)

Another feature of the prover is that the syntax checker will tell you when you're doing something wrong by using `lastReverted` after using a function without `@withrevert`. For example in `RevertingConditionsForgotWithRevert.spec` we have the same spec but we didn't store `lastReverted` and called the function `balanceOf` and used `lastReverted` afterwards.

You can run the spec `RevertingConditionsForgotWithRevert.spec` using:
```
certoraRun RevertingConditionsForgotWithRevert.conf
```

And you will get an error along the lines of:
"ERROR: Failed to compile spec files:
CRITICAL: [main] ERROR ALWAYS - Found errors in RevertingConditionsForgotWithRevert.spec:
CRITICAL: [main] ERROR ALWAYS - Error in spec file (RevertingConditionsForgotWithRevert.spec:16:76): `lastReverted` is always false after non-reverting call(s) [ERC20.balanceOf(e.msg.sender)]. Did you mean to add `@withrevert`?

CVL specification syntax and type check failed"