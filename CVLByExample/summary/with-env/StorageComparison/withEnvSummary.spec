/**
  An example for using a summary with `with env`.
*/

using Basic as basic;

methods {
  function reduceBalance(uint256 amount) internal returns (uint256) with (env e) => cvlReduceBalance(e, amount);
  function totalSupply() external returns (uint256) envfree;
}

function cvlReduceBalance(env e, uint256 amount) returns uint256  {
	uint256 poolBalance = getBalance(e, currentContract);
	require (poolBalance != 0);
	require (amount != 0);
	uint256 amountOut = decr(e);
	return amountOut;
}

rule checkReduceBalance() {
	env e;
	requireInvariant totalSupplyIsSumOfBalances();
	uint256 amountBefore = getBalance(e, e.msg.sender);
	uint256 amount;
	callReduceBalance(e, amount);
	assert (getBalance(e, e.msg.sender) == assert_uint256(amountBefore - 1), "Withdraw failed");
}

ghost mathint sum_of_balances {
    init_state axiom sum_of_balances == 0;
}

hook Sstore balance[KEY address a] uint new_value (uint old_value) STORAGE {
    // when balance changes, update ghost
    sum_of_balances = sum_of_balances + new_value - old_value;
}

// This `sload` makes `sum_of_balances >= to_mathint(balance)` hold at the beginning of each rule.
hook Sload uint256 balance balance[KEY address a]  STORAGE {
  require sum_of_balances >= to_mathint(balance);
}

//// ## Part 4: Invariants

/** `totalSupply()` returns the sum of `balanceOf(u)` over all users `u`. */
invariant totalSupplyIsSumOfBalances()
    to_mathint(totalSupply()) == sum_of_balances; 

