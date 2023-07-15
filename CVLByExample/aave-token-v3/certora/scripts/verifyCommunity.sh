if [[ "$1" ]]
then
    RULE="--rule $1"
fi

certoraRun certora/harness/AaveTokenV3HarnessCommunity.sol:AaveTokenV3Harness \
    --verify AaveTokenV3Harness:certora/specs/community.spec \
    $RULE \
    --solc solc8.13 \
    --optimistic_loop \
    --cloud \
    --msg "AaveTokenV3HarnessCommunity:community.spec $1"
# --sanity
 