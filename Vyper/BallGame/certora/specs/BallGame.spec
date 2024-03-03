methods {
    function ballPosition() external returns(uint8) envfree;
    function passBall()                        external envfree;
}

/// The ball should never get to player 2
invariant playerTwoNeverReceivesBall() 
    ballPosition() != 2;

