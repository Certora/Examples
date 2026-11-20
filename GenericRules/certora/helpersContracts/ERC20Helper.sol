// SPDX-License-Identifier: agpl-3.0
pragma solidity ^0.8.0;
import "../../contracts/IERC20.sol";

contract ERC20Helper {

    function tokenBalanceOf(address token, address user) public returns (uint256) {
            return IERC20(token).balanceOf(user);
    }
}