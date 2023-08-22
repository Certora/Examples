/*
    This is a specification file for the verification of AaveTokenV3.sol 
    smart contract using the Certora prover. The rules in this spec have been
    contributed by the community. Individual attribution is given in the comments
    to each rule.

    For more information, visit: https://www.certora.com/

    This file is run with scripts/verifyCommunity.sh
    On AaveTokenV3Harness.sol

    Run results: https://prover.certora.com/output/67509/d36b2357623beec546c1?anonymousKey=f6fb866df18e6bc9ed880806375e7861cde8274f

*/

import "base.spec";

methods {
    function ecrecoverWrapper(bytes32, uint8, bytes32, bytes32) external returns (address) envfree;
    function computeMetaDelegateHash(address delegator,  address delegatee, uint256 deadline, uint256 nonce) external returns (bytes32) envfree;
    function computeMetaDelegateByTypeHash(address delegator,  address delegatee, AaveTokenV3Harness.GovernancePowerType delegationType, uint256 deadline, uint256 nonce) external returns (bytes32) envfree;
    function _nonces(address addr) external returns (uint256) envfree;
    function getNonce(address) external returns (uint256) envfree;
}

definition ZERO_ADDRESS() returns address = 0;


/*
    @Rule

    @Description:
    Integrity of permit function
    Successful permit function increases the nonce of owner by 1 and also changes the allowance of owner to spender

    @Formula:
    {
        nonceBefore = getNonce(owner)
    }
    <
        permit(owner, spender, value, deadline, v, r, s)
    >
    {
        allowance(owner, spender) == value && getNonce(owner) == nonceBefore + 1
    }

    @Note:
        Written by https://github.com/parth-15

    @Link:
*/
rule permitIntegrity() {
    env e;
    address owner;
    address spender;
    uint256 value;
    uint256 deadline;
    uint8 v;
    bytes32 r;
    bytes32 s;

    uint256 allowanceBefore = allowance(owner, spender);
    mathint nonceBefore = getNonce(owner);

    //checking this because function is using unchecked math and such a high nonce is unrealistic
    require nonceBefore < max_uint;

    permit(e, owner, spender, value, deadline, v, r, s);

    uint256 allowanceAfter = allowance(owner, spender);
    mathint nonceAfter = getNonce(owner);

    assert allowanceAfter == value, "permit increases allowance of owner to spender on success";
    assert nonceAfter == nonceBefore + 1, "successful call to permit function increases nonce of owner by 1";
}


/*
    @Rule

    @Description:
        Address 0 has no voting or proposition power

    @Formula:
    {
        getPowerCurrent(0, VOTING_POWER) == 0 && getPowerCurrent(0, PROPOSITION_POWER) == && balanceOf(0) == 0
    }

    @Note:
        Written by https://github.com/JayP11

    @Link:
*/
invariant addressZeroNoPower()
  getPowerCurrent(0, VOTING_POWER()) == 0 && getPowerCurrent(0, PROPOSITION_POWER()) == 0 && balanceOf(0) == 0;


/*
    @Rule

    @Description:
        Verify that `metaDelegateByType` can only be called with a signed request.

    @Formula:
    {
        ecrecover(v,r,s) != delegator
    }
    <
        metaDelegateByType@withrevert(delegator, delegatee, delegationType, deadline, v, r, s)
    >
    {
        lastReverted == true
    }

    @Note:
        Written by https://github.com/kustosz

    @Link:
*/
rule metaDelegateByTypeOnlyCallableWithProperlySignedArguments(env e, address delegator, address delegatee, AaveTokenV3Harness.GovernancePowerType delegationType, uint256 deadline, uint8 v, bytes32 r, bytes32 s) {
    require ecrecoverWrapper(computeMetaDelegateByTypeHash(delegator, delegatee, delegationType, deadline, _nonces(delegator)), v, r, s) != delegator;
    metaDelegateByType@withrevert(e, delegator, delegatee, delegationType, deadline, v, r, s);
    assert lastReverted;
}

 /*
    @Rule

    @Description:
        Verify that it's impossible to use the same arguments to call `metaDalegate` twice.

    @Formula:
    {
        hash1 = computeMetaDelegateHash(delegator, delegatee, deadline, nonce)
        hash2 = computeMetaDelegateHash(delegator, delegatee, deadline, nonce + 1)
        ecrecover(hash1, v, r, s) == delegator
    }
    <
        metaDelegate(e1, delegator, delegatee, v, r, s)
        metaDelegate@withrevert(e2, delegator, delegatee, delegationType, deadline, v, r, s)
    >
    {
        lastReverted == true
    }

    @Note:
        Written by https://github.com/kustosz

    @Link:
*/
rule metaDelegateNonRepeatable(env e1, env e2, address delegator, address delegatee, uint256 deadline, uint8 v, bytes32 r, bytes32 s) {
    uint256 nonce = _nonces(delegator);
    bytes32 hash1 = computeMetaDelegateHash(delegator, delegatee, deadline, nonce);
    bytes32 hash2 = computeMetaDelegateHash(delegator, delegatee, deadline, require_uint256(nonce+1));
    // assume no hash collisions
    require hash1 != hash2;
    // assume first call is properly signed
    require ecrecoverWrapper(hash1, v, r, s) == delegator;
    // assume ecrecover is sane: cannot sign two different messages with the same (v,r,s)
    require ecrecoverWrapper(hash2, v, r, s) != ecrecoverWrapper(hash1, v, r, s);
    metaDelegate(e1, delegator, delegatee, deadline, v, r, s);
    metaDelegate@withrevert(e2, delegator, delegatee, deadline, v, r, s);
    assert lastReverted;
}


