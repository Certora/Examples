methods {
    function TransientTest.lock() external returns (bool) envfree;
    function TransientTest.unlock() external returns (bool) envfree;
    function TransientTest.isLocked() external returns (bool) envfree;
}

use builtin rule sanity;


// TODO
// tload/tstore hooks for locked field.

rule lockLocks() {
    // TODO: direct field access
    //require !currentContract.locked;

    require !currentContract.isLocked();
    lock();
    assert currentContract.isLocked();
}

rule unlockUnlocks() {
    require currentContract.isLocked();
    unlock();
    assert !currentContract.isLocked();
}
