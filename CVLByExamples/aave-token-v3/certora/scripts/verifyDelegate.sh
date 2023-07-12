if [[ "$1" ]]
then
    RULE="--rule $1"
fi

certoraRun certora/harness/AaveTokenV3Harness.sol:AaveTokenV3Harness \
    --verify AaveTokenV3Harness:certora/specs/delegate.spec \
    $RULE \
    --solc solc8.13 \
    --optimistic_loop \
    --cloud \
    --msg "AaveTokenV3Harness:delegate.spec $1"
# --sanity
 