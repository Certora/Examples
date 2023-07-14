# Ball Game

This repository contains a simple example contract that shows how strengthening
properties is sometimes necessary to make them correct, and thus provable.

The contract implement a simple "ball-passing" game, where the "ball" can be in the
hands of one of four players, denoted using numbers 1-4.
A method `pass` defines how players pass the ball. Each player passes the ball to some other player.

We wish to show that the ball can never reach player 2, and wrote the invariant `playerTwoNeverReceivesBall`, that can be found in `certora/specs/BallGame.spec`.

## Incorrect spec

When we try to verify the contract at `contracts/BallGame.sol` with the spec `BallGame.spec` the invariant fails because the invariant is not strong enough. 
The Prover starts from an arbitrary state, only assuming player 2 does not have the ball.
But actually if in our starting state the ball can be at player 4, player 4 passes the ball to player 2, violating the invariant.

To run the correct version, still getting a violation:
```certoraRun certora/conf/runWeakInvariant.conf```

## Correct Spec

This is fixed by the stronger spec `BallGameCorrect.spec`, requiring that in fact the ball can be held either by player 1 or by player 3.

The command for running this version:
```certoraRun certora/conf/runFixed.conf```




