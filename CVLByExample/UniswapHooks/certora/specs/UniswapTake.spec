methods {
    function PoolManagerHarness.getDelta(PoolManagerHarness.Currency currency, address account) external returns (int256) envfree;
}

rule take_accounting_ok(PoolManagerHarness.Currency currency, address to, uint256 amount) {
    env e;
    mathint before_take = getDelta(currency, e.msg.sender);
    take(e, currency, to, amount);
    mathint after_take = getDelta(currency, e.msg.sender);
    assert after_take == before_take - amount;
}
