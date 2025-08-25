// SPDX-License-Identifier: MIT
// OpenZeppelin Uniswap Hooks (last updated v0.1.0) (src/interfaces/IHookEvents.sol)

pragma solidity ^0.8.24;

/**
 * @dev Interface for standard hook events emission.
 *
 * NOTE: Hooks should inherit from this interface to standardized event emission.
 */
interface IHookEvents {
    /**
     * @dev Event emitted when a swap is executed.
     */
    event HookSwap(
        bytes32 indexed id,
        address indexed sender,
        int128 amount0,
        int128 amount1,
        uint128 hookLPfeeAmount0,
        uint128 hookLPfeeAmount1
    );

    /**
     * @dev Event emitted when a fee is collected.
     */
    event HookFee(bytes32 indexed id, address indexed sender, uint128 feeAmount0, uint128 feeAmount1);

    /**
     * @dev Event emitted when a liquidity modification is executed.
     */
    event HookModifyLiquidity(bytes32 indexed id, address indexed sender, int128 amount0, int128 amount1);

    /**
     * @dev Event emitted when a bonus is added to a swap.
     */
    event HookBonus(bytes32 indexed id, uint128 amount0, uint128 amount1);
}
