certoraRun \
    contracts/Pool.sol \
    contracts/Asset.sol \
    certora/harness/TrivialReceiver.sol \
    certora/harness/FlexibleReceiver.sol \
    --link Pool:asset=Asset \
    --link FlexibleReceiver:token=Pool \
    --verify Pool:certora/specs/flashLoan_dispatcher.spec \
    --solc solc8.0 \
    --msg "flashLoan with linked flexible dispatchee" \
    --send_only

