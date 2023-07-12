certoraRun contracts/Pool.sol contracts/Asset.sol contracts/SymbolicFlashLoanReceiver.sol \
    --link Pool:asset=Asset \
	--verify Pool:certora/specs/highLevel.spec \
    --solc solc8.0 \
    --msg "Abstract Pool, highLevel.spec" \
    --send_only

