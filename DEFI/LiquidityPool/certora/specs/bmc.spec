/* Bounded Model Checking - example spec for Liquidity Pool */

using Asset as underlying;

methods {
    function balanceOf(address) external returns(uint256) envfree;
    function totalSupply() external returns(uint256) envfree;
    function transfer(address, uint256) external returns(bool);
    function transferFrom(address, address, uint256) external returns(bool);
    function amountToShares(uint256) external returns(uint256) envfree;
    function sharesToAmount(uint256) external returns(uint256) envfree;
    function depositedAmount() external returns(uint256) envfree;
    function calcPremium(uint256) external returns (uint256) envfree;

    //function _.executeOperation(uint256,uint256,address) external => DISPATCHER(true);
    function _.executeOperation(uint256,uint256,address) external => NONDET;

    function underlying.balanceOf(address) external returns(uint256) envfree;
    function underlying.allowance(address, address) external returns(uint256) envfree;
    function underlying.totalSupply() external returns(uint256) envfree;
}

/// @notice Only `deposit` is not vacuous in this case
rule sharesNeverGreaterThanAssets1(address client, method f) {
    reset_storage currentContract;

    env e;
    calldataarg args;
    f(e, args);

    assert sharesToAmount(balanceOf(client)) <= depositedAmount();
}


rule sharesNeverGreaterThanAssets2(address client, method f1, method f2) filtered {
    f1 -> !f1.isView && f1.selector == sig:deposit(uint256).selector,  // Only option for first method
    f2 -> !f2.isView
} {

    reset_storage currentContract;

    env e1;
    calldataarg args1;
    f1(e1, args1);

    env e2;
    calldataarg args2;
    f2(e2, args2);

    assert sharesToAmount(balanceOf(client)) <= depositedAmount();
}


// << Sufficient to find mutation bug in `flashLoan`
rule sharesNeverGreaterThanAssets3(address client, method f1, method f2, method f3) filtered {
    f1 -> !f1.isView && f1.selector == sig:deposit(uint256).selector,  // Only option for first method
    f2 -> !f2.isView,
    f3 -> !f3.isView
} {

    reset_storage currentContract;

    env e1;
    calldataarg args1;
    f1(e1, args1);

    env e2;
    calldataarg args2;
    f2(e2, args2);

    env e3;
    calldataarg args3;
    f3(e3, args3);

    assert sharesToAmount(balanceOf(client)) <= depositedAmount();
}


rule sharesNeverGreaterThanAssets4(address client, method f1, method f2, method f3, method f4) filtered {
    f1 -> !f1.isView && f1.selector == sig:deposit(uint256).selector,  // Only option for first method
    f2 -> !f2.isView,
    f3 -> !f3.isView,
    f4 -> !f4.isView
} {

    reset_storage currentContract;

    env e1;
    calldataarg args1;
    f1(e1, args1);

    env e2;
    calldataarg args2;
    f2(e2, args2);

    env e3;
    calldataarg args3;
    f3(e3, args3);

    env e4;
    calldataarg args4;
    f4(e4, args4);

    assert sharesToAmount(balanceOf(client)) <= depositedAmount();
}


rule example(address receiverAddress, uint256 amount) {
    reset_storage currentContract;

    env e1;
    calldataarg args1;
    deposit(e1, args1);

    env e2;
    calldataarg args2;
    underlying.approve(e2, args2);
    
    env e21;
    calldataarg args21;
    underlying.approve(e21, args21);
    
    env e3;
    calldataarg args3;
    setFeeRate(e3, args3);

    /*
    env e22;
    calldataarg args22;
    underlying.approve(e22, args22);

    env e3;
    calldataarg args3;
    approve(e3, args3);

    env e31;
    calldataarg args31;
    approve(e31, args31);
    */

    env e4;
    calldataarg args4;
    /*
    require e4.msg.value == 0;
    require e4.msg.sender != currentContract;
    require e4.msg.sender != 0;
    require amount <= depositedAmount();
    require underlying.allowance(e4.msg.sender, currentContract) == max_uint256;
    require underlying.allowance(currentContract, currentContract) == max_uint256;
    require currentContract.feeRate != 0;
    require calcPremium(amount) != 0;
    */

    flashLoan(e4, receiverAddress, amount);

    satisfy true; //sharesToAmount(balanceOf(client)) <= depositedAmount();
}

rule sharesNeverGreaterThanAssets5(
    address client,
    method f1,
    method f2,
    method f3,
    method f4,
    method f5
) filtered {
    f1 -> !f1.isView && f1.selector == sig:deposit(uint256).selector,
    f2 -> !f2.isView,
    f3 -> !f3.isView,
    f4 -> !f4.isView,
    f5 -> !f5.isView
} {

    reset_storage currentContract;

    env e1;
    calldataarg args1;
    f1(e1, args1);

    env e2;
    calldataarg args2;
    f2(e2, args2);

    env e3;
    calldataarg args3;
    f3(e3, args3);

    env e4;
    calldataarg args4;
    f4(e4, args4);

    env e5;
    calldataarg args5;
    f5(e5, args5);

    assert sharesToAmount(balanceOf(client)) <= depositedAmount();
}


definition isApprove(method g) returns bool = (
    g.selector == sig:approve(address,uint256).selector ||
    g.selector == sig:Asset.approve(address,uint256).selector
);


definition isApproveSuccessor(method g1, method g2) returns bool = (
    isApprove(g2) && !isApprove(g1)
);


definition isDeposit(method g) returns bool = g.selector == sig:deposit(uint256).selector;


definition depositAfterApproves(method g1, method g2) returns bool = (
    (isApprove(g1) && !isApprove(g2)) => isDeposit(g2)
);


definition depositFollowsApproves(method g1, method g2) returns bool = (
    !isApproveSuccessor(g1, g2) && depositAfterApproves(g1, g2)
);


rule sharesNeverGreaterThanAssets5Reduced(
    address client,
    method f1,
    method f2,
    method f3,
    method f4,
    method f5
) filtered {
    f1 -> !f1.isView && (isDeposit(f1) || isApprove(f1)),
    f2 -> !f2.isView,
    f3 -> !f3.isView,
    f4 -> !f4.isView,
    f5 -> !f5.isView
} {
    require depositFollowsApproves(f1, f2);
    require depositFollowsApproves(f2, f3);
    require depositFollowsApproves(f3, f4);
    require depositFollowsApproves(f4, f5);

    reset_storage currentContract;

    env e1;
    calldataarg args1;
    f1(e1, args1);

    env e2;
    calldataarg args2;
    f2(e2, args2);

    env e3;
    calldataarg args3;
    f3(e3, args3);

    env e4;
    calldataarg args4;
    f4(e4, args4);

    env e5;
    calldataarg args5;
    f5(e5, args5);

    assert sharesToAmount(balanceOf(client)) <= depositedAmount();
}
