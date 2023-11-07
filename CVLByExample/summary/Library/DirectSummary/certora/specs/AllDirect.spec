/**
 * For each function called from Test.sol a summary is provided.
 */

using TestLibrary as testlibrary;

methods {
    // functions declared in TestLibrary
    function TestLibrary.calleeInternal() internal returns bool => ALWAYS(true);
    function TestLibrary.calleeExternal() external returns bool => ALWAYS(true);
    // functions declared in IUnresolved
    function _.calleeOverloadedInInterfaceExternal()  external => ALWAYS(true) UNRESOLVED;
    // functions from the contract Test.
    function callInternal() external returns bool;
    function callExternal() external returns bool;
    function callIOverloadedInInterfaceExternal() external returns bool;
}

// Call summarized internal function.
rule callInternal(env e) { 
    assert (callInternal(e), "Internal function summarization is not applied");                               
}

// Call summarized external function
rule callExternal(env e) { 
    assert (callExternal(e), "External function summarization is not applied"); 
}

// Call resolved function which is not summarized.
rule callOverloadedInInterfaceExternal(env e) { 
    assert (callOverloadedInInterfaceExternal(e), "Resolved function is not summarized");         
}

// Call unresolved and therefore summarized function.
rule callIOverloadedInInterfaceExternal(env e) { 
    assert (callIOverloadedInInterfaceExternal(e), "Unresolved function not summarized as expected") ;        
}

rule callSummarizedFromCVL(env e) {
    assert (testlibrary.calleeExternal(e), "Function called from CVL is not summarized");
}
