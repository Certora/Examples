methods {
    function ballPosition() external returns(uint8) envfree;
}

/// The ball should never get to player 2 - too weak version.
invariant playerTwoNeverReceivesBall() 
    ballPosition() != 2;

