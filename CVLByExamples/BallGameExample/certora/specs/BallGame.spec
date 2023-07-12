methods {
    function ballPosition() external returns(uint8) envfree;
    function pass()                        external envfree;
}

/// The ball should never get to player 2
invariant playerTwoNeverWins()
    ballPosition() != 2;

