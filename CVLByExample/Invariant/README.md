# Invariants

This repository contains a simple example contract that shows how strengthening
properties is sometimes necessary to make them correct, and thus provable.

The contract implements a simple "ball-passing" game, where the "ball" can be in the
hands of one of four players, denoted by numbers 1-4.
A method `pass` defines how players pass the ball. Each player passes the ball to another player.

We wish to depict that the ball can never reach player 2, and wrote the invariant `playerTwoNeverReceivesBall`. This can be found in `certora/specs/BallGame.spec`.

## Incorrect spec

When we try to verify the contract at `contracts/BallGame.sol` with the spec `BallGame.spec`, the invariant fails because it is not strong enough. 
The Certora Prover starts from an arbitrary state, only assuming that player 2 does not have the ball.
But actually if in our starting state the ball can be at player 4, player 4 passes the ball to player 2, violating the invariant.

To run the incorrect spec:
```certoraRun certora/conf/runWeakInvariant.conf```

[A report of this run](https://prover.certora.com/output/1902/08b4c079e3e54fb7b6ea07a4b0187339?anonymousKey=c6861d58bd612b3c2d9d656a361e98fada5ebbd7)

## Correct Spec

This is fixed by the stronger spec `BallGameCorrect.spec`, requiring that the ball can be held either by player 1 or by player 3.

The command for running this version:
```certoraRun certora/conf/runFixed.conf```

[A report of this run](file:///home/sitvanit/EVMVerifier-all/examples-doc/Examples/CVLByExample/Invariant/emv-1-certora-21-Nov--11-42/Reports/FinalResults.html)





