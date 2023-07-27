
using ERC20 as Token;
using CurveTokenExample as LPToken;


ghost uint256 before_func1;
ghost uint256 after_func1;
ghost uint256 current_func1;
ghost bool cond;

// hook on the return value of the view function
hook Sstore solghost_return_func1 uint256 newValue (uint256 oldValue) STORAGE {
    current_func1 = newValue;
}

// hook on the read only reentrancy condition.
// true is the current result of the view function is equal to the result before the unresolved or
// to the result after the unresolved.
hook Sstore solghost_trigger_check bool newValue (bool oldValue) STORAGE {
    cond = cond && ((current_func1 == before_func1) || (current_func1 == after_func1));
}

// Using require for setting before_func1 to the value of getVirtualPrice before the unresolved call and
// setting after_func1 to the value of getVirtualPrice after the unresolved call.
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