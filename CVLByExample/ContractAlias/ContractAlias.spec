import "Imported.spec";

methods {
    function A.Always1() internal returns (uint) => ALWAYS(2);
}

rule verifySummaryOnAlias() {
    env e;
    assert 2 == Always1(e);
}