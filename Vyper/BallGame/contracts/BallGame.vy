
###
# Contract that models a game of keep away.  The contract keeps track of an
# integer indicating which player holds a ball.
#
# When a user calls {pass}, the players will pass the ball to another player if
# they have it:
#   - player 1 will pass to player 3
#   - player 3 will pass back to player 1
#   - any other player will pass to player 2
#
# Player 1 starts with the ball the game is lost if player 2 ever gets the
# ball.
##

### The current position of the ball
ballPosition: public(uint8)

### Initialize the ball position to 1
@external
def __init__():
    self.ballPosition = 1

### Move the ball to the next player, based on who is currently holding it:
###   - player 1 will pass to player 3
###   - player 3 will pass to player 1
###   - everyone else will pass to player 2
@external
def passBall():
    if self.ballPosition == 1:
        self.ballPosition = 3
    elif self.ballPosition == 3:
        self.ballPosition = 1
    else:
        self.ballPosition = 2


