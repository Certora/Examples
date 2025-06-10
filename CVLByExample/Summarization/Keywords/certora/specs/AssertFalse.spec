methods {
    unresolved external in A.execute => DISPATCH[Dummy._()] default ASSERT_FALSE;
}

// This should never be reached because the assert should fail due to no appropriate implementation in Dummy contract to resolve the unresolved call.
rule AssertFalse {
    env e;
    address x;
    bytes data;
    currentContract.execute(e, x, data);
    assert true;
}