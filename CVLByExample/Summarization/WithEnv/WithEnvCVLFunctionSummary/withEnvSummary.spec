/**
  An example for using a summary with `with env`.
*/

methods {
  // Summarization by a CVL function. The result is non-deterministic because the CVL function is not deterministic.
  function reduceBalance(uint256 amount) internal returns (uint256) with (env e) => cvlReduceBalance(e, amount);
}

// CVL function used for summarization. 
function cvlReduceBalance(env e, uint256 amount) returns uint256  {
	uint256 poolBalance = getBalance(e, currentContract);
	require (poolBalance != 0);
	require (amount != 0);
	uint256 amountOut = decr(e);
	return amountOut;
}

// A rule that demonstrates the use of the summarization.
rule checkReduceBalance() {
	env e;
	uint256 amountBefore = getBalance(e, e.msg.sender);
	uint256 amount;
	callReduceBalance(e, amount);
	assert (getBalance(e, e.msg.sender) == assert_uint256(amountBefore - 1), "Withdraw failed");
}


