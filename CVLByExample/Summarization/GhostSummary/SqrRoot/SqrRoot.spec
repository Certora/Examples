methods {
    function sqrt(uint256 y) internal  returns (uint256) => floorSqrt(y);
}
// A precise summarization of sqrt
ghost floorSqrt(uint256) returns uint256 {    
                // sqrt(x)^2 <= x
    axiom forall uint256 x. floorSqrt(x)*floorSqrt(x) <= to_mathint(x) && 
                // sqrt(x+1)^2 > x 
                (floorSqrt(x) + 1)*(floorSqrt(x) + 1) > to_mathint(x);
}

rule addLiquidityMonotonicity(uint256 amount0, uint256 amount1, uint256 amount2, uint256 amount3) {
    env e;
    storage initStorage = lastStorage;
    uint256 firstAdd = addLiquidity(e, amount0, amount1);
    uint256 secondAdd = addLiquidity(e, amount2, amount3) at initStorage;
    assert ((amount0 <= amount2 || amount1 <= amount3) => 
            (firstAdd <= secondAdd), 
            "addLiquidity is not monotonic");
}
