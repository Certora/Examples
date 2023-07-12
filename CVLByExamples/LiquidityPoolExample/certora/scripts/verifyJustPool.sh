certoraRun contracts/Pool.sol \
    --verify Pool:certora/specs/pool_havoc.spec \
    --solc solc8.0 \
    --msg "Pool with no summarization" \
    --send_only

