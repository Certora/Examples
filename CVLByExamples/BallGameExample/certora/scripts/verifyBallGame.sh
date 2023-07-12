#!/bin/sh

certoraRun contracts/BallGame.sol \
    --verify BallGame:certora/specs/BallGame.spec \
    --solc solc8.0 \
    --msg  "KeepAway verification" \
    --server "staging"
    

