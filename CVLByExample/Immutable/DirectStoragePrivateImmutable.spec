
rule DirectStorageAccess(env e){
    method f;
    calldataarg args;
    
    address directOwner = currentContract.OWNER;

    f(e, args);

    assert directOwner == currentContract.OWNER;
}
