methods {
    function TransientTest.lock() external returns (bool) envfree;
    function TransientTest.unlock() external returns (bool) envfree;
}

ghost bool ghostLocked;


// We can hook on the transient field locked just like on any normal storage field
hook Tload bool value currentContract.locked {
    require ghostLocked == value, "we want our ghost to match the read value";
}

hook Tstore currentContract.locked bool value (bool oldValue) {
    require ghostLocked == oldValue, "our ghost must have matched the old value before this store";
    ghostLocked = value;
}


rule lockLocks() {
    // we can also directly access the transient field from cvl, like any normal field
    require !currentContract.locked, "initially we want to be in unlocked state";
    lock();
    assert currentContract.locked;
    assert ghostLocked;
}

rule unlockUnlocks() {
    require currentContract.locked, "initially we want to be in locked state";
    unlock();
    assert !currentContract.locked;
    assert !ghostLocked;
}