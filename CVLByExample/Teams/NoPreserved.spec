// This spec shows the invariant `nonExistTeamHasNoPlayers` cannot be proven without
// a preserved block.
methods {
    function teamOf(address) external returns (uint8) envfree;
    function leaderOf(uint8) external returns (address) envfree;
}


/** @title If a team does not exist it has not players
 *  This invariant cannot be proven without a preserved block.
 */
invariant nonExistTeamHasNoPlayers(uint8 teamId, address player)
    (teamId != 0 && leaderOf(teamId) == 0) => teamOf(player) != teamId ;