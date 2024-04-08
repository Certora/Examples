using Owner as owner;

// Access private immutable via linking (variable must be referenced in the code!)
rule ownerNeverChangedUsingLinking(env e, method f, calldataarg arg){
    address currentOwner;
    require currentOwner == owner;
    f(e, arg);
    assert currentOwner == owner;
}

// Access private immutable via direct storage access (variable must be referenced in the code!)
rule ownerNeverChangedUsingDirectStorageAccess(env e){
    method f;
    calldataarg args;
    
    address directOwner = currentContract.OWNER;

    f(e, args);

    assert directOwner == currentContract.OWNER;
}

// Access public immutable via direct storage access
rule uintNeverChangedDirectStorageAccess(env e){
    method f;
    calldataarg args;

    uint256 myUint = currentContract.MY_UINT;

    f(e, args);

    assert myUint == currentContract.MY_UINT;
}

// Access public immutable via getter
rule uintNeverChangedGetter(env e){
    method f;
    calldataarg args;

    uint256 myUint = currentContract.MY_UINT(e);

    f(e, args);

    assert myUint == currentContract.MY_UINT(e);
}