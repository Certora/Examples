certoraRun contracts/Pool.sol contracts/Asset.sol certora/harness/TrivialReceiver.sol \
    --verify Pool:certora/specs/flashLoan_dispatcher.spec \
    --solc solc8.0 \
    --link Pool:asset=Asset \
    --msg "flashLoan with trivial dispatchee" \
    --send_only

