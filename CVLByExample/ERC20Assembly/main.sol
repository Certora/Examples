// SPDX-License-Identifier: MIT

pragma solidity 0.8.22;

import { IERC20 } from "./IERC20.sol";
import { ERC20Utils } from "./ERC20Utils.sol";

contract main {

    using ERC20Utils for IERC20;

    function approve(IERC20 token, address to) external {
        token.approve(to);
    }

    function permit(IERC20 token, bytes calldata data) external {
        token.permit(data);
    }

    function isETH(IERC20 token, uint256 amount) external payable returns (uint256) {
        return token.isETH(amount);
    }

    function safeTransfer(IERC20 token, address recipient, uint256 amount) external returns (bool) {
        return token.safeTransfer(recipient, amount);
    }

    function safeTransferFrom(
        IERC20 srcToken,
        address sender,
        address recipient,
        uint256 amount
    )
        external
        returns (bool success)
    {
        return srcToken.safeTransferFrom(sender, recipient, amount);
    }

    function getBalance(IERC20 token, address account) external view returns (uint256) {
        return token.getBalance(account);
    }

    function encodeForPermit224(
        address owner,
        address spender,
        uint256 value,
        uint256 deadline,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) external pure returns (bytes memory) {
        return abi.encode(owner, spender, value, deadline, v, r, s);
    }

    function encodeForPermit256(
        address owner,
        address spender,
        uint256 value,
        uint256 deadline,
        bool allowed,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) external pure returns (bytes memory) {
        return abi.encode(owner, spender, value, deadline, allowed, v, r, s);
    }
}