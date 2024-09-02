hook Sstore currentContract.dontUseMe uint256 newVal (uint256 oldVal) {
    assert false, "the hook shouldn't be called";
}

rule resetZeroesAllFunds(address to,uint256 amount) {
	env e;
	require exists address a. currentContract.funds[a] > 0;
	reset_storage currentContract;
	assert forall address a. currentContract.funds[a] == 0, "all funds should be zero";
}