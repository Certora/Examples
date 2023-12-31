# nativeBalances

This directory demonstrates how to use nativeBalances.

## Incorrect Code
- The rule `bidIncreasesAssets` fails for `Auction.sol` because:
    - `msg.value` is passed to `currentContract` at the entrance to `bid()`
    - the sender changes to `currentContract` in internal `bid()` and all its balance is transferred so it does not increase.
- The rule `bidSuccessfullyExpectVacuous` passes vacuously because of the 
  `require e.msg.value > nativeBalances[currentContract]` in the spec
  and `require msg.value >= msg.value + nativeBalances[currentContract]` in the code where 
  `nativeBalances[currentContract] > 0`.

Run this configuration via:

```certoraRun runAuction.conf```

[A report of this run](https://prover.certora.com/output/15800/7566d29557fc49bb8fbc88fb63364dc5?anonymousKey=7140792242c73d6646692e34deaecbf02cc82b1b)

## Correct Code
- The rule passes for `AuctionFixed.sol` because at the entrance to `bid` `address(this).balance` is already increased by `msg.value`,
so the balance of `currentContract >= currentBid` and therefore the transfer succeeds.
- The rule `bidSuccessfullyExpectVacuous` passes non-vacuously for `AuctionFixed.sol` because the amount transferred is `currentBid` for which `msg.value >= currentBid` can hold.

Run this configuration via:

```certoraRun runAuctionFixed.conf```

[A report of this run](https://prover.certora.com/output/15800/5dbc1a9e4f6949cea9871038e82097e9?anonymousKey=8d552772ee1a1a78b49b90d4558b0bb3444d4f73)

