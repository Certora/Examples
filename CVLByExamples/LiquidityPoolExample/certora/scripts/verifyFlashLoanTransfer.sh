certoraRun \
    contracts/Pool.sol \
    contracts/Asset.sol \
    certora/harness/TrivialReceiver.sol \
    certora/harness/TransferReceiver.sol \
    --link Pool:asset=Asset \
    --link TransferReceiver:underlying=Asset \
    --verify Pool:certora/specs/flashLoan_dispatcher.spec \
    --solc solc8.0 \
    --msg "flashLoan with transfer dispatchee" \
    --send_only

