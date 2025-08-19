import "extsload.spec";

using PoolManagerHarness as poolManager;

methods {
    function _.beforeAddLiquidity(address, PoolManagerHarness.PoolKey, PoolManagerHarness.ModifyLiquidityParams, bytes) external => DISPATCHER(true);
    function _.beforeRemoveLiquidity(address, PoolManagerHarness.PoolKey, PoolManagerHarness.ModifyLiquidityParams, bytes) external => DISPATCHER(true);
    function _.beforeSwap(address, PoolManagerHarness.PoolKey, PoolManagerHarness.SwapParams, bytes) external => DISPATCHER(true);
    function _.afterAddLiquidity(address, PoolManagerHarness.PoolKey, PoolManagerHarness.ModifyLiquidityParams, PoolManagerHarness.BalanceDelta, PoolManagerHarness.BalanceDelta, bytes) external => DISPATCHER(true);
    function _.afterRemoveLiquidity(address, PoolManagerHarness.PoolKey, PoolManagerHarness.ModifyLiquidityParams, PoolManagerHarness.BalanceDelta, PoolManagerHarness.BalanceDelta, bytes) external => DISPATCHER(true);
    function _.afterSwap(address, PoolManagerHarness.PoolKey, PoolManagerHarness.SwapParams, PoolManagerHarness.BalanceDelta, bytes) external => DISPATCHER(true);
    function _.beforeInitialize(address, PoolManagerHarness.PoolKey, uint160) external => DISPATCHER(true);
    function _.afterInitialize(address, PoolManagerHarness.PoolKey, uint160, int24) external => DISPATCHER(true);

    function PoolManager._swap(Pool.State storage, PoolManager.PoolId id, Pool.SwapParams memory swapParams, Pool.Currency inputCurrency) internal returns (PoolManager.BalanceDelta) => swapSummary(id, swapParams, inputCurrency);
    function Pool.modifyLiquidity(Pool.State storage, Pool.ModifyLiquidityParams memory liquidityParams) internal returns (PoolManager.BalanceDelta, PoolManager.BalanceDelta) => modifyLiquiditySummary(liquidityParams);
    function Pool.initialize(Pool.State storage, uint160 sqrtPrice, uint24 lpFee) internal returns (int24) => initializeSummary(sqrtPrice, lpFee);

    function PoolManagerHarness.computeBalanceDelta(int128 _amount0, int128 _amount1) external returns (PoolManager.BalanceDelta) envfree;
    function PoolManagerHarness.getDelta(PoolManagerHarness.Currency currency, address account) external returns (int256) envfree;
}

// These ghost variables track the number of tokens that were put into the pool.  
// Token0/Token1 are the two tokens that the pool swaps between.
ghost mathint poolToken0Balance;
ghost mathint poolToken1Balance;

// This summary simulates the _swap function of the Uniswap PoolManager.  Instead of
// having the exact computation that Uniswap would be doing, we do an overabstraction:
// we allow more behavior that Uniswap would not allow, but these behaviors are still
// fine to ensure our property.  We do this by non-deterministically generating the 
// amounts (by not initializing the local variables).
function swapSummary(PoolManager.PoolId id, Pool.SwapParams swapParams, Pool.Currency inputCurrency) returns PoolManager.BalanceDelta {
    // uninitialized amounts -> prover tries every possible swap
    int128 amount0Delta;
    int128 amount1Delta;

    // but we require some restrictions, so that trade corresponds to swapParams
    if (swapParams.zeroForOne) {
        // user should pay token0 (negative) and receive token1 (positive)
        require amount0Delta <= 0 && amount1Delta >= 0, "swap token0 for token1";

        // check that we did not overshoot the specified amount
        if (swapParams.amountSpecified > 0) {
            require amount1Delta <= swapParams.amountSpecified, "swap at most amount specified";
        } else {
            require amount0Delta >= swapParams.amountSpecified, "swap at most amount specified";
        }
    } else {
        // user should pay token1 (negative) and receive token0 (positive)
        require amount0Delta >= 0 && amount1Delta <= 0, "swap token1 for token0";

        // check that we did not overshoot the specified amount
        if (swapParams.amountSpecified > 0) {
            require amount0Delta <= swapParams.amountSpecified, "swap at most amount specified";
        } else {
            require amount1Delta >= swapParams.amountSpecified, "swap at most amount specified";
        }
    }

    // update the pool balances.
    // The pool receives what the user pays, so we subtract the amounts.
    poolToken0Balance = poolToken0Balance - amount0Delta;
    poolToken1Balance = poolToken1Balance - amount1Delta;

    // Check that the pool had enough tokens for the trade
    require poolToken0Balance >= 0 && poolToken1Balance >= 0, "swap ensures that token balance cannot be negative";  

    // Return the amounts
    return poolManager.computeBalanceDelta(amount0Delta, amount1Delta);
}

 // This summary simulates the modifyLiquidity function of the Uniswap Pool.  Again,
 // we do an overabstraction and allow more behavior that Uniswap would not allow.
 // In this case we non-deterministically choose the number of tokens to pay to match the
 // liquidity and the amount of fees that the user already earned for his position.
 function modifyLiquiditySummary(Pool.ModifyLiquidityParams liquidityParams) returns (PoolManager.BalanceDelta, PoolManager.BalanceDelta) {
    Pool.BalanceDelta liqDelta;
    Pool.BalanceDelta feeDelta;
    int128 liqDelta0;
    int128 liqDelta1;
    int128 feeDelta0;
    int128 feeDelta1;

    // The user only receives fees, so feeDelta is always non-negative.
    require feeDelta0 >=0 && feeDelta1 >= 0, "fee deltas must be non-negative";

    // Check that the sign of liqDelta is the opposite of the sign of liquidityDelta: if the
    // user puts in liquidity (positive), he should pay for liquidity in liqDelta (negative).
    if (liquidityParams.liquidityDelta > 0) {
        require liqDelta0 <= 0 && liqDelta1 <= 0, "liquidity deltas must be non-positive";
    } else if (liquidityParams.liquidityDelta == 0) {
        require liqDelta0 == 0 && liqDelta1 == 0, "currencyDelta sign must match liquidityDelta sign";
    } else {
        require liqDelta0 >= 0 && liqDelta1 >= 0, "liquidity deltas must be non-negative";
    }

    // update the pool balance, again the sign is flipped because we switch to the perspective
    // of the pool.
    poolToken0Balance = poolToken0Balance - liqDelta0 - feeDelta0;
    poolToken1Balance = poolToken1Balance - liqDelta1 - feeDelta1;
    
    // There should be some tokens left in the pool, or uniswap is seriously broken.
    // Note that we don't verify uniswap here, but we assume that uniswap works.
    require poolToken0Balance >= 0 && poolToken1Balance >= 0, "uniswap is always solvent";

    // Return the balance deltas.
    liqDelta = poolManager.computeBalanceDelta(liqDelta0, liqDelta1);
    feeDelta = poolManager.computeBalanceDelta(feeDelta0, feeDelta1);
    return (liqDelta, feeDelta);
}


function initializeSummary(uint160 price, uint24 fee) returns int24 {
    int24 tick;
    require price > 0, "price must be positive";
    return tick; // nondeterministic tick
}
