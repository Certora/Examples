using DamnValuableToken as token;

methods {
    function token.totalSupply() external returns (uint256) envfree;
    function token.allowance(address, address) external returns (uint256) envfree;
    unresolved external in TrusterLenderPool.flashLoan => DISPATCH(use_fallback)[token.approve(address, uint256)(address, uint256), currentContract._()] default NONDET;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Pool Allowance Always Zero                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
invariant poolAllowanceAlwaysZero(address user) token.allowance(currentContract, user) == 0 {
    preserved with (env e) {
        require e.msg.sender != currentContract;
 }