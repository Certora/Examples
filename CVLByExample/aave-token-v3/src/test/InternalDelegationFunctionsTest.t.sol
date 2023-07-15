// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {Strings} from '../../lib/openzeppelin-contracts/contracts/utils/Strings.sol';
import {IERC20Metadata} from '../../lib/openzeppelin-contracts/contracts/token/ERC20/extensions/IERC20Metadata.sol';
import {AaveTokenV3} from '../AaveTokenV3.sol';

import {AaveUtils, console} from './utils/AaveUtils.sol';

contract StorageTest is AaveTokenV3, AaveUtils {
  function setUp() public {}

  function testFor_getDelegatedPowerByType() public {
    DelegationAwareBalance memory userState;
    userState.delegatedPropositionBalance = 100;
    userState.delegatedVotingBalance = 200;
    assertEq(
      _getDelegatedPowerByType(userState, GovernancePowerType.VOTING),
      userState.delegatedVotingBalance * POWER_SCALE_FACTOR
    );
    assertEq(
      _getDelegatedPowerByType(userState, GovernancePowerType.PROPOSITION),
      userState.delegatedPropositionBalance * POWER_SCALE_FACTOR
    );
  }

  function testFor_getDelegateeByType() public {
    address user = address(0x1);
    address user2 = address(0x2);
    address user3 = address(0x3);
    DelegationAwareBalance memory userState;

    _votingDelegateeV2[user] = address(user2);
    _propositionDelegateeV2[user] = address(user3);

    userState.delegationState = DelegationState.VOTING_DELEGATED;
    assertEq(_getDelegateeByType(user, userState, GovernancePowerType.VOTING), user2);
    assertEq(_getDelegateeByType(user, userState, GovernancePowerType.PROPOSITION), address(0));

    userState.delegationState = DelegationState.PROPOSITION_DELEGATED;
    assertEq(_getDelegateeByType(user, userState, GovernancePowerType.VOTING), address(0));
    assertEq(_getDelegateeByType(user, userState, GovernancePowerType.PROPOSITION), user3);

    userState.delegationState = DelegationState.FULL_POWER_DELEGATED;
    assertEq(_getDelegateeByType(user, userState, GovernancePowerType.VOTING), user2);
    assertEq(_getDelegateeByType(user, userState, GovernancePowerType.PROPOSITION), user3);
  }

  function _setDelegationStateAndTest(
    DelegationState initialState,
    GovernancePowerType governancePowerType,
    bool willDelegate,
    DelegationState expectedState
  ) internal {
    DelegationAwareBalance memory userState;
    DelegationAwareBalance memory updatedUserState;
    userState.delegationState = initialState;
    updatedUserState = _updateDelegationFlagByType(userState, governancePowerType, willDelegate);
    assertTrue(
      updatedUserState.delegationState == expectedState,
      Strings.toString(uint8(updatedUserState.delegationState))
    );
  }

  function testFor_updateDelegationFlagByType() public {
    _setDelegationStateAndTest(
      DelegationState.NO_DELEGATION,
      GovernancePowerType.VOTING,
      true,
      DelegationState.VOTING_DELEGATED
    );
    _setDelegationStateAndTest(
      DelegationState.NO_DELEGATION,
      GovernancePowerType.VOTING,
      false,
      DelegationState.NO_DELEGATION
    );
    _setDelegationStateAndTest(
      DelegationState.VOTING_DELEGATED,
      GovernancePowerType.VOTING,
      true,
      DelegationState.VOTING_DELEGATED
    );
    _setDelegationStateAndTest(
      DelegationState.FULL_POWER_DELEGATED,
      GovernancePowerType.VOTING,
      false,
      DelegationState.PROPOSITION_DELEGATED
    );
    _setDelegationStateAndTest(
      DelegationState.NO_DELEGATION,
      GovernancePowerType.PROPOSITION,
      true,
      DelegationState.PROPOSITION_DELEGATED
    );
    _setDelegationStateAndTest(
      DelegationState.PROPOSITION_DELEGATED,
      GovernancePowerType.PROPOSITION,
      false,
      DelegationState.NO_DELEGATION
    );
    _setDelegationStateAndTest(
      DelegationState.PROPOSITION_DELEGATED,
      GovernancePowerType.VOTING,
      true,
      DelegationState.FULL_POWER_DELEGATED
    );
    _setDelegationStateAndTest(
      DelegationState.FULL_POWER_DELEGATED,
      GovernancePowerType.VOTING,
      true,
      DelegationState.FULL_POWER_DELEGATED
    );
    _setDelegationStateAndTest(
      DelegationState.VOTING_DELEGATED,
      GovernancePowerType.PROPOSITION,
      true,
      DelegationState.FULL_POWER_DELEGATED
    );
    _setDelegationStateAndTest(
      DelegationState.FULL_POWER_DELEGATED,
      GovernancePowerType.PROPOSITION,
      true,
      DelegationState.FULL_POWER_DELEGATED
    );
  }
}
