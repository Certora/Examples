
using ERC20 as Token;
using CurveTokenExample as LPToken;


ghost uint256 before_func1;
ghost uint256 after_func1;
ghost uint256 current_func1;
ghost bool cond;

hook Sstore solghost_return_func1 uint256 newValue (uint256 oldValue) STORAGE {
    current_func1 = newValue;
}

hook Sstore solghost_trigger_check bool newValue (bool oldValue) STORAGE {
    cond = cond && ((current_func1 == before_func1) || (current_func1 == after_func1));
}


// Maybe a better name would be "no_dirty_view_in_external_execution"
rule no_read_only_reentrancy(method f)
{
    env e;
    env e_external;
    calldataarg data;
    require cond;
    require before_func1 == getVirtualPrice(e_external);
    f(e, data);
    require after_func1 == getVirtualPrice(e_external);
    assert cond;
}