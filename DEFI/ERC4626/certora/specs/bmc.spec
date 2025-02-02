/* Bounded model checking example spec
 *
 * NOTE. In this spec we only reset the storage of the main contract.
 * NOTE: without sanity `vaultSolvency3` runs MUCH faster (16 minutes) and without any
 * issues.
 * NOTE: the resulting `treeview` files are overly large, causing issues with rendering
 * and timeouts in the back-end when trying to enter the results into the database.
 *
 * Runs:
 * https://prover.certora.com/output/98279/c85563ebbe2042b6bb0ba43128374cba?anonymousKey=0fa8f2c9e441dcacf7c90fd8410fa1774938cebd
 * `vaultSolvency3`:
 *  https://prover.certora.com/output/98279/aa5aa6b1ead14e91ba20fb4c86908708?anonymousKey=81658c45624a22d8e9e24a107efc57a8f819a61a
 * `vaultSolvency3` only `ERC4626AccountingHarness` as parametric contract:
 *  https://prover.certora.com/output/98279/3080276246e0459c894f155322169003?anonymousKey=3c763b1352763f7bd22143d3bb38cb7012238cfe
 * `vaultSolvency3` no sanity:
 *  https://prover.certora.com/output/98279/3080276246e0459c894f155322169003?anonymousKey=3c763b1352763f7bd22143d3bb38cb7012238cfe
 */


using DummyERC20A as asset;

methods {
    function totalAssets() external returns (uint256) envfree;
    function totalSupply() external returns (uint256) envfree;
    function userAssets(address) external returns (uint256) envfree;

    function DummyERC20A.totalSupply() external returns (uint256) envfree;
}


/// @title Solvency condition for the vault
definition isVaultSolvent() returns bool = (
    totalAssets() >= totalSupply() && userAssets(currentContract) >= totalAssets()
);



/// @title Step 0 of checking vault solvency
/// @notice The solvency check is done after `reset_storage`, however
/// *this is not* the same as calling the constructor - which is what we need.
/// @notice We only reset the storage of the current contract
rule vaultSolvency0() {
    reset_storage currentContract;
    assert isVaultSolvent();
}


/// @title Step 1 of checking vault solvency - single function call
/// @notice We only reset the storage of the current contract
rule vaultSolvency1(method f) {
    reset_storage currentContract;
    require isVaultSolvent();  // This is supposed to help the Prover
    require userAssets(currentContract) == 0;  // TODO: justify

    env e;
    calldataarg args;
    f(e, args);

    assert isVaultSolvent();
}


/// @title Step 2 of checking vault solvency
/// @notice Two methods seems to be enough to catch some mutations, given that
/// we *only reset the storage of the current contract*
rule vaultSolvency2(method f1, method f2) {
    reset_storage currentContract;
    require isVaultSolvent();
    require userAssets(currentContract) == 0;

    env e1;
    calldataarg args1;
    f1(e1, args1);
    require isVaultSolvent();

    env e2;
    require e2.msg.sender != currentContract;  // TODO: justify
    calldataarg args2;
    f2(e2, args2);

    assert isVaultSolvent();
}


/// @title Step 3 of checking vault solvency
rule vaultSolvency3(method f1, method f2, method f3) filtered {
    f1 -> !f1.isView,
    f2 -> !f2.isView,
    f3 -> !f3.isView
} {
    reset_storage currentContract;
    require isVaultSolvent();
    require userAssets(currentContract) == 0;
    require forall address spender. asset.a[currentContract][spender] == 0;
    require (
        f1.contract == currentContract || 
        f2.contract == currentContract || 
        f3.contract == currentContract
    );

    env e1;
    require e1.msg.sender != currentContract;  // TODO: justify
    calldataarg args1;
    f1(e1, args1);
    require isVaultSolvent();

    env e2;
    require e2.msg.sender != currentContract;  // TODO: justify
    calldataarg args2;
    f2(e2, args2);
    require isVaultSolvent();

    env e3;
    require e3.msg.sender != currentContract;  // TODO: justify
    calldataarg args3;
    f3(e3, args3);

    assert isVaultSolvent();
}


// ---- Parametric rules (bounded) ---------------------------------------------

/// @title Total supply increases/decreases iff total assets changes similarly
/// @notice Single method call, resetting the storage of the main contract only
rule totalsMonotonicity1(method f) {
    reset_storage currentContract;

    uint256 totalSupplyBefore = totalSupply();
    uint256 totalAssetsBefore = totalAssets();
    
    env e;
    require e.msg.sender != currentContract; 
    calldataarg args;
    f(e, args);

    uint256 totalSupplyAfter = totalSupply();
    uint256 totalAssetsAfter = totalAssets();
    
    assert totalSupplyBefore < totalSupplyAfter <=> totalAssetsBefore < totalAssetsAfter;
    assert totalSupplyAfter == totalSupplyBefore => totalAssetsBefore == totalAssetsAfter;
}


/// @title Total supply increases/decreases iff total assets changes similarly - 3 steps
/// @notice Three method calls, resetting the storage of the main contract only
rule totalsMonotonicity3(method f1, method f2, method f3) filtered {
    f1 -> !f1.isView,
    f2 -> !f2.isView,
    f3 -> !f3.isView
} {
    reset_storage currentContract;

    env e1;
    require e1.msg.sender != currentContract;  // TODO: justify
    calldataarg args1;
    f1(e1, args1);

    env e2;
    require e2.msg.sender != currentContract;  // TODO: justify
    calldataarg args2;
    f2(e2, args2);

    uint256 totalSupplyBefore = totalSupply();
    uint256 totalAssetsBefore = totalAssets();

    env e3;
    require e3.msg.sender != currentContract;  // TODO: justify
    calldataarg args3;
    f3(e3, args3);

    uint256 totalSupplyAfter = totalSupply();
    uint256 totalAssetsAfter = totalAssets();
    
    assert totalSupplyBefore < totalSupplyAfter <=> totalAssetsBefore < totalAssetsAfter;
    assert totalSupplyAfter == totalSupplyBefore => totalAssetsBefore == totalAssetsAfter;
}
