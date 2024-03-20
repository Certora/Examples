using ERC20 as token;
//using ERC20_bug as token;

methods {
    function token.balanceOf(address) external returns (uint256) envfree;
    function token.totalSupply() external returns (uint256) envfree;
    function token.transfer(address,uint256) external returns (bool);
}

/// True sum of balances.
ghost mathint sumOfBalances {
    init_state axiom sumOfBalances == 0;
}

/// The initial value is being updated as we access the acounts balances one-by-one.
/// Should only be used as an initial value, never post-action!
ghost mathint sumOfUnaccessedBalances {
    init_state axiom sumOfUnaccessedBalances == 0;
}

ghost mapping(address => bool) didAccessAccount;

function SumTrackingSetup() {
    require sumOfBalances == sumOfUnaccessedBalances;
    require forall address account. !didAccessAccount[account];
}

/*
For every storage load of the balance for some account, for the first time,
we deduct the storage amount from the sumOfUnaccessedBalance and require that the result is non-negative.

Example:
Suppose that at the beginning of a rule the sum of balances is x.
So initially sumOfBalances = sumOfUnaccessedBalances = x.
The function flow is going to access:
    _balances[0x1] = 1
    _balances[0x2] = 2
    _balances[0x3] = 3

At first access [0x1]:
    sumOfUnaccessedBalances = x - 1 ; require x - 1 >=0
At second access [0x2]:
    sumOfUnaccessedBalances = x - 3 ; require x - 3 >=0
At third access [0x3]:
    sumOfUnaccessedBalances = x - 6 ; require x - 6 >=0

The result is that x = 6 + sumOfUnaccessedBalances >= 6 = 1 + 2 + 3, as expected.
*/
hook Sload uint256 _balance _balances[KEY address account] {
    if(!didAccessAccount[account]) {
        didAccessAccount[account] = true;
        sumOfUnaccessedBalances = sumOfUnaccessedBalances - _balance;
        require sumOfUnaccessedBalances >= 0;
    }
}

hook Sstore _balances[KEY address account] uint256 _balance (uint256 _balance_old) {
    if(!didAccessAccount[account]) {
        didAccessAccount[account] = true;
        sumOfUnaccessedBalances = sumOfUnaccessedBalances - _balance_old;
        require sumOfUnaccessedBalances >= 0;
    }
    sumOfBalances = sumOfBalances + _balance - _balance_old;
}

invariant SumOfBalancesEqualsTotalSupply()
    sumOfBalances == to_mathint(token.totalSupply())
    {
        preserved {
            SumTrackingSetup();
        }
    }

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

rule TwoBalancesCannotExceedTotalSupply(address accountA, address accountB) {
    SumTrackingSetup();
    requireInvariant SumOfBalancesEqualsTotalSupply();
    uint256 balanceA = token.balanceOf(accountA);
    uint256 balanceB = token.balanceOf(accountB);

    assert accountA != accountB =>
        balanceA + balanceB <= to_mathint(token.totalSupply());
}
