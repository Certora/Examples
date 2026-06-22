// SPDX-License-Identifier: MIT
pragma solidity 0.8.22;

// Interfaces
import { IERC20 } from "./IERC20.sol";

/// @title ERC20Utils
/// @notice Optimized functions for ERC20 tokens
library ERC20Utils {
    /*//////////////////////////////////////////////////////////////
                                ERRORS
    //////////////////////////////////////////////////////////////*/

    error IncorrectEthAmount();
    error PermitFailed();
    error TransferFromFailed();
    error TransferFailed();
    error ApprovalFailed();

    /*//////////////////////////////////////////////////////////////
                               CONSTANTS
    //////////////////////////////////////////////////////////////*/

    IERC20 internal constant ETH = IERC20(0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE);

    /*//////////////////////////////////////////////////////////////
                                APPROVE
    //////////////////////////////////////////////////////////////*/

    /// @dev Vendored from Solady by @vectorized - SafeTransferLib.approveWithRetry
    /// https://github.com/Vectorized/solady/src/utils/SafeTransferLib.sol#L325
    /// Instead of approving a specific amount, this function approves for uint256(-1) (type(uint256).max).
    function approve(IERC20 token, address to) internal {
        // solhint-disable-next-line no-inline-assembly
        assembly ("memory-safe") {
            mstore(0x14, to) // Store the `to` argument.
            mstore(0x34, 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) // Store the `amount`
                // argument (type(uint256).max).
            mstore(0x00, 0x095ea7b3000000000000000000000000) // `approve(address,uint256)`.
            // Perform the approval, retrying upon failure.
            if iszero(
                and( // The arguments of `and` are evaluated from right to left.
                    or(eq(mload(0x00), 1), iszero(returndatasize())), // Returned 1 or nothing.
                    call(gas(), token, 0, 0x10, 0x44, 0x00, 0x20)
                )
            ) {
                mstore(0x34, 0) // Store 0 for the `amount`.
                mstore(0x00, 0x095ea7b3000000000000000000000000) // `approve(address,uint256)`.
                pop(call(gas(), token, 0, 0x10, 0x44, codesize(), 0x00)) // Reset the approval.
                mstore(0x34, 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) // Store
                    // type(uint256).max for the `amount`.
                // Retry the approval, reverting upon failure.
                if iszero(
                    and(
                        or(eq(mload(0x00), 1), iszero(returndatasize())), // Returned 1 or nothing.
                        call(gas(), token, 0, 0x10, 0x44, 0x00, 0x20)
                    )
                ) {
                    mstore(0, 0x8164f84200000000000000000000000000000000000000000000000000000000)
                    // store the selector (error ApprovalFailed())
                    revert(0, 4) // revert with error selector
                }
            }
            mstore(0x34, 0) // Restore the part of the free memory pointer that was overwritten.
        }
    }

    /*//////////////////////////////////////////////////////////////
                                PERMIT
    //////////////////////////////////////////////////////////////*/

    /// @dev Executes an ERC20 permit and reverts if invalid length is provided
    function permit(IERC20 token, bytes calldata data) internal {
        // solhint-disable-next-line no-inline-assembly
        assembly ("memory-safe") {
            // check the permit length
            switch data.length
            // 32 * 7 = 224 EIP2612 Permit
            case 224 {
                let x := mload(64) // get the free memory pointer
                mstore(x, 0xd505accf00000000000000000000000000000000000000000000000000000000) // store the selector
                    // function permit(address owner, address spender, uint256
                    // amount, uint256 deadline, uint8 v, bytes32 r, bytes32 s)
                calldatacopy(add(x, 4), data.offset, 224) // store the args
                pop(call(gas(), token, 0, x, 228, 0, 32)) // call ERC20 permit, skip checking return data
            }
            // 32 * 8 = 256 DAI-Style Permit
            case 256 {
                let x := mload(64) // get the free memory pointer
                mstore(x, 0x8fcbaf0c00000000000000000000000000000000000000000000000000000000) // store the selector
                    // function permit(address holder, address spender, uint256
                    // nonce, uint256 expiry, bool allowed, uint8 v, bytes32 r, bytes32 s)
                calldatacopy(add(x, 4), data.offset, 256) // store the args
                pop(call(gas(), token, 0, x, 260, 0, 32)) // call ERC20 permit, skip checking return data
            }
            default {
                mstore(0, 0xb78cb0dd00000000000000000000000000000000000000000000000000000000) // store the selector
                    // (error PermitFailed())
                revert(0, 4)
            }
        }
    }

    /*//////////////////////////////////////////////////////////////
                                 ETH
    //////////////////////////////////////////////////////////////*/

    /// @dev Returns 1 if the token is ETH, 0 if not ETH
    function isETH(IERC20 token, uint256 amount) internal view returns (uint256 fromETH) {
        // solhint-disable-next-line no-inline-assembly
        assembly ("memory-safe") {
            // If token is ETH
            if eq(token, 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE) {
                // if msg.value is not equal to fromAmount, then revert
                if xor(amount, callvalue()) {
                    mstore(0, 0x8b6ebb4d00000000000000000000000000000000000000000000000000000000) // store the selector
                        // (error IncorrectEthAmount())
                    revert(0, 4) // revert with error selector
                }
                // return 1 if ETH
                fromETH := 1
            }
            // If token is not ETH
            if xor(token, 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE) {
                // if msg.value is not equal to 0, then revert
                if gt(callvalue(), 0) {
                    mstore(0, 0x8b6ebb4d00000000000000000000000000000000000000000000000000000000) // store the selector
                    // (error IncorrectEthAmount())
                    revert(0, 4) // revert with error selector
                }
            }
        }
        // return 0 if not ETH
    }

    /*//////////////////////////////////////////////////////////////
                                TRANSFER
    //////////////////////////////////////////////////////////////*/

    /// @dev Executes transfer and reverts if it fails, works for both ETH and ERC20 transfers
    function safeTransfer(IERC20 token, address recipient, uint256 amount) internal returns (bool success) {
        // solhint-disable-next-line no-inline-assembly
        assembly {
            switch eq(token, 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE)
            // ETH
            case 1 {
                // transfer ETH
                // Cap gas at 10000 to avoid reentrancy
                success := call(10000, recipient, amount, 0, 0, 0, 0)
            }
            // ERC20
            default {
                let x := mload(64) // get the free memory pointer
                mstore(x, 0xa9059cbb00000000000000000000000000000000000000000000000000000000) // store the selector
                    // (function transfer(address recipient, uint256 amount))
                mstore(add(x, 4), recipient) // store the recipient
                mstore(add(x, 36), amount) // store the amount
                success := call(gas(), token, 0, x, 68, 0, 32) // call transfer
                if success {
                    switch returndatasize()
                    // check the return data size
                    case 0 { success := gt(extcodesize(token), 0) }
                    default { success := and(gt(returndatasize(), 31), eq(mload(0), 1)) }
                }
            }
            if iszero(success) {
                mstore(0, 0x90b8ec1800000000000000000000000000000000000000000000000000000000) // store the selector
                    // (error TransferFailed())
                revert(0, 4) // revert with error selector
            }
        }
    }

    /*//////////////////////////////////////////////////////////////
                             TRANSFER FROM
    //////////////////////////////////////////////////////////////*/

    /// @dev Executes transferFrom and reverts if it fails
    function safeTransferFrom(
        IERC20 srcToken,
        address sender,
        address recipient,
        uint256 amount
    )
        internal
        returns (bool success)
    {
        // solhint-disable-next-line no-inline-assembly
        assembly {
            let x := mload(64) // get the free memory pointer
            mstore(x, 0x23b872dd00000000000000000000000000000000000000000000000000000000) // store the selector
                // (function transferFrom(address sender, address recipient,
                // uint256 amount))
            mstore(add(x, 4), sender) // store the sender
            mstore(add(x, 36), recipient) // store the recipient
            mstore(add(x, 68), amount) // store the amount
            success := call(gas(), srcToken, 0, x, 100, 0, 32) // call transferFrom
            if success {
                switch returndatasize()
                // check the return data size
                case 0 { success := gt(extcodesize(srcToken), 0) }
                default { success := and(gt(returndatasize(), 31), eq(mload(0), 1)) }
            }
            if iszero(success) {
                mstore(x, 0x7939f42400000000000000000000000000000000000000000000000000000000) // store the selector
                    // (error TransferFromFailed())
                revert(x, 4) // revert with error selector
            }
        }
    }

    /*//////////////////////////////////////////////////////////////
                                BALANCE
    //////////////////////////////////////////////////////////////*/

    /// @dev Returns the balance of an account, works for both ETH and ERC20 tokens
    function getBalance(IERC20 token, address account) internal view returns (uint256 balanceOf) {
        // solhint-disable-next-line no-inline-assembly
        assembly {
            switch eq(token, 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE)
            // ETH
            case 1 { balanceOf := balance(account) }
            // ERC20
            default {
                let x := mload(64) // get the free memory pointer
                mstore(x, 0x70a0823100000000000000000000000000000000000000000000000000000000) // store the selector
                    // (function balanceOf(address account))
                mstore(add(x, 4), account) // store the account
                let success := staticcall(gas(), token, x, 36, x, 32) // call balanceOf
                if success { balanceOf := mload(x) } // load the balance
            }
        }
    }
}
