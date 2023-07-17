
#Curve 

This directory contains the contract Curve which has the read only reentrancy weakness.


##Specs
certora/specs contains two spec files for exposing this weakness.

1. BuiltinViewReentrancy.spec uses the builtin rule viewReentrancy that checks that for every solidity function and every
   view function the read only reentrancy weakness is not present.
2. ViewReentrancy.spec uses regular rules for checking that for every solidity function but only for the view function
   getVirtualPrice() the read only reentrancy weakness is not present. This is done by using ghosts for tracking:
    1. The value of getVirtualPrice() at the current state.
    2. The value of getVirtualPrice() before the unresolved call present in the solidity function.
    3. The value of getVirtualPrice() after the unresolved call present in the solidity function.
    4. The existence of read only weakness with respect to getVirtualPrice().
    Two hooks are defined. One for updating (1) and one for updating (2).

Both rules check the existence of the weakness by checking 
the result of a view function after an
unresolved call is equal either to the result of this view function at the beginning or at the end of the 
solidity function.

Both specs find that the weakness exists in the contract.

## Failing Rules:
no_read_only_reentrancy for function remove_liquidity.
