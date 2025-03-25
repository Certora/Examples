methods {
    function main(uint256, bool, address) external returns (uint256) envfree;

    
    unresolved external in Caller.doCall(address, bytes memory) => DISPATCH [
        Target.calculate(uint256)
    ] default HAVOC_ALL;

    unresolved external in Main.main(uint256, bool) => DISPATCH [
        Target.calculate(uint256)
    ] default HAVOC_ALL;

    unresolved external in Main.catch(address, uint256) => DISPATCH [
        Target.calculate(uint256)
    ] default NONDET;
    */
}


rule testRuleInternal(uint256 x) {
    mathint result = main(x, true, 0);
    assert result == x * x;
    satisfy result == x * x;
}


rule testRuleExternal(uint256 x) {
    mathint result = main(x, false, 0);
    assert result == x * x;
    satisfy result == x * x;
}


rule testCatch(uint256 x) {
    env e;
    mathint result = catchCall(e, x);
    assert result == x * x;
    satisfy result == x * x;
}


rule testNoCode(uint256 x, address callTarget) {
    require nativeCodesize[callTarget] == 0;
    require callTarget != 0 && callTarget != currentContract.target;
    env e;
    main@withrevert(x, true, callTarget);
    assert lastReverted;
}
