methods {
    unresolved external in A.execute(address x, bytes calldata data) => DISPATCH[
        Dummy._
    ] default ASSERT_FALSE;
}

rule AssertFalse() {
    env e;
    address x;
    bytes data;
    currentContract.execute(e, x, data);
    assert true; // This should never be reached because the assert should fail due to no appropriate implementation in Dummy contract to resolve the unresolved call.
}
