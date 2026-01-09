
using DamnValuableToken as token;

methods{
    function token.totalSupply() external returns (uint256) envfree;
    function token.allowance(address, address) external returns (uint256) envfree;

    unresolved external in TrusterLenderPool.flashLoan(uint256,address,address,bytes) => DISPATCH(use_fallback=true) [
        token.approve(address, uint256),
        currentContract._
    ] default NONDET;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Pool Allowance Always Zero                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/

invariant poolAllowanceAlwaysZero(address user)
    token.allowance(currentContract, user) == 0
    {
        preserved constructor() {
            require token.allowance(currentContract, user) == 0, "the token should not have an allowance yet for a contract that is being constructed";
        }
        preserved with (env e)
        {
            require e.msg.sender != currentContract;
        } 
    }