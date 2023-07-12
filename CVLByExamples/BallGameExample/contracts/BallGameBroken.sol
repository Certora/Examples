pragma solidity ^0.8.0;

/**
 * Contract that models a game of keep away.  The contract keeps track of an
 * integer indicating which player holds a ball.
 *
 * When a user calls {pass}, the players will pass the ball to another player if
 * they have it:
 *   - player 1 will pass to player 3
 *   - player 3 will pass back to player 1
 *   - any other player will pass to player 2
 *
 * ...except this version has a bug
 *
 * Player 1 starts with the ball; the game is lost if player 2 ever gets the
 * ball.
 */
contract BallGameBroken {

    /// The current position of the ball
    uint8 public ballPosition;

    /// Initialize the ball position to 1
    constructor() {
        ballPosition = 1;
    }
    
    /// Move the ball to the next player, based on who is currently holding it:
    ///   - player 1 will pass to player 3
    ///   - player 3 will pass to player 1
    ///   - everyone else will pass to player 2
    ///
    /// @dev this version has a known bug
    function pass() external {
        if (ballPosition == 1)
            ballPosition = 4;
        else if (ballPosition == 3)
            ballPosition = 1;
        else
            ballPosition = 2;
    }

}
