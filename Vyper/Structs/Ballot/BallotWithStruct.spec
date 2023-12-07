// methods {
//     function directlyVoted(address addr) external returns(bool) envfree;
//     // function voterCount() external returns(int128) envfree;
// }

rule giveRightIncreasesVoterCount(address voter) {
    env e;

    int128 voterCountBefore = voterCount(e);
    bool votedBefore = directlyVoted(e, voter);
    giveRightToVote(e, voter);
    assert !votedBefore => voterCount(e) == assert_int128(voterCountBefore + 1);
}

// Assignment to a struct variable
// Assignments to multiple lhs only work for calls to functions which return multiple values.
rule revertIfDelegatingAlreadyVoted(address vaddress) {
    env e;
    int128 weight;
    bool alreadyVoted;
    address delegate;
    int128 vote;
    weight, alreadyVoted, delegate, vote = getVoter(e, e.msg.sender);
    delegate@withrevert(vaddress);
    assert alreadyVoted => lastReverted;
}