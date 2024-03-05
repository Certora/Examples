
using Owner as owner;

methods{
    function getMyUint() external returns uint envfree;
    }

rule OwnerNeverChangedUsingLinking(env e, method f, calldataarg arg){
    address currentOwner;
    require currentOwner == owner;
    f(e, arg);
    assert currentOwner == owner;
}

rule OwnerNeverChangedUsingCalls(env e, method f, calldataarg arg){
    address currentOwner;
    require currentOwner == OWNER(e);
    f(e, arg);
    assert currentOwner == OWNER(e);
}

//proved but not related to reality
rule HavocProoved(env e){
    require MY_UINT(e) == 5;
    assert getMyUint() == 6;
}


// CRITICAL: [main] ERROR ALWAYS - Error in spec file (Immutable.spec:10:1): named pattern root 'MY_UINT' is not defined: did you spell something wrong? Note, named slots are only supported from solc 0.5.13 onward.
// CRITICAL: Encountered an error running Certora Prover:
// CVL specification syntax and type check failed

// ghost uint ghostUint256;

// hook Sload uint256 _MY_UINT currentContract.MY_UINT {
//     require ghostUint256 == _MY_UINT;
// }

// rule UintNeverChengedUsingGhost(env e, method f, calldataarg args){
//     uint256 currentGhost = ghostUint256;
//     f(e, args);
//     assert currentGhost == ghostUint256;
// }


// Immutable cant be accessed through the direct storage access
// rule DirectStorageAccess(env e){
//     assert currentContract.MY_UINT ==2;
// }