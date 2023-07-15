/*
    This is a base spec file that includes methods declarations, definitions
    and functions to be included in other spec. There are no rules in this file.
    For more information, visit: https://www.certora.com/

*/

/*

    Declaration of methods of the Aave token contract (and harness)

*/ 

methods {
    function totalSupply()                         external returns (uint256)   envfree;
    function balanceOf(address)                    external returns (uint256)   envfree;
    function allowance(address,address)            external returns (uint256)   envfree;
    function increaseAllowance(address, uint256) external;
    function decreaseAllowance(address, uint256) external;
    function transfer(address,uint256) external;
    function transferFrom(address,address,uint256) external;
    function permit(address,address,uint256,uint256,uint8,bytes32,bytes32) external;

    function delegate(address delegatee) external;
    function metaDelegate(address,address,uint256,uint8,bytes32,bytes32) external;
    function metaDelegateByType(address,address,uint8,uint256,uint8,bytes32,bytes32) external;
    function getPowerCurrent(address, AaveTokenV3Harness.GovernancePowerType) external returns (uint256) envfree;

    function getBalance(address user) external returns (uint104) envfree;
    function getDelegatedPropositionBalance(address user) external returns (uint72) envfree;
    function getDelegatedVotingBalance(address user) external returns (uint72) envfree;
    function getDelegatingProposition(address user) external returns (bool) envfree;
    function getDelegatingVoting(address user) external returns (bool) envfree;
    function getVotingDelegate(address user) external returns (address) envfree;
    function getPropositionDelegate(address user) external returns (address) envfree;
    function getDelegationState(address user) external returns (AaveTokenV3Harness.DelegationState) envfree;
}

definition VOTING_POWER() returns AaveTokenV3Harness.GovernancePowerType = AaveTokenV3Harness.GovernancePowerType.VOTING;
definition PROPOSITION_POWER() returns AaveTokenV3Harness.GovernancePowerType = AaveTokenV3Harness.GovernancePowerType.PROPOSITION;
definition DELEGATED_POWER_DIVIDER() returns uint256 = 10^10;

/**

    Definitions of delegation states

*/
definition NO_DELEGATION() returns AaveTokenV3Harness.DelegationState = AaveTokenV3Harness.DelegationState.NO_DELEGATION;
definition VOTING_DELEGATED() returns AaveTokenV3Harness.DelegationState = AaveTokenV3Harness.DelegationState.VOTING_DELEGATED;
definition PROPOSITION_DELEGATED() returns AaveTokenV3Harness.DelegationState = AaveTokenV3Harness.DelegationState.PROPOSITION_DELEGATED;
definition FULL_POWER_DELEGATED() returns AaveTokenV3Harness.DelegationState = AaveTokenV3Harness.DelegationState.FULL_POWER_DELEGATED;
definition DELEGATING_VOTING(AaveTokenV3Harness.DelegationState state) returns bool = 
    state == VOTING_DELEGATED() || state == FULL_POWER_DELEGATED();
definition DELEGATING_PROPOSITION(AaveTokenV3Harness.DelegationState state) returns bool =
    state == PROPOSITION_DELEGATED() || state == FULL_POWER_DELEGATED();

definition AAVE_MAX_SUPPLY() returns uint256 = 16000000 * 10^18;
definition SCALED_MAX_SUPPLY() returns mathint = AAVE_MAX_SUPPLY() / DELEGATED_POWER_DIVIDER();


/**

    Functions

*/

function normalize(uint256 amount) returns mathint {
    return amount / DELEGATED_POWER_DIVIDER() * DELEGATED_POWER_DIVIDER();
}

function validDelegationState(address user) returns bool {
    AaveTokenV3Harness.DelegationState state = getDelegationState(user);
    return state == AaveTokenV3Harness.DelegationState.NO_DELEGATION ||
        state == AaveTokenV3Harness.DelegationState.VOTING_DELEGATED ||
        state == AaveTokenV3Harness.DelegationState.PROPOSITION_DELEGATED ||
        state == AaveTokenV3Harness.DelegationState.FULL_POWER_DELEGATED;
}

function validAmount(uint256 amt) returns bool {
    return amt < AAVE_MAX_SUPPLY();
}
