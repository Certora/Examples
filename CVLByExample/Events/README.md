# Reasoning about Events

This directory demonstrates how to reason about events with the Prover. 
The Prover cannot natively reason about the Events, therefore a workaround is needed.

The workaround is to wrap the `emits` of Solidity `events` into an internal function and then apply internal summarization to reason about the emitted event. 

- 
Run this configuration via:

```certoraRun runAuctionFixed.conf```

[A report of this run](https://prover.certora.com/output/53900/4ffdad0c20094a729d830bfb1b460f3e?anonymousKey=b345ea4d1fe4b3631442c0f110e926a58f47ee9b)


