certoraRun contracts/Pool.sol contracts/Asset.sol contracts/SymbolicFlashLoanReceiver.sol \
    --link Pool:asset=Asset \
	--verify Pool:certora/specs/highLevelSimplified.spec \
    --solc solc8.0 \
    --msg "Pool - simplified spec default setting" \
    --send_only