/*
    @Rule

    @Description:
        Power of the previous delegate is removed when the delegatee delegates to another delegate

    @Formula:
    {
        _votingBalance = getDelegatedVotingBalance(alice)
    }
    <
        delegateByType(alice, VOTING_POWER)
        delegateByType(bob, VOTING_POWER)
    >
    {
        alice != bob => getDelegatedVotingBalance(alice) == _votingBalance
    }

    @Note:
        Written by https://github.com/priyankabhanderi

    @Link:
*/
rule delegatingToAnotherUserRemovesPowerFromOldDelegatee(env e, address alice, address bob) {

    require e.msg.sender != ZERO_ADDRESS(); 
    require e.msg.sender != alice && e.msg.sender != bob;
    require alice != ZERO_ADDRESS() && bob != ZERO_ADDRESS();

    require getVotingDelegate(e.msg.sender) != alice;

    uint72 _votingBalance = getDelegatedVotingBalance(alice);

    delegateByType(e, alice, VOTING_POWER());

    assert getVotingDelegate(e.msg.sender) == alice;

    delegateByType(e, bob, VOTING_POWER());

    assert getVotingDelegate(e.msg.sender) == bob;
    uint72 votingBalance_ = getDelegatedVotingBalance(alice);
    assert alice != bob => votingBalance_ == _votingBalance;
}

/*
    @Rule

    @Description:
        Voting and proposition power change only as a result of specific functions

    @Formula:
    {
        powerBefore = getPowerCurrent(alice, type)
    }
    <
        f(e, args)
    >
    {
       powerAfter = getPowerCurrent(alice, type)
       powerAfter != powerBefore =>
        f.selector == sig:delegate(address).selector ||
        f.selector == sig:delegateByType(address, uint8).selector ||
        f.selector == sig:metaDelegate(address, address, uint256, uint8, bytes32, bytes32).selector ||
        f.selector == sig:metaDelegateByType(address, address, uint8, uint256, uint8, bytes32, bytes32).selector ||
        f.selector == sig:transfer(address, uint256).selector ||
        f.selector == sig:transferFrom(address, address, uint256).selector
    }

    @Note:
        Written by https://github.com/top-sekret

    @Link:
*/

rule powerChanges(address alice, method f) {
    env e;
    calldataarg args;

    AaveTokenV3Harness.GovernancePowerType type;
    uint256 powerBefore = getPowerCurrent(alice, type);

    f(e, args);

    uint256 powerAfter = getPowerCurrent(alice, type);

    assert powerBefore != powerAfter =>
        f.selector == sig:delegate(address).selector ||
        f.selector == sig:delegateByType(address, AaveTokenV3Harness.GovernancePowerType).selector ||
        f.selector == sig:metaDelegate(address, address, uint256, uint8, bytes32, bytes32).selector ||
        f.selector == sig:metaDelegateByType(address, address, AaveTokenV3Harness.GovernancePowerType, uint256, uint8, bytes32, bytes32).selector ||
        f.selector == sig:transfer(address, uint256).selector ||
        f.selector == sig:transferFrom(address, address, uint256).selector;
}



