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
        require contract_lock_status == isLocked(v), "Match contract lock status";
    }
}

// invariant version is getting SANITY_FAILURE using the below rule instead
// invariant lockStatusDontChange()
//     !contract_lock_status;

rule lockStatusDontChange() {
    require !contract_lock_status, "Pre condition"; // require contract is not locked
    // Check that after any method call, the lock is not held
    method f; env e; calldataarg args;
    f(e, args);
    assert !contract_lock_status;
}

// if contract was locked function call always reverted
rule checkContractLockReverts(){
    env e;
    require contract_lock_status; // require contract is locked

    contractLevelAccess@withrevert(e);

    assert lastReverted;
}