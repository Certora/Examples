
#Curve 

This directory contains a mock contract we've written that is based on the past 
read only reentrancy vulnerability of one of the `Curve`
 pools. 

##Contracts
The original contract is `Curve`` whose weakness is found by the builtin rule viewReentrancy. In addition we have the
contract MungedCurve that allows finding the weakness also with a regular rule.

##Specs
`certora/specs`` contains two spec files for exposing this weakness.

1. `BuiltinViewReentrancy.spec` uses the builtin rule `viewReentrancy` that checks that for every solidity function and every
   view function the read only reentrancy weakness is not present. This spec is used for finding the weakness in Curve.
2. `ViewReentrancy.spec`` uses regular rules for checking that for every solidity function 
    the read only reentrancy weakness is not present for the view function `getVirtualPrice()`. It is not checked for all
    view functions.
    This is done by using ghosts for tracking:
    1. The value of `getVirtualPrice()` at the current state.
    2. The value of `getVirtualPrice()` before the unresolved call that is in the solidity function.
    3. The value of `getVirtualPrice()` after the unresolved call that is in the solidity function.
    4. The existence of a read only weakness with respect to `getVirtualPrice()`.
    Two hooks are defined. One for updating (1) and one for updating (4).
    Additional munging is required in order to catch the bug. This spec works on the contract `MungedCurve`.

Both rules check the existence of the weakness by checking 
that the result of a view function after an
unresolved call is equal either to the result of this view function at the beginning or at the end of the 
solidity function.

Both specs find that the weakness exists in the contract.

## Failing Rules:
`no_read_only_reentrancy` for function `remove_liquidity`. In `remove_liquidity` the unresolved call is performed in an unstable
state, after the call to `CurveToken(lp_token).burnFrom` and before the call to `ERC20(coins_1).transfer`.
