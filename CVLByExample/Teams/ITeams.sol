// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;


/** @title An interface of managing "teams"
 *  - Each team is identified by a unique id 1-255
 *  - Each team has three different players, one of which is the team leader
 *  - Each player can belong only to a single team
 *  - Team id of zero means the address has no assigned team
 *  - Address zero cannot be part of a team
 *  - If the team leader is address zero it means the team has not been created
 */
interface ITeams {

    /// @return The team id of the player
    /// @notice Return value of 0 means the player has not been assigned to a team
    function teamOf(address player) external view returns (uint8);

    /// @return The team leader
    /// @notice Return value of zero means the team has not been created
    function leaderOf(uint8 teamId) external view returns (address);

    /// @dev Players must not be assigned to any team
    /// @dev The team must not exist before the call
    function createTeam(
        address leader,
        address playerA,
        address playerB,
        uint8 teamId
    ) external;

    /// @notice Change the team's leader
    /// @dev Only the current leader may call this function
    /// @dev The new leader must be a member of the tem
    function changeLeader(address newLeader) external;
}
