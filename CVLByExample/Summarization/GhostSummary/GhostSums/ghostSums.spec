ghost mapping(address => uint256) balances;

hook Sstore currentContract.balances[KEY address a] uint256 newVal {
    balances[a] = newVal;
}

hook Sload uint256 val currentContract.balances[KEY address a]  {
    require balances[a] == val;
}

rule totalSupplyIsSumOfBalances(env e, method f, calldataarg args) {
    require currentContract.totalSupply == (sum address a. balances[a]);
    f(e, args);
    assert currentContract.totalSupply == (sum address a. balances[a]);
}
