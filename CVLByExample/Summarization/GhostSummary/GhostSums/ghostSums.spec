ghost mapping(address => uint256) mirrorBalances {
    init_state axiom (sum address a. mirrorBalances[a]) == 0;
}

hook Sstore currentContract.balances[KEY address a] uint256 newVal {
    mirrorBalances[a] = newVal;
}

hook Sload uint256 val currentContract.balances[KEY address a] {
    require mirrorBalances[a] == val;
}

invariant totalSupplyIsSumOfBalances()
    currentContract.totalSupply == (sum address a. mirrorBalances[a]) ;