/*
    @Rule

    @Description:
        Changing a delegate of one type doesn't influence the delegate of the other type

    @Formula:
    {
        delegateBefore = type == 1 ? getPropositionDelegate(e.msg.sender) : getVotingDelegate(e.msg.sender)
    }
    <
        delegateByType(e, delegatee, 1 - type)
    >
    {
       delegateBefore = type == 1 ? getPropositionDelegate(e.msg.sender) : getVotingDelegate(e.msg.sender)
       delegateBefore == delegateAfter
    }

    @Note:
        Written by https://github.com/top-sekret

    @Link:
*/
rule delegateIndependence(method f) {
    env e;

    AaveTokenV3Harness.GovernancePowerType type;

    address delegateBefore = type == AaveTokenV3Harness.GovernancePowerType.PROPOSITION ? getPropositionDelegate(e.msg.sender) : getVotingDelegate(e.msg.sender);

    AaveTokenV3Harness.GovernancePowerType otherType = type == AaveTokenV3Harness.GovernancePowerType.PROPOSITION ? AaveTokenV3Harness.GovernancePowerType.VOTING : AaveTokenV3Harness.GovernancePowerType.PROPOSITION;
    delegateByType(e, _, otherType);

    address delegateAfter = type == AaveTokenV3Harness.GovernancePowerType.PROPOSITION ? getPropositionDelegate(e.msg.sender) : getVotingDelegate(e.msg.sender);

    assert delegateBefore == delegateAfter;
}

/*
    @Rule

    @Description:
        Verifying voting power increases/decreases while not being a voting delegatee yourself

    @Formula:
    {
        votingPowerBefore = getPowerCurrent(a, VOTING_POWER)
        balanceBefore = balanceOf(a)
        isVotingDelegatorBefore = getDelegatingVoting(a)
        isVotingDelegateeBefore = getDelegatedVotingBalance(a) != 0
    }
    <
        f(e, args)
    >
    {
        votingPowerAfter = getPowerCurrent(a, VOTING_POWER()
        balanceAfter = getBalance(a)
        isVotingDelegatorAfter = getDelegatingVoting(a);
        isVotingDelegateeAfter = getDelegatedVotingBalance(a) != 0

        votingPowerBefore < votingPowerAfter <=> 
        (!isVotingDelegatorBefore && !isVotingDelegatorAfter && (balanceBefore < balanceAfter)) ||
        (isVotingDelegatorBefore && !isVotingDelegatorAfter && (balanceBefore != 0))
        &&
        votingPowerBefore > votingPowerAfter <=> 
        (!isVotingDelegatorBefore && !isVotingDelegatorAfter && (balanceBefore > balanceAfter)) ||
        (!isVotingDelegatorBefore && isVotingDelegatorAfter && (balanceBefore != 0))
    }

    @Note:
        Written by https://github.com/Zarfsec

    @Link:
*/
rule votingPowerChangesWhileNotBeingADelegatee(address a) {
    require a != 0;

    uint256 votingPowerBefore = getPowerCurrent(a, VOTING_POWER());
    uint256 balanceBefore = getBalance(a);
    bool isVotingDelegatorBefore = getDelegatingVoting(a);
    bool isVotingDelegateeBefore = getDelegatedVotingBalance(a) != 0;

    method f;
    env e;
    calldataarg args;
    f(e, args);

    uint256 votingPowerAfter = getPowerCurrent(a, VOTING_POWER());
    uint256 balanceAfter = getBalance(a);
    bool isVotingDelegatorAfter = getDelegatingVoting(a);
    bool isVotingDelegateeAfter = getDelegatedVotingBalance(a) != 0;

    require !isVotingDelegateeBefore && !isVotingDelegateeAfter;

    /* 
    If you're not a delegatee, your voting power only increases when
        1. You're not delegating and your balance increases
        2. You're delegating and stop delegating and your balanceBefore != 0
    */
    assert votingPowerBefore < votingPowerAfter <=> 
        (!isVotingDelegatorBefore && !isVotingDelegatorAfter && (balanceBefore < balanceAfter)) ||
        (isVotingDelegatorBefore && !isVotingDelegatorAfter && (balanceBefore != 0));

    /*
    If you're not a delegatee, your voting power only decreases when
        1. You're not delegating and your balance decreases
        2. You're not delegating and start delegating and your balanceBefore != 0
    */
    assert votingPowerBefore > votingPowerAfter <=> 
        (!isVotingDelegatorBefore && !isVotingDelegatorAfter && (balanceBefore > balanceAfter)) ||
        (!isVotingDelegatorBefore && isVotingDelegatorAfter && (balanceBefore != 0));
}

