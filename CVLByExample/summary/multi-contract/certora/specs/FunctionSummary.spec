/**
  Shows the difference between calls to a function summarized by funcion summary and calls to a non-summarized function.
  */
using Impl1 as impl1;
using Impl2 as impl2;
methods {
    
    // A function summary 
    // Wildcard method entry may not specify return types in the method signature.
    // The summarized functions belong to other contracts and therefore defined external.
    // Functions of other contracts
    function _.summarizedByFunction() external => summary() expect uint256;
    function _.notSummarized() external optional envfree; 
    // functions of the main contract
    function callSummarizedByFunctionInCalledContract1() external returns(uint256) envfree;
    function callSummarizedByFunctionInCalledContract2() external returns(uint256) envfree;
    function callnotSummarizedInCalledContract1() external returns(uint256) envfree;
}   

// Function to be used as function summary.
function summary() returns uint256 {
    return 6;
}

// Calling summarized function of Impl1 contract. Should pass.
rule checkA {
    assert (callSummarizedByFunctionInCalledContract1() == 6, "Function summary does not work");
}

rule checkB {
    assert (callSummarizedByFunctionInCalledContract2() == 6, "Function summary does not work");
}

// Calling summarized function of Impl2 contract. Should pass.
// Not summarized. Should pass.
rule checkNotSummarized(){
    assert (callnotSummarizedInCalledContract1() == 3, "wrong result for not-summarized function");
}

