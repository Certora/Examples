// Spec for the `ITeams` interface - showing examples of invariants
methods {
    function teamOf(address) external returns (uint8) envfree;
    function leaderOf(uint8) external returns (address) envfree;
}

/// @title The team's leader is part of the team
invariant leaderBelongsToTeam(uint8 teamId)
    (teamId != 0 && leaderOf(teamId) != 0) => teamOf(leaderOf(teamId)) == teamId ;

/// @title Address zero is not in any team
invariant addressZeroNotPlayer()
    teamOf(0) == 0 ;

/// @title If a team does not exist it has not players
invariant nonExistTeamHasNoPlayers(uint8 teamId, address player)
    (teamId != 0 && leaderOf(teamId) == 0) => teamOf(player) != teamId {
        preserved {
            requireInvariant addressZeroNotPlayer();
        }
    }

/// @return If the four addresses are all different from each other
function fourDifferentAddresses(address a, address b, address c, address d) returns bool {
    return (a != b && a != c && a != d && b != c && b != d && c != d);
}

/// @return If all players are on the same team
function sameTeam(address a, address b, address c) returns bool {
    return teamOf(a) == teamOf(b) && teamOf(b) == teamOf(c);
}

/// @title A team has at most three players
invariant teamHasMaxThreePlayers(address a, address b, address c, address d)
    (teamOf(a) != 0 && fourDifferentAddresses(a, b, c, d) && sameTeam(a, b, c) => teamOf(d) != teamOf(a)) {
        preserved createTeam(address leader, address playerA, address playerB, uint8 teamId) with(env e) {
            requireInvariant nonExistTeamHasNoPlayers(teamId, a);
            requireInvariant nonExistTeamHasNoPlayers(teamId, b);
            requireInvariant nonExistTeamHasNoPlayers(teamId, c);
            requireInvariant nonExistTeamHasNoPlayers(teamId, d);
        }
    }