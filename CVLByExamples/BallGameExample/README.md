# Keep Away

This repository contains a simple example contract that shows how strengthening
invariants is sometimes necessary to prove them.


TODO: this repository is a work in progress.  See [the Certora tutorials][tutorial].

[tutorial]: https://github.com/Certora/Tutorials/tree/master/07.Lesson_InductiveReasoning

There are two versions of the contract:

The version with a bug is `BallGameBroken.sol" in which the invariant is not preserved because the ball gets
to player 4.

The command for running this version:
```certoraRun certora/specs/runBroken.conf```

A correct contract is `BallGameCorrect.sol`, but even when trying to verify this contract with the previous spec `BallGame.spec` the invariant fails because the invariant is not strong enough.

The command for running this version:
```certoraRun certora/specs/runWeakInvariant.conf```

This is fixed by the stronger spec `BallGameCorrect.spec`.

The command for running this version:
```certoraRun certora/specs/runFixed.conf```




