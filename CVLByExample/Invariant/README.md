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
```certoraRun runWeakInvariant.conf```

[A report of this run](https://prover.certora.com/output/15800/69c8e23f33c1479cbad44c1333a635af?anonymousKey=6154079d49ca940c8a59ca7d2ee62b6052694381)

## Correct Spec

This is fixed by the stronger spec `BallGameCorrect.spec`, requiring that the ball can be held either by player 1 or by player 3.

The command for running this version:
```certoraRun runFixed.conf```

[A report of this run](https://prover.certora.com/output/15800/b05cae20910045b9805702dad78ff9ef?anonymousKey=f5fe95dfa296dbca91a3e5c88c4f518abef908ff)





