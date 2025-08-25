methods {
    function checkHookPermission(uint160 flag) external returns (bool) envfree;
}

definition BEFORE_INITIALIZE_FLAG() returns uint160 = 2^13;
definition AFTER_INITIALIZE_FLAG() returns uint160 = 2^12;

definition BEFORE_ADD_LIQUIDITY_FLAG() returns uint160 = 2^11;
definition AFTER_ADD_LIQUIDITY_FLAG() returns uint160 = 2^10;

definition BEFORE_REMOVE_LIQUIDITY_FLAG() returns uint160 = 2^9;
definition AFTER_REMOVE_LIQUIDITY_FLAG() returns uint160 = 2^8;

definition BEFORE_SWAP_FLAG() returns uint160 = 2^7;
definition AFTER_SWAP_FLAG() returns uint160 = 2^6;

definition BEFORE_DONATE_FLAG() returns uint160 = 2^5;
definition AFTER_DONATE_FLAG() returns uint160 = 2^4;

definition BEFORE_SWAP_RETURNS_DELTA_FLAG() returns uint160 = 2^3;
definition AFTER_SWAP_RETURNS_DELTA_FLAG() returns uint160 = 2^2;
definition AFTER_ADD_LIQUIDITY_RETURNS_DELTA_FLAG() returns uint160 = 2^1;
definition AFTER_REMOVE_LIQUIDITY_RETURNS_DELTA_FLAG() returns uint160 = 2^0;


rule onlyCallableByPoolManager(method f)
filtered { f -> !f.isView }
{
    env e;
    calldataarg args;
    f@withrevert(e, args);

    assert !lastReverted => e.msg.sender == currentContract.poolManager, "Only callable by PoolManager";
}

rule hookFlagsSetForBeforeInitialize() {
    env e;
    calldataarg args;
    currentContract.beforeInitialize@withrevert(e, args);

    assert !lastReverted => currentContract.checkHookPermission(BEFORE_INITIALIZE_FLAG()), "beforeInitialize flag not set";
}

rule hookFlagsSetForAfterInitialize() {
    env e;
    calldataarg args;
    currentContract.afterInitialize@withrevert(e, args);

    assert !lastReverted => currentContract.checkHookPermission(AFTER_INITIALIZE_FLAG()), "afterInitialize flag not set";
}

rule hookFlagsSetForBeforeRemoveLiquidity() {
    env e;
    calldataarg args;
    currentContract.beforeRemoveLiquidity@withrevert(e, args);

    assert !lastReverted => currentContract.checkHookPermission(BEFORE_REMOVE_LIQUIDITY_FLAG()), "beforeRemoveLiquidity flag not set";
}

rule hookFlagsSetForAfterRemoveLiquidity() {
    env e;
    calldataarg args;
    currentContract.afterRemoveLiquidity@withrevert(e, args);

    assert !lastReverted => currentContract.checkHookPermission(AFTER_REMOVE_LIQUIDITY_FLAG()), "afterRemoveLiquidity flag not set";
}

rule hookFlagsSetForBeforeDonate() {
    env e;
    calldataarg args;
    currentContract.beforeDonate@withrevert(e, args);

    assert !lastReverted => currentContract.checkHookPermission(BEFORE_DONATE_FLAG()), "beforeDonate flag not set";
}

rule hookFlagsSetForAfterDonate() {
    env e;
    calldataarg args;
    currentContract.afterDonate@withrevert(e, args);

    assert !lastReverted => currentContract.checkHookPermission(AFTER_DONATE_FLAG()), "afterDonate flag not set";
}

rule hookFlagsSetForBeforeSwap() {
    env e;
    calldataarg args;
    currentContract.beforeSwap@withrevert(e, args);

    assert !lastReverted => currentContract.checkHookPermission(BEFORE_SWAP_FLAG()), "beforeSwap flag not set";
}

rule hookFlagsSetForAfterSwap() {
    env e;
    calldataarg args;
    currentContract.afterSwap@withrevert(e, args);

    assert !lastReverted => currentContract.checkHookPermission(AFTER_SWAP_FLAG()), "afterSwap flag not set";
}

rule swapOnlyCalledViaRouter() {
    env e;
    
    address sender;
    PointsHook.PoolKey key;
    PointsHook.SwapParams swapParams;
    //PointsHook.BalanceDelta delta;
    bytes data;
    currentContract.beforeSwap(e, sender, key, swapParams, data);

    assert e.msg.sender == currentContract.poolManager, "Only callable by PoolManager";
    //assert sender == currentContract.router, "Only callable by Router";
    //assert key == currentContract.poolKey, "Invalid PoolKey";
}


