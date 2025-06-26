# Reasoning about Solidity events

This directory demonstrates how to reason about Solidity events with the Prover. 
The Prover cannot natively reason about events, therefore a workaround is needed.

The workaround is to wrap the `emits` of Solidity `events` into an internal function and then apply internal summarization to reason about the emitted event. 

See `contracts/Auction.sol` for the original code that uses an event and take a look at `contract/AuctionFixed.sol` for code that uses the workaround.

- 
Run this configuration via:

```certoraRun runAuctionFixed.conf```

[A report of this run](https://prover.certora.com/output/53900/4ffdad0c20094a729d830bfb1b460f3e?anonymousKey=b345ea4d1fe4b3631442c0f110e926a58f47ee9b)


