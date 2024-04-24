// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {ITeams} from './ITeams.sol';


/// @title A buggy implementation of ITeams
contract TeamsBugs is ITeams {

    mapping(address => uint8) internal _teamOf;
    mapping(uint8 => address) internal _leaderOf;

    /// @inheritdoc ITeams
    function teamOf(address player) external view returns (uint8) {
        return _teamOf[player];
    }

    /// @inheritdoc ITeams
    function leaderOf(uint8 teamId) external view returns (address) {
        return _leaderOf[teamId];
    }

    /// @inheritdoc ITeams
    function createTeam(
        address leader,
        address playerA,
        address playerB,
        uint8 teamId
    ) external {
        require(_leaderOf[teamId] == address(0));
        require(_teamOf[leader] == 0 && _teamOf[playerA] == 0 && _teamOf[playerB] == 0);
        require(leader != playerA && leader != playerB && playerA != playerB);

        _leaderOf[teamId] = leader;
        _teamOf[leader] = teamId;
        _teamOf[playerA] = teamId;
        _teamOf[playerB] = teamId;
    }

    /// @inheritdoc ITeams
    function changeLeader(address newLeader) external {
        uint8 teamId = _teamOf[msg.sender];

        require(teamId != 0);
        require(msg.sender == _leaderOf[teamId]);

        _leaderOf[teamId] = newLeader;
    }
}
