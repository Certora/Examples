# Summarization According to Visibility, Function summary, Dispatcher

This directory demonstrates:
- summarization of external and internal functions.
- summarization of functions called from CVL (which is not applied).
- summarization by a CVL function.

The main contract is `Main.sol` which calls its internal functions as well as functions from the contracts Impl1 and Impl2.

## InternalExternalSummary.spec

This spec shows when a function is summarized according to its visibility.

Run this spec via
```certoraRun runInternalExternalSummary.conf```

[The report of this run](https://prover.certora.com/output/15800/cac7d8a111414456b1e1d97aad82fb3a?anonymousKey=f76136a6b62e4744d72cfdc45fae8227bf53ff93)

### Failing Rules
Rule `checkSummarizedExternalInCaller`:
The call used here uses the internal `summarizedExternal` which is not summarized. Therefore the assert fails. However, because the configuration is using `multi_assert_check` this assertion becomes a require (despite the fact that it failed) when we reach the second assertion which passes because of the requirement. This same assertion fails in 
rule `checkSummarizedCalledFromCVL` because if the function is called from CVL rather than from contract code then it is never replaced by a summary. Therefore, the call in the rule is not replaced and the rule fails.

### Verified rules
Rule `checkExternalSummarizations`:
The functions of `impl1` and the current contract are summarized but the function of `impl2` is not. So both assertions
pass.

Rule `checkSummarizedInternalInCaller` passes because the external function `summarizedInternal` in `Main` calls the internal function `summarizedInternal` which is summarized.

## FunctionSummary.spec

This spec shows summarization by a CVL function.
`function _.summarizedByFunction() external => summary() expect uint256;`

each external `summarizedByFunction` is summarized by the CVL function `summary()`.

Run this spec via

```certoraRun runFunctionSummary.conf```

[The result of this run](https://prover.certora.com/output/15800/7805eb8e73fb40e8ad56735446a1c15a?anonymousKey=32d31e15e53a4ff690da2ebbaec128074a7d7e21)
