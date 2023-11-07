methods {
    function sqrt(uint256 y) internal  returns (uint256) => floorSqrt(y);
    // function sqrt(uint256 x) internal  returns (uint256) => floorSqrtSummarization(x);
}

ghost floorSqrt(uint256) returns uint256 {    
    axiom forall uint256 x. floorSqrt(x)*floorSqrt(x) <= to_mathint(x) && (floorSqrt(x) + 1)*(floorSqrt(x) + 1) > to_mathint(x);
}

// function floorSqrtSummarization(uint256 x) returns uint256 {
//     mathint SQRT;
//     require SQRT*SQRT <= to_mathint(x) && (SQRT + 1)*(SQRT + 1) > to_mathint(x);
//     return assert_uint256(SQRT);
// }

rule addLiquidityMonotonicity(uint256 amount0, uint256 amount1, uint256 amount2, uint256 amount3) {
    env e;
    storage initStorage = lastStorage;
    uint256 firstAdd = addLiquidity(e, amount0, amount1);
    uint256 secondAdd = addLiquidity(e, amount2, amount3) at initStorage;
    assert ((amount0 <= amount2 || amount1 <= amount3) => 
            (firstAdd <= secondAdd), 
            "addLiquidity is not monotonic");
}

// Weak monotonicity
// rule sqrtRule1(uint256 x, uint256 y) {
//     assert x > y => sqrt(x) >= sqrt(y);
// }

// // sqrt(4*x) = 2*sqrt(x) > sqrt(x)
// rule sqrtRule2(uint256 x) {
//     assert (x != 0 && 4*x <= max_uint) => floorSqrtexternal(to_uint256(4*x)) > floorSqrtexternal(x);
// }

// // squre of sqrt is identity (fails)
// rule sqrtRule3(uint256 x){
//     assert sqrt(x)*sqrt(x) == to_mathint(x);
// }

// // Multiplicative (fails)
// rule sqrtRule4(uint256 x, uint256 y){
//     require x*y <= max_uint;
//     assert floorSqrtexternal(x)*floorSqrtexternal(y) == floorSqrtexternal(to_uint256(x*y));
// }

// // sqrt of squre is identity (verified)
// rule sqrtRule5(uint256 x, uint256 x2){
//     require x*x == x2;
//     assert floorSqrtexternal(x2) == x && floorSqrtexternal(x2)*floorSqrtexternal(x2) == x2;
// }

// // sqrt(x) < x
// rule sqrtRule6(uint256 x)
// {
//     assert x>1 => floorSqrtexternal(x) < x;
// }
// */

// rule floorBug(uint256 x)  {
//     uint256 res = sqrt(x);
//     uint256 nextPower = (res + 1)*(res + 1);
//     assert res*res <= x && nextPower > x;
// }

// rule floor(uint256 x)  {
//     uint256 res = sqrt(x);
//     assert res*res <= x && (res + 1)*(res + 1) > x;
// }

