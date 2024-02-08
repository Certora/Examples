/***
This example explains many features of Certora Verification Language. 
See https://docs.certora.com for a complete guide.

Example for ecrecover 
***/

/*
    Declaration of methods that are used in the rules. envfree indicate that
    the method is not dependent on the environment (msg.value, msg.sender).
    Methods that are not declared here are assumed to be dependent on env.
*/


/*** # ecrecover properties:
# 1. zero value:
        ecrecover(0, v, r, s) == 0
# 2. deterministic 
        ecrecover(msgHash, v, r, s) == _addr on different calls.  
# 3. uniqueness of signature
        ecrecover(msgHash, v, r, s) != 0 => ecrecover(msgHash', v, r, s) == 0
        where msgHash' != msgHash
# 4. Dependency on r and s
        ecrecover(msgHash, v, r, s) != 0 => ecrecover(msgHash, v, r', s) == 0
        where r' != r
        ecrecover(msgHash, v, r, s) != 0 => ecrecover(msgHash, v, r, s') == 0
        where s' != s
**/



methods {
    function isSigned(address _addr, bytes32 msgHash, uint8 v, bytes32 r, bytes32 s) external returns (bool) envfree;
    function executeMyFunctionFromSignature(uint8 v, bytes32 r, bytes32 s, address owner, uint256 myParam, uint256 deadline) external;
    function getHash(address owner, uint256 myParam, uint256 deadline) external returns(bytes32) envfree;
}


function ecrecoverAxioms() {
  // zero value:
  require (forall uint8 v. forall bytes32 r. forall bytes32 s. ecrecover(to_bytes32(0), v, r, s) == 0);
  // uniqueness of signature
  require (forall uint8 v. forall bytes32 r. forall bytes32 s. forall bytes32 h1. forall bytes32 h2.
    h1 != h2 => ecrecover(h1, v, r, s) != 0 => ecrecover(h2, v, r, s) == 0);
  // dependency on r and s
  require (forall bytes32 h. forall uint8 v. forall bytes32 s. forall bytes32 r1. forall bytes32 r2.
    r1 != r2 => ecrecover(h, v, r1, s) != 0 => ecrecover(h, v, r2, s) == 0);
  require (forall bytes32 h. forall uint8 v. forall bytes32 r. forall bytes32 s1. forall bytes32 s2.
    s1 != s2 => ecrecover(h, v, r, s1) != 0 => ecrecover(h, v, r, s2) == 0);
}

/*
    shows that ecrecover has a single value, i.e two different addresses can not be the result of ecrecover(msgHash, v, r, s)  
*/
rule zeroValue() {
    ecrecoverAxioms();
    bytes32 msgHash; uint8 v; bytes32 r; bytes32 s; 
    assert ecrecover(to_bytes32(0), v, r, s ) == 0;
}




rule deterministic() {
    ecrecoverAxioms();
    bytes32 msgHash; uint8 v; bytes32 r; bytes32 s; 
    assert ecrecover(msgHash, v, r, s ) == ecrecover(msgHash, v, r, s );
}

rule uniqueness() {
    ecrecoverAxioms();
    bytes32 msgHashA; bytes32 msgHashB; uint8 v; bytes32 r; bytes32 s; 
    require msgHashA != msgHashB;  
    assert ecrecover(msgHashA, v, r, s) != 0 => ecrecover(msgHashB, v, r, s) == 0;
}

rule dependencyOnS() {
    ecrecoverAxioms();
    bytes32 msgHash;  uint8 v; bytes32 r; bytes32 s1; bytes32 s2; 
    require s1 != s2;  
    assert ecrecover(msgHash, v, r, s1) != 0 => ecrecover(msgHash, v, r, s2) == 0;
    //!= ecrecover(msgHash, v, r, s1) ;
}

rule dependencyOnR() {
    ecrecoverAxioms();
    bytes32 msgHash; uint8 v; bytes32 r1; bytes32 r2; bytes32 s; 
    require r1 != r2;  
    assert ecrecover(msgHash, v, r1, s) != 0 => ecrecover(msgHash, v, r2, s) == 0 ;
}

// Rules for a function that checks signature 

rule singleVerifier () 
{
    ecrecoverAxioms();
    bytes32 msgHash; uint8 v; bytes32 r; bytes32 s; 
    address addr1; 
    address addr2; 
    require addr1 != addr2 && addr1!=0 && addr2!=0 ;
    assert isSigned(addr1, msgHash, v, r, s ) => !isSigned(addr2, msgHash, v, r, s ) ;

}


