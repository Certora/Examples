# Summarization According to Visibility, Function summary, Dispatcher

This directory demonstrates:
- summarization of external and internal functions.
- summarization of functions called from CVL (which is not applied).
- summarization by a CVL function.

The main contract is `Main.sol` which calls its internal functions as well as functions from the contracts Impl1 and Impl2.

## InternalExternalSummary.spec

This spec shows when a function is summarized according to its visibility.

Run this spec via
```certoraRun certora/conf/runInternalExternalSummary.conf```

[The report of this run](https://prover.certora.com/output/1902/200199806e5b45f4a1e8d8dd5203b4dd?anonymousKey=76178c551a0f52b0f7c4ccc6c6abf1e1349ab28a)

### Failing Rules
Rule `checkSummarizedExternalInCaller`:
The call used here uses the internal `summarizedExternal` which is not summarized. Therefore the assert fails. However, because the configuration is using `multi_assert_check` this assertion becomes a require (despite the fact that it failed) when we reach the second assertion which passes because of the requirement. This same assertion fails in 
rule `checkSummarizedCalledFromCVL` because if the function is called from CVL rather than from contract code then it is never replaced by a summary.
Therefore the call in the rule is not replaced and the rule fails.

### Verified rules
Rule `checkExternalSummarizations`:
The functions of `impl1` and the current contract are summarized but the function of impl2 is not. So both assertions
pass.

Rule `checkSummarizedInternalInCaller` passes because the external function summarizedInternal In Main calls the internal function summarizedInternal which is summarized.

## FunctionSummary.spec

This spec shows summarization by a CVL function.
function _.summarizedByFunction() external => summary() expect uint256;

each external summarizedByFunction is summarized by the CVL function summary().

Run this spec via

```certoraRun certora/conf/runFunctionSummary.conf```

[The result of this run](https://prover.certora.com/output/1902/99acf1eca52241c0aa2503997f87dcef?anonymousKey=4227ae43427f41621dacf0883c98bc9476482e83)
