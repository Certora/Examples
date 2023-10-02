/**
    Summarization of internal vs external functions.
*/

using Impl1 as impl1;
using Impl2 as impl2;
methods {
    
    function impl1.summarizedInCallerExternalOnly() external returns(uint256) envfree => ALWAYS(1); 
    function impl2.summarizedInCallerExternalOnly() external returns(uint256) envfree;
    // Methods of the main contract.
    // If the contract name is omitted, the default is currentContract
    function summarizedInCallerExternalOnly() external returns(uint256) envfree => ALWAYS(15) ALL;  
    function summarizedInternalInCaller() internal returns(uint256)  => ALWAYS(16) ALL;
    function callSummarizedInCallerExternalOnlyInCalledContract1() external returns(uint256) envfree;
    function callSummarizedInCallerExternalOnlyInCalledContract2() external returns(uint256) envfree;
    function callSummarizedInCallerExternalOnly() external returns(uint256) envfree;
    function callSummarizedInternalInCaller() external returns(uint256) envfree;
}

rule checkExternalSummarizations(){
     // The functions of `impl1` and the current contract are summarized but the function of impl2 is not.
     // This call gives the summarization so the assert should pass.
    assert (callSummarizedInCallerExternalOnlyInCalledContract1() == 1, "wrong result for summarized function");
    // The following  call gives the original function result. Should pass.
    assert (callSummarizedInCallerExternalOnlyInCalledContract2() == 5, "wrong result for not-summarized function");
}

// Shows when external summarization is not applied.
rule checkSummarizedExternalInCaller() {
    // The call used here uses the internal summarizedInCallerExternalOnly() which is not summarized. Therefore the assert fails.
    assert (callSummarizedInCallerExternalOnly() == 15, "ALWAYS summary does not apply for external function called from the contract");
    // If the function is called from CVL rather than from contract code then it is never replaced by a summary.
    // So this one is not replaced. But since the run is with the option `multi_assert_check`, the previous assert is assumed to hold 
    // when checking the next assert and therefore it passes.
    assert (summarizedInCallerExternalOnly() == 15, "ALWAYS summary does not apply for function called from CVL");
}

// The summary does not apply so the rule should fail.
rule checkSummarizedCalledFromCVL() {
    // If the function is called from CVL rather than from contract code then it is never replaced by a summary.
    // So this one is not replaced.
    assert (summarizedInCallerExternalOnly() == 15, "ALWAYS summary does not apply for function called from CVL");
}

// The external function summarizedInternalInCaller calls the internal function summarizedInternalInCaller which is summarized.
rule checkSummarizedInternalInCaller() {
    env e;
    assert (callSummarizedInternalInCaller() == 16, "Summarization of internal function does not take effect.");
}

