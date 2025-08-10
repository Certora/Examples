methods {
    function summarizedInternal() internal returns (uint) => cvlSummary();
    // function anInternalFunction() internal returns (uint) envfree; <-- This will fail compilation: 'The envfree qualifier is not allowed on internal functions'
}

function cvlSummary() returns (uint) {
    return 1;
}

rule internalFunctionCall {
    env e;

    assert anInternalFunction(e) == 0;
    assert summarizedInternal(e) == 1;

    // A.S s;
    // internalFunctionWithStorageInput(e, s); <-- This will fail compilation: 'could not type expression "internalFunctionWithStorageInput(e,s)", message: Cannot call internal function internalFunctionWithStorageInput from spec because input parameter '_s' has storage location'
    // internalFunctionWithStorageOutput(e); <-- This will fail compilation: 'could not type expression "internalFunctionWithStorageOutput(e)", message: Cannot call internal function internalFunctionWithStorageOutput from spec because output parameter #0 has storage location'
}
