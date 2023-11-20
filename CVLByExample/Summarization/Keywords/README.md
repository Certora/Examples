# Summarization Keywords
This directory contains examples for [Summarization](https://github.com/Certora/Documentation/blob/master/docs/cvl/methods.md)
The interface `IntGetter` has the functions `get1()`, `get2()`, `set1()` and `set2()`. Contract `IntGetterImpl` is an implementation of this interface.

 
The specs Always, AlwaysVsContant and ConstantvsNondet are regardless of the implementation of IntGetter.
Notice that in a summarization of an unknown contract, a wildcard entry is used in the methods block.
```
methods {
  function _.get1() external =>  ...
}
```

## Always.spec
Here the function `get1` is summarized by `ALWAYS(7)` while `get2` is not summarized.
Therefore, the rule `isG1Always7` is verified, as `g1` can be only 7.
However, `isG2Always7` is violated as `g2` can be any value. As default, the prover takes into account that any value is a possible one.

Run via ```certoraRun certora/conf/runAlways.conf```
[A report of this run](https://prover.certora.com/output/1902/31dbb3850048402cb5567095939c7584?anonymousKey=4cfea6c137777248bb60ec4ea6fe112832eb0b5a)

## AlwaysVsConstant.spec

Here the function `get1` is summarized by `ALWAYS(7)` while `get2` is summarized by `CONSTANT`.
This means that all calls to `get2` always return the same result but it can be other than `7`.
Therefore, the rule `constantCanbeAnyValue` demonstrates that the `g2` can be to 7, while the rule `constantVsAlways` is violated as `get1` can be different than `get2`.

Rule `constantDoesNotChange` checks whether `get2` is that value before each function. Notice that this rule is successfully verified on all functions, including `set2` demonstrating that contast summarization implies the same value even on state-changing functions. 

Run via ```certoraRun certora/conf/runAlwaysVsConstant.conf```
[A report of this run](https://prover.certora.com/output/1902/bda3b5a430e946dcb5fc20091d61ed41?anonymousKey=9df3fb1680b76a3c5ed74a72f66261a4acd56a0e)

## ConstantVSNondet.spec

Here the function `get1` is summarized by `CONTANT` while `get2` is summarized by `NONDET`.
This means that all calls to `get1` always return the same result and therefore the rule `checkConstantSummary` is verified.
Since `get2` is summarized with `NONDET` two calls to `get2` can have different results and therefore the
rule `checkNondetSummary` fails.

Run via ```certoraRun certora/conf/runConstantVsNondet.conf```

[A report of this run](https://prover.certora.com/output/1902/12e0683824854ec583afe14a4a6ed7f4?anonymousKey=9c0fb7a3af23fe157e89ec8c82c1ca8433ad25ce)


## NondetVsHavoc.spec

Here we add two implementations of `IntGetter` to the list of contracts, and demonstrate the use of NONDET to indicate that no state has changed. Rule `checkChangeGi` indicates which function call can change `gi`.
Due to the nondet summarization of `get1` the rule is verified for `setToG1`. However it shows a case of change to both `get1` and `get2` on a call to `setToG2`, this is due to the havoc that assumes any slot can change. 

[A report of this run](https://prover.certora.com/output/1902/e01ddd0825fc48a2bf66d390ba8697c6?anonymousKey=8069b0007ad59f722b99f9cd732269f38c7a0593)

## NoSummary.spec

In this spec the functions are not summarized.

To run this spec with no link run

```certoraRun certora/conf/runNoSummaryNoLink.conf```

[The report of this run](https://prover.certora.com/output/1902/dd77ab85b440476cb6e327e20a696e49?anonymousKey=31df6e044f36de1fed0e98fd853eb3e78b6eb18b)

The rule `checkNoSummarization` fails because without linking the results of the functions are havoced.

To run this spec with linking run

```certoraRun certora/conf/runNoSummaryWithLink.conf```

[The report of this run](https://prover.certora.com/output/1902/ad7c77200ba54ea68dd779b731a43422?anonymousKey=db597db36523fdeb38f65a99987d037d50bbf0c9)

## WithDispatcher.spec

This spec contains DISPATCHER summarizations for a multi-contract setting. The summarized function `x()` appears in both contracts while the function `dummyB` appears only in `AnotherIntGetterImpl`. The spec is run with two configurations: one with linking and one without.

To run this spec with no link run
```certoraRun certora/conf/runWithDispatcherNoLink.conf```

[The report of this run](https://prover.certora.com/output/1902/a468e34ad5264f2d820de62d9f0d2790?anonymousKey=95030748f842c167b93f4389cf2a7eee51f437ee)

The rule `checkDispatcherUnresolvedSummarizationResult` fails because the used field `x` appears in both contracts and the absence of a link causes switching the called contracts.

The rule `checkDispatcherUniqueSummarizationResult` passes despite the absence of a link because the summarized function `dummyB()` appears only in `CalleeB` so the dispatcher finds the right function.

To run this spec with a link run
```certoraRun certora/conf/runWithDispatcherWithLink.conf```

[The report of this run](https://prover.certora.com/output/1902/96cf026da0e24ec685e2b83f6b774d4a?anonymousKey=22fede80dbe5118c02b9dd070b3c1fb52dc15766)

All rules pass.
