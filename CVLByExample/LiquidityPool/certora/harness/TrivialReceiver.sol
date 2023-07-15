pragma solidity >= 0.8.0;

import "../../contracts/IFlashLoanReceiver.sol";

contract TrivialReceiver is IFlashLoanReceiver {
    function executeOperation(
        uint256 amount,
        uint256 premium,
        address initiator
    ) external override(IFlashLoanReceiver) returns (bool) {
        // do nothing
        return true;
    }
}

