rule cvlStringEqComparisonToEVMType() {
    env e;
    string r1;
    string r2 = Blurp;
    r1 = getBlurp(e);
    assert r1 == r2, "Should succeed";
}
