// SPDX-License-Identifier: MIT

/**

  This is an extension of the AaveTokenV3 with added getters on the _balances fields

 */

pragma solidity ^0.8.0;

import {AaveTokenV3} from '../../src/AaveTokenV3.sol';

contract AaveTokenV3Harness is AaveTokenV3 {
  // returns user's token balance, used in some community rules
  function getBalance(address user) public view returns (uint104) {
    return _balances[user].balance;
  }

  // returns user's delegated proposition balance
  function getDelegatedPropositionBalance(address user) public view returns (uint72) {
    return _balances[user].delegatedPropositionBalance;
  }

  // returns user's delegated voting balance
  function getDelegatedVotingBalance(address user) public view returns (uint72) {
    return _balances[user].delegatedVotingBalance;
  }

  //returns user's delegating proposition status
  function getDelegatingProposition(address user) public view returns (bool) {
    return
      _balances[user].delegationState == DelegationState.PROPOSITION_DELEGATED ||
      _balances[user].delegationState == DelegationState.FULL_POWER_DELEGATED;
  }

  // returns user's delegating voting status
  function getDelegatingVoting(address user) public view returns (bool) {
    return
      _balances[user].delegationState == DelegationState.VOTING_DELEGATED ||
      _balances[user].delegationState == DelegationState.FULL_POWER_DELEGATED;
  }

  // returns user's voting delegate
  function getVotingDelegate(address user) public view returns (address) {
    return _votingDelegateeV2[user];
  }

  // returns user's proposition delegate
  function getPropositionDelegate(address user) public view returns (address) {
    return _propositionDelegateeV2[user];
  }

  // returns user's delegation state
  function getDelegationState(address user) public view returns (DelegationState) {
    return _balances[user].delegationState;
  }
}
