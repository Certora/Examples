certoraRun contracts/Pool.sol contracts/Asset.sol contracts/SymbolicFlashLoanReceiver.sol \
    --link Pool:asset=Asset \
	--verify Pool:certora/specs/mathProperties.spec \
    --solc solc8.0 \
    --msg "Abstract Pool, mathProperties" \
    --send_only

