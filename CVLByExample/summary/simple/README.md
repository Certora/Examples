This directory contains examples for [Function Summaries](https://docs.certora.com/en/latest/docs/cvl/cvl2/changes.html#summaries-only-apply-to-one-contract-by-default:~:text=a%20function%E2%80%99s%20sighash).-,Summaries%20only%20apply%20to%20one%20contract%20by%20default,%EF%83%81,-In%20CVL%201)

The interface `IntGetter` has the functions `get1()` and `get2()` that have no implementation. 
Function summaries are used instead of their missing implementations. Since IntGetter is an interface and not a contract a 
wildcard entry is used.

## Always.spec
Here the function `g1` is summarized by `ALWAYS(7)` while `g2` is not summarized.
Therefore, the rule `checlAlwaysSummary` the rule `checkNotSummarized` fails.

Run via ```certoraRun certora/conf/runAlways.conf```
[A report of this run](https://prover.certora.com/output/1902/4c92bd8a54b44521b83452e93f675907?anonymousKey=84d515da2c8d3b4e5a7d8b0a34137973d1751f96)

## AlwaysVsConstant.spec

Here the function `g1` is summarized by `ALWAYS(7)` while `g2` is summarized by `CONSTANT``.
This means that all calls to `g2` always return the same result but it can be other than `7` which is what `g1` is summarized to.
Therefore, the rule checkAlwaysSummary passes, while the rule checkConstantSummary fails.

Run via ```certoraRun certora/conf/runAlwaysVsConstant.conf```
[A report of this run](https://prover.certora.com/output/1902/d65e16a0a6d2451781cc1826c6ec4aa0?anonymousKey=941589808b3a5504ec8d54b78b1f41108ec7ac89)

## ConstantVSNondet.spec

Here the function `g1` is summarized by `CONTANT` while `g2` is summarized by `NONDET`.
This means that all calls to `g1` always return the same result and therefore the rule `checkConstantSummary` passes.
Since `g2` is summarized with `NONDET` two calla to `getFromG2()` can have different results and therefore the
rule `checkNondetSummary` fails.

Run via ```certoraRun certora/conf/runConstantVsNondet.conf```

[A report of this run](https://prover.certora.com/output/1902/c7ea19339a0240999d3fc15fc0f39bae?anonymousKey=2d1b5597b9c802826f6c32aba484639b63774aff)
