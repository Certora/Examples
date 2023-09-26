using Basic as basic;

methods {
  function _.receiveCash() external => NONDET;
  function withdraw(uint256 amount) external returns (uint256) with (env e) => cvlWithdraw(e, amount);
  function sharesToAmount(uint256 shares) external returns (uint256) envfree;
  function totalSupply() external returns (uint256) envfree;
}

function cvlWithdraw(env e, uint256 amount) returns uint256  {
	uint256 poolBalance = getBalance(e, currentContract);
	require (poolBalance != 0);
	// uint256 amountOut = sharesToAmount(shares);
	require (amount != 0);
	decr(e);
	transfer(e, currentContract, amount);
	return amount;
}

// ghost mathint totalTransferred;

// hook Sload uint x Basic.balance[KEY address a] STORAGE {
// 	totalTransferred = totalTransferred + x;
// }

rule checkWithdraw() {
	env e;
	requireInvariant totalSupplyIsSumOfBalances();
	uint256 amountBefore = getBalance(e, e.msg.sender);
	uint256 amount;
	uint256 amountWithdrawn = withdraw(e, amount);
	assert (getBalance(e, e.msg.sender) == assert_uint256(amountBefore - 1 - amountWithdrawn), "Withdraw failed");
}

rule should_pass_1 {
	storage init = lastStorage;
	env e;
	incr(e);
	incr(e);
	decr(e);
	decr(e);
	assert init[basic] == lastStorage[basic];
}

rule should_pass_2 {
	env e;
	incr(e);
	storage init = lastStorage;
	incr(e);
	decr(e);
	assert init[basic] == lastStorage[basic];
}

rule should_pass_3 {
	env e;
	env e2;
	address target;
	uint amount;

	storage init = lastStorage;
	transfer(e, e2.msg.sender, amount);
	transfer(e2, target, amount);
	storage s1 = lastStorage;
	transfer(e, target, amount) at init;
	assert s1[basic] == lastStorage[basic];
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

// rule should_pass_4 {
// 	env e;
// 	storage init = lastStorage;
// 	address x;
// 	butThenAlsoSend(e, x);
// 	assert init[basic] == lastStorage[basic];
// }

// rule should_pass_5 {
// 	env e;
// 	storage init = lastStorage;
// 	require(e.msg.sender == t);
// 	receiveCash(e);
// 	assert init[nativeBalances] == lastStorage[nativeBalances];
// }

// rule should_pass_6 {
// 	env e;
// 	storage init = lastStorage;
// 	require(e.msg.sender == t);
// 	butThenAlsoSend(e, t);
// 	assert init[nativeBalances] == lastStorage[nativeBalances];
// }

// rule should_pass_7 {
// 	env e;
// 	storage init = lastStorage;
// 	address x;
// 	butThenAlsoSend(e, x);
// 	assert init[totalTransferred] == lastStorage[totalTransferred];
// }

// rule should_pass_8(address a) {
// 	env e;
// 	storage init = lastStorage;
// 	t.butThenAlsoSend(e, a);
// 	t.incr(e);
// 	storage scenario1 = lastStorage;
// 	t.incr(e) at init;
// 	t.butThenAlsoSend(e, a);
// 	assert scenario1 == lastStorage;
// }

rule should_fail_1 {
	env e;
	storage init = lastStorage;
	incr(e);
	assert init[basic] == lastStorage[basic];
}


// rule should_fail_2 {
// 	env e;
// 	storage init = lastStorage;
// 	address x;
// 	butThenAlsoSend(e, x);
// 	assert init == lastStorage;
// }


// rule should_fail_3 {
// 	env e;
// 	storage init = lastStorage;
// 	incrStructField(e);
// 	assert init == lastStorage;
// }


// rule should_fail_4 {
// 	env e;
// 	storage init = lastStorage;
// 	incrNestedStructField(e);
// 	assert init == lastStorage;
// }


// rule should_fail_5 {
// 	env e;
// 	storage init = lastStorage;
// 	incrTightlyPackedStruct(e);
// 	assert init == lastStorage;
// }

// rule should_fail_6 {
// 	env e;
// 	env e2;
// 	address target;
// 	uint amount;

// 	storage init = lastStorage;
// 	transfer(e, e2.msg.sender, amount);
// 	transfer(e2, target, amount);
// 	storage s1 = lastStorage;
// 	transfer(e, target, amount) at init;
// 	assert s1 == lastStorage;
// }
