// Strong invariant: must hold even during external calls
strong invariant storageValueIsConstant_strong(env e) 1 == currentContract.storageValue;

// Weak invariant: only needs to hold before and after top-level calls
weak invariant storageValueIsConstant_weak(env e) 1 == currentContract.storageValue;
