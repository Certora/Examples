using Impl1 as impl1;
using Impl2 as impl2;
methods {
    
    // A function summary 
    function _.summarizedByFunction() external => summary() expect uint256;
    function _.notSummarized() external optional envfree; 
    // function impl2.notSummarized() external returns(uint256) envfree;
    function impl1.summarizedInCallerExternalOnly() external returns(uint256) envfree; 
    function impl2.summarizedInCallerExternalOnly() external returns(uint256) envfree;
    // If the contract name is omitted, the default is currentContract
    function summarizedInCallerExternalOnly() external returns(uint256) envfree => ALWAYS(15) ALL;  
    function callSummarizedByFunctionInCalledContract1() external returns(uint256) envfree;
    function callSummarizedByFunctionInCalledContract2() external returns(uint256) envfree;
    function callnotSummarizedInCalledContract1() external returns(uint256) envfree;
    function callSummarizedInCallerExternalOnlyInCalledContract1() external returns(uint256) envfree;
    function callSummarizedInCallerExternalOnlyInCalledContract2() external returns(uint256) envfree;
    function summarizedInCallerExternalOnly() external returns(uint256) envfree;
    function callSummarizedInCallerExternalOnly() external returns(uint256) envfree;
    function summarizedInternalInCaller() internal returns(uint256)  => ALWAYS(16) ALL;
    function callSummarizedInternalInCaller() external returns(uint256) envfree;
    // Wildcard method entry may not specify return types in the method signature.
    // HAVOC_ECF can be specified only for external functions.
    // Method annotation summarizedByECF() with both envfree and summary specification without explicit 
    // base contract is not allowed.
    // If this is truly the behavior you want, add an explicit currentContract qualifier
    function _.summarizedByECF() external => HAVOC_ECF;
}

// Function to be used as function summary.
function summary() returns uint256 {
    return 6;
}


rule checkA {
    assert (callSummarizedByFunctionInCalledContract1() == 6, "Function summary does not work");
}

rule checkB {
    assert (callSummarizedByFunctionInCalledContract2() == 6, "Function summary does not work");
}

// Not summarized
rule checkNotSummarized(){
    assert (callnotSummarizedInCalledContract1() == 3, "wrong result for not-summarized function");
}

// Functions in Impl1 and Impl2 not summarized. The external function in currentContract is summarized to 15.
rule checkSummarizedExternalOnly() {
    // Only the current contract's `summarizedInCallerExternalOnly()` function is summarized so the following 2 calls give the original function result.
    assert (callSummarizedInCallerExternalOnlyInCalledContract1() == 5, "wrong result for not-summarized function");
    assert (callSummarizedInCallerExternalOnlyInCalledContract2() == 5, "wrong result for not-summarized function");
    // The call used here uses the internal summarizedInCallerExternalOnly() which is not summarized.
    assert (callSummarizedInCallerExternalOnly() == 15, "ALWAYS summary does not apply for external function called from the contract");
    // If the function is called from CVL rather than from contract code then it is never replaced by a summary.
    // So this one is not replaced.
    assert (summarizedInCallerExternalOnly() == 15, "ALWAYS summary does not apply for function called from CVL");
}

// The external function summarizedInternalInCaller calls the internal function summarizedInternalInCaller which is summarized.
rule checkSummarizedInternalInCaller() {
    env e;
    assert (summarizedInternalInCaller(e) == 16, "ALWAYS summary does not apply for internal function called from CVL");
    assert (callSummarizedInternalInCaller() == 16, "Summarization of internal function does not take effect.");
}

// The summarization has to be on the internal function in order to take effect.
// The envfree qualifier is not allowed on internal functions, therefore an env variable is defined.
rule checkHavocECFSummary() {
    env e;
    assert (summarizedByECF(e) == 10, "HAVOC_ECF not applied for main contract");
    assert (impl1.summarizedByECF(e) == 7, "HAVOC_ECF applies for a contract that is not the main contract");
}
