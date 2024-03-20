methods {

    function lockValue() external returns (uint256) envfree;
    function getContractLock() external returns (uint256) envfree;
}

definition isLocked(uint256 status) returns bool = status == lockValue();

persistent ghost bool contract_lock_status;

hook ALL_TSTORE(uint loc, uint v) {
    if (loc == getContractLock() && executingContract == currentContract) {
        contract_lock_status = isLocked(v);
    }
}

hook ALL_TLOAD(uint loc) uint v {
    if (loc == getContractLock() && executingContract == currentContract) {
        require contract_lock_status == isLocked(v);
    }
}

// if function call not reverted contract was unlocked before and should be unlocked after.
rule checkContractLock(){
    env e;

    bool lock_status_before = contract_lock_status;

    contractLevelAccess(e);

    bool lock_status_after = contract_lock_status;

    assert !lock_status_before && !lock_status_after;
}

// if contract was locked function call always reverted
rule checkContractLockReverts(){
    env e;
    require contract_lock_status; // require contract is locked

    contractLevelAccess@withrevert(e);

    assert lastReverted;
}