invariant isUnlocked(env e) getLock(e) == 0 ;

invariant deltaZeroWhenUnlocked(env e) getLock(e) == 0 => getDelta(e) == 0 ;

invariant deltaEqualsStorage(env e) getDelta(e) == currentContract.storageValue {
    preserved onTransactionBoundary with (env e2) {
        requireInvariant isUnlocked(e2);
        requireInvariant deltaZeroWhenUnlocked(e2);
 }