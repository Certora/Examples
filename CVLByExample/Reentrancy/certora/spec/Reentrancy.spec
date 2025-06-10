persistent ghost bool called_extcall;

persistent ghost bool g_reverted;

persistent ghost uint32 g_sighash;

// we are hooking here on "CALL" opcodes in order to simulate reentrancy to a non-view function and check that the function reverts
hook CALL uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength uint rc {
    called_extcall = true;
    env e;
    bool cond;
    if (g_sighash == sig:withdrawAll().selector) {
        withdrawAll@withrevert(e);
        // concrete name
        g_reverted = lastReverted;
    } else if (g_sighash == sig:withdraw(uint256).selector) {
        calldataarg args;
        withdraw@withrevert(e, args);
        // concrete name
        g_reverted = lastReverted;
    } else {
        // fallback case
        g_reverted = true;
    }
}

// The main rule - 
// we filter only for non-view methods as only state modifying methods 
// are dangerous for the specific reentrancy scenarios. 
rule no_reentrancy(method f, method g) filtered {f -> !f.isView, g -> !g.isView} {
    require !called_extcall;
    require !g_reverted;
    env e;
    calldataarg args;
    require g_sighash == g.selector;
    f@withrevert(e, args);
    // main assert here - we expect that if an external function is called
    // any reentrancy to a non-view function will revert
    assert called_extcall => g_reverted, "Reentrancy weakness exists";
}