/**
    Summarization of internal vs external functions. Public functions have both external and internal instances.
    When the public function is called the external function is called and calls the internal summary.
*/

using Impl1 as impl1;
using Impl2 as impl2;
methods {
    
    function Impl1.summarizedExternal() external returns(uint256) envfree => ALWAYS(1); 
    function Impl2.summarizedExternal() external returns(uint256) envfree;
    // Methods of the main contract.
    // If the contract name is omitted, the default is currentContract
    function summarizedExternal() external returns(uint256) envfree => ALWAYS(15) ALL;  
    // envfree is not allowed on internal functions.
    function summarizedInternal() internal returns(uint256)  => ALWAYS(16) ALL;
    function callSummarizedExternalInCalled1() external returns(uint256) envfree;
    function callSummarizedExternalInCalled2() external returns(uint256) envfree;
    function callSummarizedExternalInCaller() external returns(uint256) envfree;
    function callSummarizedInternalInCaller() external returns(uint256) envfree;
}

rule checkExternalSummarizations(){
     // The functions of `impl1` and the current contract are summarized but the function of impl2 is not.
     // This call uses the summarization so the assertion should pass.
    assert (callSummarizedExternalInCalled1() == 1, "wrong result for summarized function");
    // The following  call uses the original function result. Should pass.
    assert (callSummarizedExternalInCalled2() == 5, "wrong result for not-summarized function");
}

// Shows when external summarization is not applied.
rule checkSummarizedExternalInCaller() {
    // The call used here calls the external summarizedExternal() which uses the internal summarizedExternal() 
    // which is not summarized. Therefore the assertion fails.
    assert (callSummarizedExternalInCaller() == 15, "ALWAYS summary does not apply for external function called from the contract");
    // If the function is called from CVL rather than from contract code then it is never replaced by a summary.
    // Therefore this particular one is not replaced. But since the run is with the option `multi_assert_check`, the previous assertion is assumed to hold 
    // when checking the next assertion and therefore it passes.
    assert (summarizedExternal() == 15, "ALWAYS summary does not apply for function called from CVL");
}

// The summary does not apply when called from CVL so the rule should fail.
rule checkSummarizedCalledFromCVL() {
    // If the function is called from CVL rather than from contract code then it is never replaced by a summary.
    // So this one is not replaced.
    assert (summarizedExternal() == 15, "ALWAYS summary does not apply for function called from CVL");
}

// The public function summarizedInternal in contract Main calls the internal function summarizedInternal 
// which is summarized.
rule checkSummarizedInternalInCaller() {
    env e;
    assert (callSummarizedInternalInCaller() == 16, "Summarization of internal function does not take effect.");
}

