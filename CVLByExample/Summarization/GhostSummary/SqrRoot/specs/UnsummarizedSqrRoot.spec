rule addLiquidityMonotonicity(uint256 amount0, uint256 amount1, uint256 amount2, uint256 amount3) {
    env e;
    storage initStorage = lastStorage;
    uint256 firstAdd = addLiquidity(e, amount0, amount1);
    uint256 secondAdd = addLiquidity(e, amount2, amount3) at initStorage;
    assert ((amount0 <= amount2 || amount1 <= amount3) => 
            (firstAdd <= secondAdd), 
            "addLiquidity is not monotonic");
}
