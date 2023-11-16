/*
 * This test is about figuring out in the case of a wildcard summary whether we should be summarizing
 * contract functions, library functions, or both.
 * Basically the idea is that if a signature _could_ be that of a contract function (i.e. no 'storage'
 * location specifiers) then we should summarize both regardless of whether their sighashes are the same or not).
 */
methods {
    // should summarize both contract and lib functions
    function _.funcWithStruct(CalledLibrary.S s) external => ALWAYS(1);

    // should summarize both contract and lib functions
    function _.funcWithEnum(CalledLibrary.E e) external => ALWAYS(4);

    // should summarize only the lib function
    function _.funcWithStorage(uint[] storage s) external => ALWAYS(2);

    // should summarize only the contract function (in the context of a library, no location
    // means _not_ storage, so that shouldn't be summarized here)
    function _.funcWithStorage(uint[] s) external => ALWAYS(3);
    
    function callLibFuncWithStruct(CalledLibrary.S s) external returns (uint) envfree;
    function callLibFuncWithEnum(CalledLibrary.E e) external returns (uint) envfree;
    function callLibFuncWithStorage() external returns (uint) envfree;
    function callContractFuncWithStruct(CalledLibrary.S s) external returns (uint) envfree;
    function callContractFuncWithEnum(CalledLibrary.E e) external returns (uint) envfree;
    function callContractFuncWithStorage() external returns (uint) envfree;
}

rule r1 {
    CalledLibrary.S s;
    uint v = callLibFuncWithStruct(s);
    assert v == 1;
}

rule r2 {
    CalledLibrary.S s;
    uint v = callContractFuncWithStruct(s);
    assert v == 1;
}

rule r3 {
    uint v = callLibFuncWithStorage();
    assert v == 2;
}

rule r4 {
    uint v = callContractFuncWithStorage();
    assert v == 3;
}

rule r5 {
    CalledLibrary.E e;
    uint v = callLibFuncWithEnum(e);
    assert v == 4;
}

rule r6 {
    CalledLibrary.E e;
    uint v = callContractFuncWithEnum(e);
    assert v == 4;
}

