# Ghost Summary

This directory demonstrates summarizing functions by ghosts.
The `continuous_interest` function includes arithmetic which, depending on the rule, might be complicated for the Prover to reason about.

The Certora Prover uses "over-approximations" of the arithmetic operations in the resulting formula. This means that we allow behaviors that include the behavior of the function, and also additional behaviors. In other words, this means that a counterexample may not be a feasible scenario (i.e. not actually a feasible program behavior).

## NotSummarized.spec

With the specification `NotSummarized.spec` the tool reports a wrong violation of the rule `yield_monotonic`. This is a case where function summarization becomes useful since we get to decide how we would like to over-approximate our function. 

This spec is run via
```certoraRun.py runInterestNotSummarized.conf```

[A report of this run](https://prover.certora.com/output/15800/3f444ff61b44410fa355bb4b912e2e2a?anonymousKey=d30bfc5a406a9916030804fa01c97c783ef89a6f)

## WithGhostSummary.spec

In the spec `WithGhostSummary.spec` the function `continuous_interest` is replaced by the ghost `ghost_interest` that includes an axiom that assures monotonicity.
With this specification, the rule passes.

This version is run via
```certoraRun.py runInterest.conf```

[A report of this run](https://prover.certora.com/output/15800/543decec519a4d6fb56e815b7c6601e5?anonymousKey=8bb2639f3152586c84e5a4fa8999c50fdbb2f0b2)