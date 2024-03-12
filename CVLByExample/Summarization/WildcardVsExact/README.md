# What happens when a function has both exact and wildcard summarizations?

When a function matches a wildcard summarization but also has an exact summarization, the exact summarization will be used to summarize
this function. We will demonstrate such case using a simple example.

We have 2 very simple contracts: `A` (in `A.sol`) and `B` (in `B.sol`).
`A` holds a reference to `B` and has a simple function `callAFunc` that call the function `toBeSummarized` from B and returns it.
The function toBeSummarized just returns 0.

The spec `WildcardVsExact.spec` defines 2 different summarizations:
* A wildcard summarization that will match a `toBeSummarized()` signature from any contract in the scene. This summarization returns 5.
* An exact summarization to `B.toBeSummarized()` that returns 7.

The spec also include 2 simple rules: `isFive` and `isSeven` that asserts that `callAFunc` returns 5 and 7 respectively.

Run this spec via
```certoraRun runWildcardVsExact.conf```

[The report of this run](https://prover.certora.com/output/15800/cbdf895a0130407e9997def721834bc3?anonymousKey=ae82616d3ac4a4b608bd41d5c6d1a6b0e1bbe836)

As you can see `isFive` fails because the wildcard summarization was not used. But `isSeven` passes because the exact summarization was used
instead of calling the actual function that would have returned 0.
