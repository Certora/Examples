#!/bin/sh

certoraRun contracts/BallGameBroken.sol \
    --verify BallGameBroken:certora/specs/BallGame.spec \
    --solc solc8.0 \
    --msg  "KeepAway verification"

