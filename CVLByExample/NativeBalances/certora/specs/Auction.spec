/***
 * # Native balances Example
 *
 * This is an example specification for using nativeBalances.
 */

methods {
    function currentBid() external returns uint256 envfree; 
}

//// Basic rules ////////////////////////////////////////////////////


rule bidIncreasesAssets() {
    env e;
    require(e.msg.sender != currentContract);
    require(e.msg.value > currentBid() );
    uint256 balanceBefore = nativeBalances[currentContract];
    bid(e);
    assert nativeBalances[currentContract] > balanceBefore;
}


rule bidSuccessfullyExpectVacuous() {

    env e;
    uint256 balanceBefore = nativeBalances[currentContract];
    require(e.msg.sender != currentContract);
    require(e.msg.value > 0 &&  e.msg.value > balanceBefore);
    require (balanceBefore > 0);
    bid(e);
    assert nativeBalances[currentContract] > balanceBefore;
}
