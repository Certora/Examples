// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

import {ITeams} from './ITeams.sol';


/// @title A contract for managing "teams"
contract Teams is ITeams {

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
        require(leader != address(0) && playerA != address(0) && playerB != address(0));

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
        require(_teamOf[newLeader] == teamId);

        _leaderOf[teamId] = newLeader;
    }
}
