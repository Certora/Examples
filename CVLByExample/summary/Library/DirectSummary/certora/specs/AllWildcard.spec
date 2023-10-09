/**
 * Every function being called (from solidity) is given its a summarization using a wildcard.
 */
 using TestLibrary as testlibrary;

 methods {
    function _.calleeInternal() internal  => ALWAYS(true);
    function _.calleeExternal() external  => ALWAYS(true);
    // functions declared in IUnresolved
    function _.calleeOverloadedInInterfaceExternal()  external => ALWAYS(true) UNRESOLVED;
    // functions from the contract Test to call in rules
    function callInternal() external returns bool;
    function callExternal() external returns bool;
    function callOverloadedInInterfaceExternal() external returns bool;
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
