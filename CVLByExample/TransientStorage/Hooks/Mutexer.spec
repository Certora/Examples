methods {
    function isLocked() external returns (bool) envfree;
}

definition isLockedCVL(uint256 status) returns bool = status == 1;
definition slot() returns uint = 0xa2e3618ded7ae709dc8e3747186ad9112d852b6c6eef8285dea55c33fdac431f;

persistent ghost bool contract_lock_status{
    init_state axiom contract_lock_status == false;
}

hook ALL_TSTORE(uint loc, uint v) {
    if(loc == slot() && executingContract == currentContract){
        contract_lock_status = isLockedCVL(v);
    } else {
        // Explicitly havocing the ghost to ensure the condition is met (there is tstore on another slot)
        havoc contract_lock_status;
    }
}

hook ALL_TLOAD(uint loc) uint v {
    if(loc == slot() && executingContract == currentContract){
        require contract_lock_status == isLockedCVL(v);
    } else {
        // Explicitly havocing the ghost to ensure the condition is met (there is tload on another slot)
        havoc contract_lock_status;
    }
}
invariant lockStatusDontChange()
    !contract_lock_status;

// if contract was locked function call always reverted
rule checkContractLockReverts(){
    env e;
    require isLocked(); // require contract is locked

    contractLevelAccess@withrevert(e);

    assert lastReverted;
}