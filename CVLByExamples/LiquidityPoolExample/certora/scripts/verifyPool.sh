certoraRun \
    certora/harness/PoolHarness.sol \
    contracts/Asset.sol          \
    certora/helpers/tokens/*.sol \
    certora/harness/*.sol        \
    --verify PoolHarness:certora/specs/pool.spec \
    --solc solc8.0 \
    --msg "Pool complete spec" \
    --send_only

