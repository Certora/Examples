// SPDX-License-Identifier: MIT

/**

  This is an extension of the harnessed AaveTokenV3 with added getters on the _balances fields.
  The imported harnessed AaveTokenV3 contract uses uint8 instead of an enum for delegation state.

  This modification is introduced to bypass a current Certora Prover limitation on accessing
  enum fields inside CVL hooks

 */

pragma solidity ^0.8.0;

import {AaveTokenV3} from '../../src/AaveTokenV3.sol';

contract AaveTokenV3Harness is AaveTokenV3 {
  function getBalance(address user) public view returns (uint104) {
    return _balances[user].balance;
  }

  function getDelegatedPropositionBalance(address user) public view returns (uint72) {
    return _balances[user].delegatedPropositionBalance;
  }

  function getDelegatedVotingBalance(address user) public view returns (uint72) {
    return _balances[user].delegatedVotingBalance;
  }

  function getDelegatingProposition(address user) public view returns (bool) {
    DelegationState state = _balances[user].delegationState;
    return
      state == DelegationState.PROPOSITION_DELEGATED ||
      state == DelegationState.FULL_POWER_DELEGATED;
  }

  function getDelegatingVoting(address user) public view returns (bool) {
    DelegationState state = _balances[user].delegationState;
    return
      state == DelegationState.VOTING_DELEGATED ||
      state == DelegationState.FULL_POWER_DELEGATED;
  }

  function getVotingDelegate(address user) public view returns (address) {
    return _votingDelegateeV2[user];
  }

  function getPropositionDelegate(address user) public view returns (address) {
    return _propositionDelegateeV2[user];
  }

  function getDelegationState(address user) public view returns (DelegationState) {
    return _balances[user].delegationState;
  }
}
