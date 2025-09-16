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
However, `isG2Always7` is violated as `g2` can be any value. As default, the Certora Prover takes into account that any value is a possible one.

Run via ```certoraRun runAlways.conf```
[A report of this run](https://prover.certora.com/output/15800/53f5e71cfc2d4bb88a6855416c0f368a?anonymousKey=e86020ee7b4c794392a80634fb73dc5dd84b680a)

## AlwaysVsConstant.spec

Here the function `get1` is summarized by `ALWAYS(7)` while `get2` is summarized by `CONSTANT`.
This means that all calls to `get2` always return the same result though it can be different than `7`.
Therefore, the rule `constantCanbeAnyValue` demonstrates that `g2` can be 7, while the rule `constantVsAlways` is violated as `get1` can be different than `get2`.

Rule `constantDoesNotChange` checks whether `get2` is that value before each function. Notice that this rule is successfully verified on all functions, including `set2` demonstrating that contract summarization implies the same value even on state-changing functions. 

Run via ```certoraRun runAlwaysVsConstant.conf```
[A report of this run](https://prover.certora.com/output/15800/69e2a0abbb8f457e91afbfa5274d6ec2?anonymousKey=2eda63648a577a53bd83dd1784da675d3f109376)

## ConstantVSNondet.spec

Here the function `get1` is summarized by `CONSTANT` while `get2` is summarized by `NONDET`.
This means that all calls to `get1` always return the same result and therefore the rule `checkConstantSummary` is verified.
Since `get2` is summarized with `NONDET` two calls to `get2` can have different results and therefore the
rule `checkNondetSummary` fails.

Run via ```certoraRun runConstantVsNondet.conf```
[A report of this run](https://prover.certora.com/output/15800/df823f7aced1420bb8465bf528d985b2?anonymousKey=f2b897c21ca68906938041456cce7c93a5633405)


## NondetVsHavoc.spec

Here we add two implementations of `IntGetter` to the list of contracts, and demonstrate the use of NONDET to indicate that no state has changed. Rule `checkChangeGi` indicates which function call can change `gi`.
Due to the nondet summarization of `get1` the rule is verified for `setToG1`. However, it shows a case of change to both `get1` and `get2` on a call to `setToG2`. This is due to the havoc that assumes any slot can change. 

Run via ```certoraRun runNondetVsHavoc.conf```
[A report of this run](https://prover.certora.com/output/15800/832957cbca9c429ba02c991e5e66ad1b?anonymousKey=93c59e757ee4714cb1cca8f32962e63c58cc218c)

## NoSummary.spec

In this spec the functions are not summarized.

To run this spec with no link run

```certoraRun runNoSummaryNoLink.conf```

[The report of this run](https://prover.certora.com/output/15800/b9fce10a39364ffe863f197daba70f79?anonymousKey=98df44442a06b4bf31cbce631fb1b278fc818870)

The rule `checkNoSummarization` fails because without linking the results of the functions are havoced.

To run this spec with linking run

```certoraRun runNoSummaryWithLink.conf```

[The report of this run](https://prover.certora.com/output/15800/fc43fcc16ca042d5b653694d5a85112d?anonymousKey=f79d54e730be86ed1edc75d7f71881e603308dd8)

## WithDispatcher.spec

This spec contains DISPATCHER summarizations for a multi-contract setting. The summarized function `x()` appears in both contracts while the function `dummyB` appears only in `AnotherIntGetterImpl`. The spec is run with two configurations: one with linking and one without.

To run this spec with no link run
```certoraRun runWithDispatcherNoLink.conf```

[The report of this run](https://prover.certora.com/output/15800/95dbe47ccdcb41de89ef4e447a9cbbad?anonymousKey=deaf578facfafa84af9d3336c474631000a204eb)

The rule `checkDispatcherUnresolvedSummarizationResult` fails because the used field `x` appears in both contracts and the absence of a link causes switching the called contracts.

The rule `checkDispatcherUniqueSummarizationResult` passes despite the absence of a link because the summarized function `dummyB()` appears only in `CalleeB` so the dispatcher finds the right function.

To run this spec with a link run
```certoraRun runWithDispatcherWithLink.conf```

[The report of this run](https://prover.certora.com/output/15800/bfab06516c284769bd7a5d41f520d95a?anonymousKey=65421f0b6a30bd261348c979d96d0f6e6c6643cc)

All rules pass.

## DispatcherFallbackInlining.spec

This spec shows how you can make the prover inline fallback functions when it doesn't find an implementation in a contract.

`CallsExternalContract` has a function `foo()` which simply calls the function `noSuchFun()` on an external address. `IntGetterImpl` doesn't have this function but has a fallback that sets one of it's fields to 5. `AnotherIntGetterImpl` do have this function and a fallback that sets one of it's fields to 5.

The spec has 2 rules: 
* `fallback_should_be_reached_with_flag` - shows the case where we make the prover only calling `IntGetterImpl` and since it doesn't have the function, the fallback will be used instead through the rule.
* 'fallback_should_never_be_reached' - And the case in which we make the prover call `AnotherIntGetterImpl` and we don't use the fallback since it has the function `noSuchFunc()` defined.

To run this spec with a link run
```certoraRun runDispatcherFallbackInlining.conf```

[The report of this run](https://vaas-stg.certora.com/output/15800/b1f5f96540cf4f2e9a61ecab69198203?anonymousKey=e85561774dc621d29cea45ae0b5829f2ad775316)


# Certora Example: Demonstrating `ASSERT_FALSE` Default Summary in Dispatch List

## Overview

This repository provides an example to demonstrate the usage of the `ASSERT_FALSE` default summary in a dispatch list. This example shows how mapping the default behavior of an unresolved call to `ASSERT_FALSE` ensures that the specification will fail if the call cannot be properly resolved.

## Solidity Contracts

This example includes two simple Solidity contracts: `A` and `Dummy`.

### Contract A

```solidity
contract A {
    function execute(address x, bytes calldata data) external {
        (bool success, ) = x.call(data);
    }
}
```

### Contract Dummy

```solidity
contract Dummy {}
```

### Contract Details

- **Contract A**: Implements the `execute` function, which makes an external call to a given address `x` with provided call data `data`.
- **Contract Dummy**: A placeholder contract with no implemented functions. It serves to demonstrate how unresolved calls are handled when no appropriate implementation exists.

## Specification

The specification demonstrates the use of the `ASSERT_FALSE` default summary in a dispatch list to handle unresolved calls.

### Specification

```cvl
methods {
     unresolved external in A.execute(address x, bytes calldata data) => DISPATCH [
        Dummy._
    ] default ASSERT_FALSE;
}

rule AssertFalse {
    env e;
    address x;
    bytes data;
    currentContract.execute(e, x, data);
    assert true;
} 
```

### Specification Breakdown

1. **Methods Block**:
   - **`unresolved external in A.execute(address x, bytes calldata data)`**: Specifies how unresolved external calls in the `execute` function of contract `A` should be handled.
   - **`DISPATCH [ Dummy._ ]`**: Indicates that any unresolved call should first attempt to match against functions in contract `Dummy`.
   - **`default ASSERT_FALSE`**: If no match is found, the specification will default to `ASSERT_FALSE`, causing an assertion failure.

2. **Rule `AssertFalse`**:
   - This rule is designed to fail. It calls `execute` and expects the unresolved call to result in an `ASSERT_FALSE` because `Dummy` does not implement any function that matches the call.
   - **`assert true;`**: This line is intentionally unreachable; the rule should fail before it reaches this point due to the `ASSERT_FALSE` in the dispatch list.

## Key Points

- **`ASSERT_FALSE` Default Summary**: This example illustrates how using `ASSERT_FALSE` as the default summary in a dispatch list ensures that any unresolved call without a matching implementation will cause the verification to fail.

## How to Run the Example

1. **Run Certora Prover**:
   - Command:
     ```bash
     certoraRun runAssertFalse.conf
     ```

2. **Check the Output**: The execution shows that the rule `AssertFalse` fails, demonstrating that the `ASSERT_FALSE` default summary correctly causes a specification failure when no appropriate function implementation is found.

### Execution Link
[Certora Run Output](https://prover.certora.com/output/1512/833e5d3150fc481a9c0bc5f816b9e8e8?anonymousKey=33e2ef368ab2521850c7ae186c3bcc7d4d1c4b63)

## Demonstrating `NONDET` on `unresolved external`

The spec in UnresolvedNondet.spec demonstrates how we can summarize the unresolved call in contract `A` from the previous example to return a nondeterministic value. It asserts that a field of the contract remains unchanged to demonstrate that the storage is not havoced.


To run this spec with a link run
```certoraRun runUnresolvedNondet.conf```

[The report of this run](https://prover.certora.com/output/950033/43e0d701a8524e55b653131228cc2929?anonymousKey=effcc27da0f85acb33dbe2dab5bc0d9b435cca3f)
