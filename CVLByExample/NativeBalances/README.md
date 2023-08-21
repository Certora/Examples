This directory demonstrates using nativeBalances.

## Incorrect Code
- The rule `bidIncreasesAssets` fails for Auction.sol because:
    - msg.value is passed to currentContract at the entrance to bid()
    - the sender changes to currentContract in internal bid() and all its balance is transferred so its balance does not increase.
- The rule bidSuccessfullyExpectVacuous passes vacuously because of the require e.msg.value > nativeBalances[currentContract] in the spec
  and require msg.value >= msg.value + nativeBalances[currentContract] in the code where nativeBalances[currentContract] > 0.

Run this configuration via:

```certoraRun certora/conf/runAuction.conf```

## Correct Code
- The rule passes for AuctionFixed.sol because  At the entrance to `bid` address(this).balance is already increased by msg.value,
so the balance of currentContract >= currentBid and therefore the transfer succeeds.
- The rule bidSuccessfullyExpectVacuous passes non-vacuously for AuctionFixed.sol because the amount transferred is currentBid for which   msg.value >= currentBid can hold.

Run this configuration via:

```certoraRun certora/conf/runAuctionFixed.conf```
