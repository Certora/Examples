import "PoolManagerSummaries.spec";

using PointsToken as token;

methods {
    function PointsHookHarness.checkHookAddress() external returns (bool) envfree;
    function PointsToken.totalSupply() external returns (uint256) envfree;
}

rule mintingMatchesOnSwap() {
    mathint tokenBalancePre = poolToken0Balance;
    mathint pointsTotalSupplyPre = token.totalSupply();
    env e;
    PoolManager.PoolKey key;
    PoolManager.SwapParams params;
    bytes hookData;

    require currentContract.checkHookAddress(), "PointsHook correctly deployed";
    require e.msg.sender != currentContract, "PointsHook will never initiate a swap";
    require key.currency0 == 0, "Pool must use ether";
    require key.hooks == currentContract, "PointsHook must be set in pool";
    require params.zeroForOne, "swap must sell ether for token";

    poolManager.swap(e, key, params, hookData);
    
    mathint tokenBalancePost = poolToken0Balance;
    mathint pointsTotalSupplyPost = token.totalSupply();

    assert tokenBalancePost - tokenBalancePre ==
        pointsTotalSupplyPost - pointsTotalSupplyPre, "minting matches";
}

rule mintingMatchesOnAddLiquidity() {
    mathint tokenBalancePre = poolToken0Balance;
    mathint pointsTotalSupplyPre = token.totalSupply();
    env e;
    PoolManager.PoolKey key;
    PoolManager.ModifyLiquidityParams params;
    bytes hookData;
    
    require currentContract.checkHookAddress(), "PointsHook correctly deployed";
    require e.msg.sender != currentContract, "PointsHook will never add liquidity";
    require key.currency0 == 0, "Pool must use ether";
    require key.hooks == currentContract, "PointsHook must be set in pool";
    require params.liquidityDelta > 0, "Must add liquidity";

    poolManager.modifyLiquidity(e, key, params, hookData);

    mathint tokenBalancePost = poolToken0Balance;
    mathint pointsTotalSupplyPost = token.totalSupply();

    if (tokenBalancePost < tokenBalancePre) {
        assert pointsTotalSupplyPost == pointsTotalSupplyPre, "no mint if only fees were redeposited";
    } else {
        assert tokenBalancePost - tokenBalancePre ==
            pointsTotalSupplyPost - pointsTotalSupplyPre, "minting matches";
    }
}
