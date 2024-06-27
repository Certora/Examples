methods {
    function balanceOf(address) external returns (uint256) envfree;
    function transfer(address,uint256) external returns (bool);
    function approve(address,uint256) external returns (bool);
}

rule transferRevertingConditions {
    env e;
    address recipient;
    uint256 amount;

    require e.msg.value == 0;
    require amount + balanceOf(recipient) <= max_uint256;
    
    bool senderIsZero = e.msg.sender == 0;
    bool recipientIsZero = recipient == 0;
    bool notEnoughFunds = balanceOf(e.msg.sender) < amount;
    
    transfer@withrevert(e, recipient, amount);

    assert lastReverted <=> senderIsZero || recipientIsZero || notEnoughFunds;
}

rule approveRevertingConditions {
    env e;
    address spender;
    uint256 amount;

    require e.msg.value == 0;

    bool ownerIsZero = e.msg.sender == 0;
    bool spenderIsZero = spender == 0;

    approve@withrevert(e, spender, amount);

    assert lastReverted <=> ownerIsZero || spenderIsZero;
}