This directory contains examples for [Function Summaries](https://github.com/Certora/Documentation/blob/master/docs/cvl/methods.md)
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
[A report of this run](https://prover.certora.com/output/40726/361048ae0da74d679958d51d821dc16a/?anonymousKey=b781f7b5cdfc95185abdc2bd6abc9602f324dd9a)

## AlwaysVsConstant.spec

Here the function `get1` is summarized by `ALWAYS(7)` while `get2` is summarized by `CONSTANT`.
This means that all calls to `get2` always return the same result but it can be other than `7`.
Therefore, the rule `constantCanbeAnyValue` demonstrates that the `g2` can be to 7, while the rule `constantVsAlways` is violated as `get1` can be different than `get2`.

Rule `constantDoesNotChange` checks whether `get2` is that value before each function. Notice that this rule is successfully verified on all functions, including `set2` demonstrating that contast summarization implies the same value even on state-changing functions. 

Run via ```certoraRun certora/conf/runAlwaysVsConstant.conf```
[A report of this run](https://prover.certora.com/output/40726/d90a11ab2f21410699b9a6ebfa6e7573/?anonymousKey=2d6835f97ab752dffcdc383e666f57f4a8c55918)

## ConstantVSNondet.spec

Here the function `get1` is summarized by `CONTANT` while `get2` is summarized by `NONDET`.
This means that all calls to `get1` always return the same result and therefore the rule `checkConstantSummary` is verified.
Since `get2` is summarized with `NONDET` two calls to `get2` can have different results and therefore the
rule `checkNondetSummary` fails.

Run via ```certoraRun certora/conf/runConstantVsNondet.conf```

[A report of this run](https://prover.certora.com/output/40726/e1a244dae4724318ba36a0b02e4ff75e/?anonymousKey=90a3a3f9205a8816ff80e0e8eb5de24f7a19ac48)


## NondetVsHavoc.spec

Here we add an implementation of `IntGetter` to the list of contracts, and demonstrate the use of NONDET to indicate that no state has changed. Rule `checkChange` indicates which function call can change which variable.
Due to the nondet summarization of `get1` the rule is verified for `setToG1`. However it shows a case of change to both `get1` and `get2` on a call to `setToG2`, this is due to the havoc that assumes any slot can change. 

[A report of this run](https://prover.certora.com/output/40726/d6d69da45a04424bab039b2656346ca1/?anonymousKey=8cbe9429d189f0f84e99a7dcd2007e6d08820777)