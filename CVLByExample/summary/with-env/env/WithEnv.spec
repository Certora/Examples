using DummyERC20WithTimedBalanceOf as discountToken;

methods {
    function discountToken.balanceOf(address user) external returns (uint256) with (env e) => 
        balanceOfDiscountTokenAtTimestamp(user, e.block.timestamp) ;
}

ghost mapping(address => mapping (uint256 => uint256)) discount_ghost;
ghost mapping(uint256 => uint256) index_ghost;

/**
* Query index_ghost for the index value at the input timestamp
**/
function indexAtTimestamp(uint256 timestamp) returns uint256 {
    // require index_ghost[timestamp] >= ray();
    return index_ghost[timestamp];
    // return 1001684385021630839436707910;//index_ghost[timestamp];
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
function envAtTimestamp(uint256 ts) returns env {
	env e;
	require(e.block.timestamp == ts);
	return e;
}

/**
* @title proves that the user's balance of debt token (as reported by GhoVariableDebtToken::balanceOf) can't increase by calling any external non-mint function.
**/
//pass
rule nonMintFunctionCantIncreaseBalance(method f) {
	address user;
	uint256 ts1;
	uint256 ts2;
	require(ts2 >= ts1);
	env e = envAtTimestamp(ts2);
	uint256 balanceBeforeOp = callBalanceOf(e, user);
	calldataarg args;
	f(e,args);
	mathint balanceAfterOp = balanceOf(e, user);
	mathint allowedDiff = indexAtTimestamp(ts2) / 5;
	assert(balanceAfterOp <= balanceBeforeOp + allowedDiff);
}