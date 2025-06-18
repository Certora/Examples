methods {
    function balanceOf(address) external returns (uint256) envfree;
    function transfer(address, uint256) external returns (bool);
    function approve(address, uint256) external returns (bool);
}

rule transferRevertingConditions() {
    env e;
    address recipient;
    uint256 amount;
    require e.msg.sender != recipient;
    uint256 balanceBefore = balanceOf(e.msg.sender);
    transfer@withrevert(e, recipient, amount);
    bool transferReverted = lastReverted;
    assert to_mathint(balanceOf(e.msg.sender)) > balanceBefore - amount => transferReverted;
}

rule approveRevertingConditions() {
    env e;
    address spender;
    uint256 amount;
    require e.msg.value == 0;
    bool ownerIsZero = e.msg.sender == 0;
    bool spenderIsZero = spender == 0;
    approve@withrevert(e, spender, amount);
    assert lastReverted <=> ownerIsZero || spenderIsZero;
}