/*
    @Rule

    @Description:
        Verifying proposition power increases/decreases while not being a proposition delegatee yourself

    @Formula:
    {
        propositionPowerBefore = getPowerCurrent(a, PROPOSITION_POWER)
        balanceBefore = balanceOf(a)
        isPropositionDelegatorBefore = getDelegatingProposition(a)
        isPropositionDelegateeBefore = getDelegatedPropositionBalance(a) != 0
    }
    <
        f(e, args)
    >
    {
        propositionPowerAfter = getPowerCurrent(a, PROPOSITION_POWER()
        balanceAfter = getBalance(a)
        isPropositionDelegatorAfter = getDelegatingProposition(a);
        isPropositionDelegateeAfter = getDelegatedPropositionBalance(a) != 0

        propositionPowerBefore < propositionPowerAfter <=> 
        (!isPropositionDelegatorBefore && !isPropositionDelegatorAfter && (balanceBefore < balanceAfter)) ||
        (isPropositionDelegatorBefore && !isPropositionDelegatorAfter && (balanceBefore != 0))
        &&
        propositionPowerBefore > propositionPowerAfter <=> 
        (!isPropositionDelegatorBefore && !isPropositionDelegatorAfter && (balanceBefore > balanceAfter)) ||
        (!isPropositionDelegatorBefore && isPropositionDelegatorAfter && (balanceBefore != 0))
    }

    @Note:
        Written by https://github.com/Zarfsec

    @Link:
*/
rule propositionPowerChangesWhileNotBeingADelegatee(address a) {
    require a != 0;

    uint256 propositionPowerBefore = getPowerCurrent(a, PROPOSITION_POWER());
    uint256 balanceBefore = getBalance(a);
    bool isPropositionDelegatorBefore = getDelegatingProposition(a);
    bool isPropositionDelegateeBefore = getDelegatedPropositionBalance(a) != 0;

    method f;
    env e;
    calldataarg args;
    f(e, args);

    uint256 propositionPowerAfter = getPowerCurrent(a, PROPOSITION_POWER());
    uint256 balanceAfter = getBalance(a);
    bool isPropositionDelegatorAfter = getDelegatingProposition(a);
    bool isPropositionDelegateeAfter = getDelegatedPropositionBalance(a) != 0;

    require !isPropositionDelegateeBefore && !isPropositionDelegateeAfter;

    /*
    If you're not a delegatee, your proposition power only increases when
        1. You're not delegating and your balance increases
        2. You're delegating and stop delegating and your balanceBefore != 0
    */
    assert propositionPowerBefore < propositionPowerAfter <=> 
        (!isPropositionDelegatorBefore && !isPropositionDelegatorAfter && (balanceBefore < balanceAfter)) ||
        (isPropositionDelegatorBefore && !isPropositionDelegatorAfter && (balanceBefore != 0));
    
    /*
    If you're not a delegatee, your proposition power only decreases when
        1. You're not delegating and your balance decreases
        2. You're not delegating and start delegating and your balanceBefore != 0
    */
    assert propositionPowerBefore > propositionPowerAfter <=> 
        (!isPropositionDelegatorBefore && !isPropositionDelegatorBefore && (balanceBefore > balanceAfter)) ||
        (!isPropositionDelegatorBefore && isPropositionDelegatorAfter && (balanceBefore != 0));
}

/*
    @Rule

    @Description:
        Allowance only changes as a result of specific subset of functions

    @Formula:
    {
        allowanceBefore = allowance(owner, spender)
    }
    <
        f(e, args)
    >
    {
       allowance(owner, spender) != allowanceBefore =>f.selector==sig:approve(address,uint256).selector 
            || f.selector==sig:increaseAllowance(address,uint256).selector
            || f.selector==sig:decreaseAllowance(address,uint256).selector
            || f.selector==sig:transferFrom(address,address,uint256).selector
            || f.selector==sig:permit(address,address,uint256,uint256,uint8,bytes32,bytes32).selector

    }

    @Note:
        Written by https://github.com/oracleorb

    @Link:
*/
rule allowanceStateChange(env e){
    address owner;
    address user;
    method f;
    calldataarg args;

    uint256 allowanceBefore=allowance(owner,user);
    f(e, args);
    uint256 allowanceAfter=allowance(owner,user);

    assert allowanceBefore!=allowanceAfter => f.selector==sig:approve(address,uint256).selector 
    || f.selector==sig:increaseAllowance(address,uint256).selector
    || f.selector==sig:decreaseAllowance(address,uint256).selector
    || f.selector==sig:transferFrom(address,address,uint256).selector
    || f.selector==sig:permit(address,address,uint256,uint256,uint8,bytes32,bytes32).selector;
}
