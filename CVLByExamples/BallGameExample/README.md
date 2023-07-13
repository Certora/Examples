# Ball Game

This repository contains a simple example contract that shows how strengthening
invariants is sometimes necessary to prove them.

There are two versions of the contract:

## Incorrect Code

The version with a bug is `BallGameBroken.sol` in which the invariant is not preserved because the ball gets
to player 4.

The command for running this version:
```certoraRun certora/specs/runBroken.conf```

## Correct Code

A correct contract is `BallGameCorrect.sol`, but even when trying to verify this contract with the previous spec `BallGame.spec` the invariant fails because the invariant is not strong enough.

The command for running this version:
```certoraRun certora/specs/runWeakInvariant.conf```

## Correct Code and Spec

This is fixed by the stronger spec `BallGameCorrect.spec`.

The command for running this version:
```certoraRun certora/specs/runFixed.conf```




