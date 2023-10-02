# Summarization According to Visibility, Function summary, Dispatcher

This directory demonstrates:
- summarization of external and internal functions.
- summarization of functions called from CVL (which is not applied).
- summarization by a CVL function.

The main contract is `Main.sol` which calls its internal functions as well as functions from the contracts Impl1 and Impl2.

## InternalExternalSummary.spec

Run this spec via
```certoraRun certora/conf/runInternalExternalSummary.conf```

[The report of this run](https://prover.certora.com/output/1902/7991cd38d3224485ba71cb1b782f2b91?anonymousKey=f554e01b67174fc4c27562b3007c0ba38d4a5a97)

Rule `checkExternalSummarizations`:
The functions of `impl1` and the current contract are summarized but the function of impl2 is not. So both assertions
pass.

Rule `checkSummarizedExternalInCaller`:
The call used here uses the internal `summarizedInCallerExternalOnly` which is not summarized. Therefore the assert fails. However, because the configuration is using `multi_assert_check` this assertion becomes a require (despite the
fact it failed) when we reach the second assert which passes because of the require. This same assert fails in 
rule `checkSummarizedCalledFromCVL` because if the function is called from CVL rather than from contract code then it is never replaced by a summary.
So the call in the rule is not replaced and the rule fails.

Rule `checkSummarizedInternalInCaller` passes because the external function summarizedInternalInCaller calls the internal function summarizedInternalInCaller which is summarized.

## FunctionSummary.spec

This spec shows summarization by a CVL function.
function _.summarizedByFunction() external => summary() expect uint256;

each external summarizedByFunction is summarized by the CVL function summary().

Run this spec via

```certoraRun certora/conf/runFunctionSummary.conf```

[The result of this run](https://prover.certora.com/output/1902/5c00179e293f4a5ba9fe8321eb7ddc38?anonymousKey=8696514ecaba54eee653796bdf00e78140e47f59)
