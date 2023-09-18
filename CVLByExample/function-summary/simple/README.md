This directory contains examples for [Function Summaries](https://docs.certora.com/en/latest/docs/cvl/cvl2/changes.html#summaries-only-apply-to-one-contract-by-default:~:text=a%20function%E2%80%99s%20sighash).-,Summaries%20only%20apply%20to%20one%20contract%20by%20default,%EF%83%81,-In%20CVL%201)

The interface `IntGetter` has the functions `get1()` and `get2()` that have no implementation. 
Function summaries are used instead of their missing implementations. Since IntGetter is an interface and not a contract a 
wildcard entry is used.

## Always.spec
Here the function `g1` is summarized by `ALWAYS(7)` while `g2` is not summarized.
Therefore, the assert that `getFromG1()` that uses `g1` equals 7 passes, while the assert about `getFromG2()` that uses `g2` fails.

Run via ```certoraRun certora/conf/runAlways.conf```
[A report of this run](https://prover.certora.com/output/1902/8bd416feef064e02a3169f110ec20388?anonymousKey=c5a5c29437011bd771fda75f2dc19e32e3b00c31)

## AlwaysVsConstant.spec

Here the function `g1` is summarized by `ALWAYS(7)` while `g2` is summarized by `CONSTANT``.
This means that all calls to `g2` always return the same result but it can be other than `7` which is what `g1` is summarized to.
Therefore, the assert that `getFromG1()` equals 7 passes, while the assert that  ```getFromG2() == getFromG2()``` fails.

Run via ```certoraRun certora/conf/runAlwaysVsConstant.conf```
[A report of this run](https://prover.certora.com/output/1902/c059594cb62c4ed1b08653b585e083df?anonymousKey=7f4185bd8266a330f51886f47a0101f2d3a3c5c2)

## ConstantVSNondet.spec

Here the function `g1` is summarized by `CONTANT` while `g2` is summarized by `NONDET`.
This means that all calls to `g1` always return the same result and therefore the assert ```getFromG1() == getFromG1()``` passes.
Since `g2` is summarized with `NONDET` and call to `getFromG2()` can have a different result and therefore the
```assert(getFromG2() != getFromG2()``` fails.

Run via ```certoraRun certora/conf/runConstantVsNondet.conf```

[A report of this run](https://prover.certora.com/output/1902/53fbb6522a7a4d0290cad835806ce05c?anonymousKey=a759dd4cefe9d1e80c65f4cbd9e5ed144cc0e965)

## PerCallee.spec

[A report of this run](https://prover.certora.com/output/1902/74b9ed369a6843b5958dc89754771fe0?anonymousKey=2cc722f2173c8f0f98b6c05d196dc3e1a5c7a290)