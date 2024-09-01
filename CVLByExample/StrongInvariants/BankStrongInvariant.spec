
/*
Property: Sum of balances

The sum of all balances is not less than then native balance the contract holds.

This property is implemented with a ghost, an additional variable that tracks changes to the balance mapping.

This property should hold on untrusted external calls, therfor we define it as a strong invariant 

Formula:
    
    sum(balanceOf(u) for all address u) <= currentContract.balance

*/

ghost mathint sumBalances{
    // assuming value zero at the initial state before constructor 
	init_state axiom sumBalances == 0; 
}


/* here we state when and how the ghost is updated */
hook Sstore userBalances[KEY address a] uint256 new_balance
// the old value that balances[a] holds before the store
    (uint256 old_balance) {
  sumBalances = sumBalances + new_balance - old_balance;
}

strong invariant sumFunds() 
	sumBalances <= to_mathint(nativeBalances[currentContract])
     { preserved with (env e) {
            // contract does not call itself 
            require e.msg.sender != currentContract;
        }
     }

