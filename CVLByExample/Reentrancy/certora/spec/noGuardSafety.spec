/**
This rule is for systems that don't have reentrancy guard but want to check that all external calls are either first or last operation of a transaction.
We verify this by hooking on calls and store operations, and checking for a call within two store operations. 
**/


ghost bool called_extcall;
ghost bool storage_access_before_call;
ghost bool storage_access_after_call;

/// we are hooking here on "CALL" opcodes in order capture if there was a storage access before or/and after a call
hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    called_extcall = true;
}

/// For every store set storage_access_before_call or storage_access_after_call according to the call state.
hook ALL_SSTORE(uint loc, uint v) {
    if (!called_extcall) {
       storage_access_before_call = true;
    } else {
        storage_access_after_call = true; 
    }
} 

/// For every load set storage_access_before_call or storage_access_after_call according to the call state.
hook ALL_SLOAD(uint loc) uint v {
    if (!called_extcall) {
       storage_access_before_call = true;
    } else {
        storage_access_after_call = true; 
    }
} 

// Check that after calling a function we are either before or after the `call`.
rule reentrancySafety(method f) {
    //start with all flags false 
    require !called_extcall && !storage_access_before_call && 
            !storage_access_after_call;

    calldataarg args;
    env e;
    f(e,args);
    assert (!(storage_access_before_call && storage_access_after_call), "Reentrancy weakness exists");
}