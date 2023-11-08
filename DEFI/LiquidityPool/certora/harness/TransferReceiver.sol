pragma solidity >= 0.8.0;

import "../../contracts/IFlashLoanReceiver.sol";
import "../../contracts/IERC20.sol";

contract TransferReceiver is IFlashLoanReceiver {
    IERC20  underlying;
    uint    transfer_amount;
    address pool;

    function executeOperation(
        uint256 amount,
        uint256 premium,
        address initiator
    ) external override(IFlashLoanReceiver) returns (bool) {
        underlying.transferFrom(pool, address(this), transfer_amount);
        return true;
    }
}

