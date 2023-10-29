/**
	Example for ghost summary using `with env`.
*/


methods {
	// Summarization by a ghost.
	// This summarization makes the result of balanceOf deterministic. For the same user and timestamp
	// balanceOf is the same.
	function balanceOf(address user) internal returns (uint256) with (env e) => 
		discount_ghost[user][e.block.timestamp];
}

ghost mapping(address => mapping (uint256 => uint256)) discount_ghost;
ghost mapping(uint256 => uint256) index_ghost;

/**
* Query index_ghost for the index value at the input timestamp
**/
function indexAtTimestamp(uint256 timestamp) returns uint256 {
    return index_ghost[timestamp];
}

/**
* Query discount_ghost for the [user]'s balance of discount token at [timestamp]
**/
function balanceOfDiscountTokenAtTimestamp(address user, uint256 timestamp) returns uint256 {
	return discount_ghost[user][timestamp];
}

/**
* Returns an env instance with [ts] as the block timestamp
**/
// function envAtTimestamp(uint256 ts) returns env {
// 	env e;
// 	require(e.block.timestamp == ts);
// 	return e;
// }

/**
* @title proves that the user's balance of debt token (as reported by GhoVariableDebtToken::balanceOf) can't increase by calling any external non-mint function.
**/
rule nonMintFunctionCantIncreaseBalance(method f) {
	address user;
	uint256 ts1;
	uint256 ts2;
	env e;
	require(e.block.timestamp == ts2);
	require(ts2 >= ts1);
	uint256 balanceBeforeOp = callBalanceOf(e, user);
	calldataarg args;
	f(e,args);
	mathint balanceAfterOp = balanceOf(e, user);
	mathint allowedDiff = indexAtTimestamp(ts2) / 5;
	assert(balanceAfterOp <= balanceBeforeOp + allowedDiff);
}

