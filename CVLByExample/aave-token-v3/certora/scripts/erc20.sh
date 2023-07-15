if [[ "$1" ]]
then
    RULE="--rule $1"
fi

certoraRun certora/harness/AaveTokenV3Harness.sol:AaveTokenV3Harness \
    --verify AaveTokenV3Harness:certora/specs/erc20.spec \
    $RULE \
    --solc solc8.13 \
    --optimistic_loop \
    --cloud \
    --msg "AaveTokenV3:erc20.spec $1"
 