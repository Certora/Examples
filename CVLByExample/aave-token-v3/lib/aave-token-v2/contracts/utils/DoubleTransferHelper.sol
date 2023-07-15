// SPDX-License-Identifier: agpl-3.0
pragma solidity 0.7.5;

import "../interfaces/IERC20.sol";

contract DoubleTransferHelper {

    IERC20 public immutable AAVE;

    constructor(IERC20 aave) public {
        AAVE = aave;
    }

    function doubleSend(address to, uint256 amount1, uint256 amount2) external {
        AAVE.transfer(to, amount1);
        AAVE.transfer(to, amount2);
    }
}