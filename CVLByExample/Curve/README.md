
#Curve 

This directory contains a simplified contract that is based on the past 
`read-only reentrancy` vulnerability of one of the `Curve` pools described [here](https://chainsecurity.com/curve-lp-oracle-manipulation-post-mortem/)

##Contracts
The original simplified contract is `SimplifiedCurve` whose weakness is found by the builtin rule `viewReentrancy`. 
Another 
contract is `ManualInstrumentationCurve` that allows finding the weakness also with a regular rule. This is used to 
demonstrate what the builtin rule actually does.

##Specs
`certora/specs` contains two spec files for exposing this weakness.

1. `BuiltinViewReentrancy.spec` uses the builtin rule `viewReentrancy` that checks that for every solidity function and every
   view function the read-only reentrancy weakness is not present. This spec is used for finding the weakness in SimplifiedCurve.
2. `ViewReentrancy.spec` uses regular rules for checking that for every solidity function 
    the read only reentrancy weakness is not present for the view function `getVirtualPrice()` only. 
    It is not checked for all view functions.
    This is done by using ghosts for tracking:
    1. The value of `getVirtualPrice()` at the current state.
    2. The value of `getVirtualPrice()` before the unresolved call that is in the checked solidity function.
    3. The value of `getVirtualPrice()` after the unresolved call that is in the checked solidity function.
    4. The existence of a read-only weakness with respect to `getVirtualPrice()`.
    Two hooks are defined. One for updating (1) and one for updating (4).
    Additional instrumentation is required in order to catch the bug. This spec works on the contract 
    `ManualInstrumentationSimplifiedCurve`.

Both rules check the existence of the weakness by checking 
that the result of a view function after an
unresolved call is equal either to the result of this view function at the beginning or at the end of the 
calling solidity function.

Both specs find that the weakness exists in the the above contracts.

## Failing Code:

The rule `no_read_only_reentrancy` fails for function `remove_liquidity`. In `remove_liquidity` the unresolved call is performed in an unstable
state, after the call to `CurveToken(lp_token).burnFrom` and before the call to `ERC20(coins_1).transfer`.

For running the builtin rule run
```certoraRun certora/conf/broken/runViewReentrancyBuiltinRule.conf```

For running the regular rule run

```certoraRun certora/conf/broken/runViewReentrancyRegularRule.conf```

The report of this run can be found in

[Report of failure with regular rule](https://prover.certora.com/output/1902/fac7a9437752438d85472b0446247aff?anonymousKey=a1fb2c1b2e88bd10a64601831ce2cd8912d2de53)

## Correct Code

The read-only reentrancy weakness was fixed by adding at the top of each view function a requiremt
that prevents running the view function in case of an inconsistent state.

The resulting code without instrumentation is `SimplifiedCurveFixed.sol`. The command to check the builtin rule
on this contract is

```certoraRun certora/conf/correct/runViewReentrancyFixedBuiltinRule.conf```

The report of this run can be found in

[Report of correctness with builtin rule](https://prover.certora.com/output/1902/a2845c679b6a4028af918b842916ad8c?anonymousKey=fe54be4932f20347abe18ac7f7afeb9665d2a8f8)


The resulting code with instrumentation is `ManualInstrumentationSimplifiedCurveFixed`. The command to check the regular rule
on this contract is

```certoraRun certora/conf/correct/runViewReentrancyFixedRegularRule.conf```

The report of this run can be found in

[Report of correctness with regular rule](https://prover.certora.com/output/1902/a411fe10787b4a778f0b63848da18d78?anonymousKey=5c2538f9a28f026d9e471c76651212bb610bf488)


