using ERC20 as token;

methods {
    function token.balanceOf(address) external returns (uint256) envfree;
    function token.totalSupply() external returns (uint256) envfree;
    function token.transfer(address,uint256) external returns (bool); 
}

ghost mathint sumOfBalances {
    init_state axiom sumOfBalances == 0;
}

/*
hook Sload uint256 _balance _balances[KEY address account] {
    require sumOfBalances >= to_mathint(_balance);
}
*/

hook Sstore _balances[KEY address account] uint256 _balance (uint256 _balance_old) {
    sumOfBalances = sumOfBalances + _balance - _balance_old;
}

invariant SumOfBalancesEqualsTotalSupply()
    sumOfBalances == to_mathint(token.totalSupply());

rule transferPreservesSumOfBalances(address to, uint256 amount) {
    env e;
    address from = e.msg.sender; 
    uint256 balanceFrom_before = token.balanceOf(from);
    uint256 balanceTo_before = token.balanceOf(to);
    /// We must explictly require the sum of balances to be capped by max(uint256)
    require balanceFrom_before + balanceTo_before <= max_uint256;
        token.transfer(e, to, amount);
    uint256 balanceFrom_after = token.balanceOf(from);
    uint256 balanceTo_after = token.balanceOf(to);

    assert balanceTo_after + balanceFrom_after == balanceTo_before + balanceFrom_before;
}

rule twoBalancesCannotExceedTotalSupply(address accountA, address accountB) {
    requireInvariant SumOfBalancesEqualsTotalSupply();
    uint256 balanceA = token.balanceOf(accountA);
    uint256 balanceB = token.balanceOf(accountB);

    assert accountA != accountB =>
        balanceA + balanceB <= to_mathint(token.totalSupply());
}