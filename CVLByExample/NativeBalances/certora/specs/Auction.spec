/***
 * # Native balances Example
 *
 * This is an example specification for using nativeBalances.
 */

methods {
    function currentBid() external returns uint256 envfree; 
}

//// Basic rules ////////////////////////////////////////////////////

// This rule fails for Auction.sol because:
// 1. msg.value is passed to currentContract at the entrance to bid()
// 2. the sender changes to currentContract in internal bid() and all its balance is transferred so its balance does not increase.
// This rule passes for AuctionFixed.sol because only currentBid is transferred.
rule bidIncreasesAssets() {
    env e;
    require(e.msg.sender != currentContract);
    require(e.msg.value > currentBid() );
    uint256 balanceBefore = nativeBalances[currentContract];
    bid(e);
    assert nativeBalances[currentContract] > balanceBefore;
}

// This rule passes vacuously for Auction.sol because of the require e.msg.value > nativeBalances[currentContract] in the spec
// and require msg.value >= msg.value + nativeBalances[currentContract] in the code where nativeBalances[currentContract] > 0.
// It passes non-vacuously for AuctionFixed.sol because the amount transferred is currentBid for which msg.value >= currentBid
// can hold.
rule bidSuccessfullyExpectVacuous() {
    env e;
    uint256 balanceBefore = nativeBalances[currentContract];
    require(e.msg.sender != currentContract);
    require(e.msg.value > 0 &&  e.msg.value > balanceBefore);
    require (balanceBefore > 0);
    bid(e);
    assert nativeBalances[currentContract] >= balanceBefore;
}
