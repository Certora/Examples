methods {
    function accessInvariant(address) external returns (bool) envfree;
    function increase(address, int256) external envfree;
}

invariant alwaysPositive(address a)
    currentContract.balance[a] >= 0;

hook Sload bool b currentContract.accessInvariant[KEY address user] {
    requireInvariant alwaysPositive(user);
}


rule shouldFail(address a) {
    bool assertVal = (currentContract.balance[a] >= 0);
    assert assertVal;
    bool b = accessInvariant(a);
    assert true;
}

rule shouldSucceed(address a) {
    bool assertVal = (currentContract.balance[a] >= 0);
    bool b = currentContract.accessInvariant(a);
    assert assertVal;
}

rule shouldSucceed2(address a) {
    int256 value;
    bool assertVal = (currentContract.balance[a] >= 0);
    increase(a, value);
    bool b = currentContract.accessInvariant(a);
    assert assertVal;
}
