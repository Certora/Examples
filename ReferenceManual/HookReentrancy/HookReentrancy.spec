// In this test, we have the following sequence of events:
// rule
//   updateX()
//     assign to x, triggering hook
//       update xStoreCount
//       updateX()
//         assign to x, shouldn't trigger hook since hook is running
//
// See https://docs.certora.com/en/latest/docs/cvl/hooks.html#recursive-hooks

methods {
    function updateX() external envfree;
}

/// the number of stores to `x`
ghost mathint xStoreCount;

/// increment xStoreCount and recursively update `x`
hook Sstore x uint v STORAGE {
    xStoreCount = xStoreCount + 1;
    if (xStoreCount < 5) {
        updateX();
    }
}

/// This rule will pass because hooks are not recursively applied
rule checkStoreCount {
    require xStoreCount == 0;
    updateX();
    assert xStoreCount == 1;
    updateX();
    assert xStoreCount == 2;
}

