/**
  Shows the difference between calls to a function summarized by function summary and calls to a non-summarized function.
  */
using Impl1 as impl1;
using Impl2 as impl2;
methods {
    
    // A wildcard method entry may not specify return types in the method signature.
    // The summarized functions belong to other contracts and therefore defined as `external`.
    // Functions of other contracts
    function _.summarizedByFunction() external => summary() expect uint256;
    function _.notSummarized() external optional envfree; 
    // functions of the main contract
    function callByFunctionInCalled1() external returns(uint256) envfree;
    function callByFunctionInCalled2() external returns(uint256) envfree;
    function callnotSummarizedInCalled1() external returns(uint256) envfree;
}   

// Function to be used as function summary.
function summary() returns uint256 {
    return 6;
}

// Calling summarized function of Impl1 contract. Should pass.
rule checkA {
    assert (callByFunctionInCalled1() == 6, "Function summary does not work");
}

// Calling summarized function of Impl2 contract. Should pass.
rule checkB {
    assert (callByFunctionInCalled2() == 6, "Function summary does not work");
}

// Not summarized. Should pass.
rule checkNotSummarized(){
    assert (callnotSummarizedInCalled1() == 3, "wrong result for not-summarized function");
}

