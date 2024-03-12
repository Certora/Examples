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
ghost mathint sumOfBalances_init {
    init_state axiom sumOfBalances_init == 0;
}

ghost mapping(address => bool) didAccessAccount;

function SumTrackingSetup() {
    require sumOfBalances == sumOfBalances_init;
    require forall address account. !didAccessAccount[account];
}

/*
For every storage load of the balance for some account, for the first time, 
we deduct the storage amount from the initial value and require that the result is non-negative. 

Example:
Suppose that at first the initial sum of balances that are going to be accessed in the flow is x.
sumOfBalances_init = x.
The function flow is going to access:
    _balances[0x1] = 1
    _balances[0x2] = 2
    _balances[0x3] = 3

x(0) = x
At first access [0x1]:    
    x(1) -> x(0) - 1 = x - 1 ; require x - 1 >=0
At second access [0x2]:    
    x(2) -> x(1) - 2 = x - 3 ; require x - 3 >=0
At third access [0x3]:
    x(3) -> x(2) - 3 = x - 6 ; require x - 6 >=0

The result is that x = sumOfBalances_init >= 6 = 1 + 2 + 3, as expected.
*/
hook Sload uint256 _balance _balances[KEY address account] {
    if(!didAccessAccount[account]) {
        didAccessAccount[account] = true;
        sumOfBalances_init = sumOfBalances_init - _balance;
        require sumOfBalances_init >= 0;
    }
}

hook Sstore _balances[KEY address account] uint256 _balance (uint256 _balance_old) {
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