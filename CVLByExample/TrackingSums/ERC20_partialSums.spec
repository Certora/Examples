using ERC20 as token;
//using ERC20_bug as token;

methods {
    function token.balanceOf(address) external returns (uint256) envfree;
    function token.totalSupply() external returns (uint256) envfree;
    function token.transfer(address,uint256) external returns (bool);
}

// Partial sum of balances.
//  sumOfBalances[x] = \sum_{i=0}^{x-1} balances[i];
ghost mapping(mathint => mathint) sumOfBalances {
    init_state axiom forall mathint addr. sumOfBalances[addr] == 0;
}

// ghost copy of balances
ghost mapping(address => uint256) ghost_balances {
    init_state axiom forall address addr. ghost_balances[addr] == 0;
}

hook Sload uint256 _balance _balances[KEY address account] {
    require ghost_balances[account] == _balance;
}

hook Sstore _balances[KEY address account] uint256 _balance (uint256 _balance_old) {
    // update partial sums for x > to_mathint(account)
    havoc sumOfBalances assuming
        forall mathint x. sumOfBalances@new[x] ==
            sumOfBalances@old[x] + (to_mathint(account) < x ? _balance - _balance_old : 0);
    ghost_balances[account] = _balance;
}

invariant sumOfBalancesStartsAtZero()
    sumOfBalances[0] == 0;
invariant sumOfBalancesGrowsCorrectly()
    forall address addr. sumOfBalances[to_mathint(addr) + 1] ==
        sumOfBalances[to_mathint(addr)] + ghost_balances[addr];

invariant sumOfBalancesMonotone()
    forall mathint i. forall mathint j. i <= j => sumOfBalances[i] <= sumOfBalances[j]
    {
        preserved {
            requireInvariant sumOfBalancesStartsAtZero();
            requireInvariant sumOfBalancesGrowsCorrectly();
        }
    }

invariant sumOfBalancesEqualsTotalSupply()
    sumOfBalances[2^160] == to_mathint(token.totalSupply())
    {
        preserved {
            requireInvariant sumOfBalancesStartsAtZero();
            requireInvariant sumOfBalancesGrowsCorrectly();
            requireInvariant sumOfBalancesMonotone();
        }
    }

rule twoBalancesCannotExceedTotalSupply(address accountA, address accountB) {
    requireInvariant sumOfBalancesStartsAtZero();
    requireInvariant sumOfBalancesGrowsCorrectly();
    requireInvariant sumOfBalancesMonotone();
    requireInvariant sumOfBalancesEqualsTotalSupply();
    uint256 balanceA = token.balanceOf(accountA);
    uint256 balanceB = token.balanceOf(accountB);

    assert accountA != accountB =>
        balanceA + balanceB <= to_mathint(token.totalSupply());
    satisfy(accountA != accountB && balanceA > 0 && balanceB > 0);
}


rule threeBalancesCannotExceedTotalSupply(address accountA, address accountB, address accountC) {
    requireInvariant sumOfBalancesStartsAtZero();
    requireInvariant sumOfBalancesGrowsCorrectly();
    requireInvariant sumOfBalancesMonotone();
    requireInvariant sumOfBalancesEqualsTotalSupply();
    uint256 balanceA = token.balanceOf(accountA);
    uint256 balanceB = token.balanceOf(accountB);
    uint256 balanceC = token.balanceOf(accountC);

    assert accountA != accountB && accountA != accountC && accountB != accountC =>
        balanceA + balanceB + balanceC <= to_mathint(token.totalSupply());
    satisfy(accountA != accountB && balanceA + balanceB + balanceC > to_mathint(token.totalSupply()));
}
