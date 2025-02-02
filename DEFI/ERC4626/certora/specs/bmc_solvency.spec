/* Bounded model checking example spec
 *
 * NOTE. In this spec we only reset all contracts' storage.
 */

using DummyERC20A as asset;

methods {
    function totalAssets() external returns (uint256) envfree;
    function totalSupply() external returns (uint256) envfree;
    function userAssets(address) external returns (uint256) envfree;

    function DummyERC20A.totalSupply() external returns (uint256) envfree;
}


/// @title Allowed functions - to reduce the load on the prover
definition isAllowed(method f) returns bool = (
    // Exclude `transferFrom`, `approve` and `permit` from current contract
    // Also, the getters for `name` and `symbol` are not considered as view, perhaps
    // because they are strings?
    (
        f.contract == asset &&
        f.selector != sig:DummyERC20A.transferFrom(address,address,uint256).selector &&
        f.selector != sig:DummyERC20A.name().selector &&
        f.selector != sig:DummyERC20A.symbol().selector
    ) ||
    f.contract == currentContract &&
    f.selector != sig:transferFrom(address,address,uint256).selector &&
    f.selector != sig:approve(address,uint256).selector &&
    f.selector != sig:permit(address,address,uint256,uint256,uint8,bytes32,bytes32).selector &&
    f.selector != sig:DummyERC20A.name().selector &&
    f.selector != sig:DummyERC20A.symbol().selector
);


/// @title Solvency condition for the vault
definition isVaultSolvent() returns bool = (
    totalAssets() >= totalSupply() && userAssets(currentContract) >= totalAssets()
);


/// @title Step 0 of checking vault solvency
/// @notice The solvency check is done after `reset_storage`, however
/// *this is not* the same as calling the constructor - which is what we need.
rule vaultSolvency0() {
    reset_storage currentContract;
    reset_storage asset;
    assert isVaultSolvent();
}


/// @title Checking vault solvency - three function calls
rule vaultSolvency3(method f1, method f2, method f3) filtered {
    f1 -> !f1.isView && f1.contract == asset,  // First call to asset (deposit)
    f2 -> !f2.isView,
    f3 -> !f3.isView
} {
    reset_storage currentContract;
    reset_storage asset;
    require isVaultSolvent();  // This is supposed to help the Prover
    require userAssets(currentContract) == 0;

    env e1;
    require e1.msg.sender != currentContract;  // TODO: justify
    calldataarg args1;
    f1(e1, args1);
    require isVaultSolvent();  // Supposed to help the Prover

    env e2;
    require e2.msg.sender != currentContract;  // TODO: justify
    calldataarg args2;
    f2(e2, args2);
    require isVaultSolvent();  // Supposed to help the Prover

    env e3;
    require e3.msg.sender != currentContract;  // TODO: justify
    calldataarg args3;
    f3(e3, args3);

    assert isVaultSolvent();
}


/// @title Checking vault solvency - four function calls
rule vaultSolvency4(method f1, method f2, method f3, method f4) filtered {
    f1 -> !f1.isView && f1.selector == sig:asset.deposit().selector ,  // First call to asset (deposit)
    f2 -> !f2.isView && isAllowed(f2),
    f3 -> !f3.isView && isAllowed(f3),
    f4 -> !f4.isView && isAllowed(f4) && f4.contract == currentContract
} {
    reset_storage currentContract;
    reset_storage asset;
    require isVaultSolvent();  // This is supposed to help the Prover
    require userAssets(currentContract) == 0;

    env e1;
    require e1.msg.sender != currentContract;  // TODO: justify
    calldataarg args1;
    f1(e1, args1);
    require isVaultSolvent();  // Supposed to help the Prover

    env e2;
    require e2.msg.sender != currentContract;  // TODO: justify
    calldataarg args2;
    f2(e2, args2);
    require isVaultSolvent();  // Supposed to help the Prover

    env e3;
    require e3.msg.sender != currentContract;  // TODO: justify
    calldataarg args3;
    f3(e3, args3);
    require isVaultSolvent();  // Supposed to help the Prover

    env e4;
    require e4.msg.sender != currentContract;  // TODO: justify
    calldataarg args4;
    f4(e4, args4);

    assert isVaultSolvent();
}


/// @title Checking vault solvency - four function calls
rule vaultSolvency5(method f1, method f2, method f3, method f4, method f5) filtered {
    f1 -> !f1.isView && f1.selector == sig:asset.deposit().selector,  // First call to asset (deposit)
    f2 -> !f2.isView && isAllowed(f2),
    f3 -> !f3.isView && isAllowed(f3),
    f4 -> !f4.isView && isAllowed(f4),
    f5 -> !f5.isView && isAllowed(f5) && f5.contract == currentContract
} {
    reset_storage currentContract;
    reset_storage asset;
    require isVaultSolvent();  // This is supposed to help the Prover
    require userAssets(currentContract) == 0;

    env e1;
    require e1.msg.sender != currentContract;  // TODO: justify
    calldataarg args1;
    f1(e1, args1);
    require isVaultSolvent();  // Supposed to help the Prover

    env e2;
    require e2.msg.sender != currentContract;  // TODO: justify
    calldataarg args2;
    f2(e2, args2);
    require isVaultSolvent();  // Supposed to help the Prover

    env e3;
    require e3.msg.sender != currentContract;  // TODO: justify
    calldataarg args3;
    f3(e3, args3);
    require isVaultSolvent();  // Supposed to help the Prover

    env e4;
    require e4.msg.sender != currentContract;  // TODO: justify
    calldataarg args4;
    f4(e4, args4);
    require isVaultSolvent();  // Supposed to help the Prover

    env e5;
    require e5.msg.sender != currentContract;  // TODO: justify
    calldataarg args5;
    f5(e5, args5);
    assert isVaultSolvent();
}
