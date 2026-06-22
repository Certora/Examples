/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Reentrancy ghost and hook                                                                                           │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
definition lock_on() returns bool = ghostReentrancyStatus == 2;
definition poll_functions(method f) returns bool = f.selector == sig:withdraw(uint256).selector ||
                                      f.selector == sig:deposit(uint256).selector ||
                                      f.selector == sig:flashLoan(address, uint256).selector;


ghost uint256 ghostReentrancyStatus;
ghost bool lock_status_on_call;

hook Sload uint256 status currentContract._status STORAGE {
    require ghostReentrancyStatus == status;
}

hook Sstore currentContract._status uint256 status STORAGE {
    ghostReentrancyStatus = status;
}

// we are hooking here on "CALL" opcodes in order to simulate reentrancy to a non-view function and check that the function reverts
hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    lock_status_on_call = lock_on(); 
}

// this rule prove the assumption e.msg.sender != currentContract;
rule reentrancyCheck(env e, method f, calldataarg args) filtered{f -> poll_functions(f)}{
    bool lockBefore = lock_on();
    
    f(e, args);
    
    bool lockAfter = lock_on();
    
    assert !lockBefore && !lockAfter;
    assert lock_status_on_call;
}