rule ownerSignatureIsUnique () {
    ecrecoverAxioms();
    bytes32 msgHashA; bytes32 msgHashB;
    uint8 v; bytes32 r; bytes32 s; 
    address addr; 
    require msgHashA != msgHashB; 
    require addr != 0;
    assert isSigned(addr, msgHashA, v, r, s ) => !isSigned(addr, msgHashB, v, r, s );
}

rule hashIsUnique(
    address ownerA,
    uint256 myParamA,
    uint256 deadlineA,
    address ownerB,
    uint256 myParamB,
    uint256 deadlineB
) {
    bytes32 hashA =  getHash(ownerA, myParamA, deadlineA);
    bytes32 hashB = getHash(ownerB, myParamB, deadlineB);
    assert hashA == hashB => (  ownerA == ownerB && 
                                myParamA == myParamB &&
                                deadlineA == deadlineB ); 
}


/*** 
   # High level property : there is only single owner that can be used
    A rule which proves that for a given set of parameters only a single owner can execute .
    This property is implemented as a relational property - it compares two different executions on the same state.
*/
rule onlySingleUserCanExecute(uint8 v,
    bytes32 r,
    bytes32 s,
    address alice,
    address bob,
    uint256 myParam,
    uint256 deadline) {

    env e1;
    env e2;
    ecrecoverAxioms();
    //save the current state
    storage init = lastStorage; 
    //execute and assume succeeded
    executeMyFunctionFromSignature(e1, v, r, s, alice, myParam, deadline);
    satisfy true;
    // compare another execution on the same state, look at reverting paths
    executeMyFunctionFromSignature@withrevert(e2, v, r, s, bob, myParam, deadline) at init;
    bool success = !lastReverted;
    //if it succeeded it must be the same owner, or an unrealistic hash collision
    assert success => alice==bob ; 
}


/*** 
   # High level property : params and deadline are signed 
make sure the param and deadline are part of the signature 
*/
rule signedParamAndDeadline(uint8 v,
    bytes32 r,
    bytes32 s,
    address owner,
    uint256 myParamA,
    uint256 deadlineA,
    uint256 myParamB,
    uint256 deadlineB) {

    env e1;
    env e2;
    ecrecoverAxioms();
    //save the current state
    storage init = lastStorage; 
    //execute and assume succeeded
    executeMyFunctionFromSignature(e1, v, r, s, owner, myParamA, deadlineA);
    satisfy true;
    // compare another execution on the same state, look at reverting paths
    executeMyFunctionFromSignature@withrevert(e2, v, r, s, owner, myParamB, deadlineB) at init;
    bool success = !lastReverted;
    //if it succeeded it must be the same owner, or an unrealistic hash collision
    assert success => ( myParamA==myParamB && deadlineA == deadlineB); 
}


/***
 A signer can sign two different messages, in this case they have different signature 
**/
rule twoDifferent() {
    ecrecoverAxioms();
    bytes32 msgHashA;  uint8 vA; bytes32 rA; bytes32 sA; 
    bytes32 msgHashB;  uint8 vB; bytes32 rB; bytes32 sB;
    require  msgHashA != msgHashB;
    require ecrecover(msgHashA, vA, rA, sA) != 0 && ecrecover(msgHashB, vB, rB, sB) != 0;
    satisfy ecrecover(msgHashA, vA, rA, sA) == ecrecover(msgHashB, vB, rB, sB); 
    assert ecrecover(msgHashA, vA, rA, sA) == ecrecover(msgHashB, vB, rB, sB) =>
                    (rA != rB || sA != sB || vA != vB );
}

/**
Once a message is executed, it can not be executed again 
**/
rule signedMessagesExecutedOnce(uint8 v,
    bytes32 r,
    bytes32 s,
    address signer,
    uint256 myParam,
    uint256 deadline) {

    env e1;
    env e2;
    ecrecoverAxioms();
    //execute and assume succeeded
    executeMyFunctionFromSignature(e1, v, r, s, signer, myParam, deadline);
    satisfy true;
    //attemp to execute again, on a possible different env
    executeMyFunctionFromSignature@withrevert(e2, v, r, s, signer, myParam, deadline);
    bool reverted = lastReverted;
    assert reverted ; 
}