# Summarization for Multi Contracts with Side Effects

## NoSummary.spec

In this spec the functions are not summarized.

To run this spec with no link run

```certoraRun certora/conf/runNoSummaryNoLink.conf```

[The report of this run](https://prover.certora.com/output/1902/650934d2c0fb4948b23cb25d650113e3?anonymousKey=8b21114d72c5640425c2f9a840d90403986133a0)

The rule `checkNoSummarization` fails because without linking the results of the functions are havoced.

To run this spec with linking run

```certoraRun certora/conf/runNoSummaryWithLink.conf```

[The report of this run](https://prover.certora.com/output/1902/754827d15dc74296b23cfeef776afec1?anonymousKey=a1fee8dcacb680b1b611091859d2bc6c84a1717e)

## WithDispatcher.spec
This spec contains DISPATCHER summarizations for a multi-contract setting. The summarized function x() appears in both contracts while the function dummyB appears only in CalleeB. The spec is run with two configurations: one with linking and one without.

To run this spec with no link run
```certoraRun certora/conf/runWithDispatcherNoLink.conf```

[The report of this run](https://prover.certora.com/output/1902/cf603b6a3c0f4162acc1e6a6e57bb207?anonymousKey=75e730230d8ca3d0374aa3470465d2efc357fd3a)

The rule `checkDispatcherUnresolvedSummarizationResult` fails because the used field `x` appears in both contracts and the absence of a link causes switching the called contracts.

The rule `checkDispatcherUniqueSummarizationResult` passes despite the absence of a link because the summarized function `dummyB()` appears only in CalleeB so the dispatcher finds the right function.

To run this spec with a link run
```certoraRun certora/conf/runWithDispatcherWithLink.conf```

[The report of this run](https://prover.certora.com/output/1902/d01190ff1ba546d98af5f2871c72a616?anonymousKey=731c6d29155e769c36a89e5b4e7b6ac23a617f5b)

All rules pass.