// SPDX-License-Identifier: MIT
// OpenZeppelin Uniswap Hooks (last updated v0.1.0) (src/fee/BaseDynamicAfterFee.sol)

pragma solidity ^0.8.24;

import {BaseHook} from "src/base/BaseHook.sol";
import {BalanceDelta} from "v4-core/src/types/BalanceDelta.sol";
import {Hooks} from "v4-core/src/libraries/Hooks.sol";
import {PoolKey} from "v4-core/src/types/PoolKey.sol";
import {IPoolManager} from "v4-core/src/interfaces/IPoolManager.sol";
import {Currency} from "v4-core/src/types/Currency.sol";
import {SafeCast} from "v4-core/src/libraries/SafeCast.sol";
import {BeforeSwapDelta, BeforeSwapDeltaLibrary} from "v4-core/src/types/BeforeSwapDelta.sol";
import {CurrencySettler} from "src/utils/CurrencySettler.sol";
import {PoolId} from "v4-core/src/types/PoolId.sol";
import {IHookEvents} from "src/interfaces/IHookEvents.sol";
import {SwapParams} from "v4-core/src/types/PoolOperation.sol";

/**
 * @dev Base implementation for dynamic fees applied after swaps.
 *
 * In order to use this hook, the inheriting contract must define the {_getTargetOutput} and
 * {_afterSwapHandler} functions. The {_getTargetOutput} function returns the target output to
 * apply to the swap depending on the given apply flag. The {_afterSwapHandler} function is called
 * after the target output is applied to the swap and currency amount is received.
 *
 * WARNING: This is experimental software and is provided on an "as is" and "as available" basis. We do
 * not give any warranties and will not be liable for any losses incurred through any use of this code
 * base.
 *
 * _Available since v0.1.0_
 */
abstract contract BaseDynamicAfterFee is BaseHook, IHookEvents {
    using SafeCast for uint256;
    using CurrencySettler for Currency;

    uint256 internal _targetOutput;

    bool internal _applyTargetOutput;

    /**
     * @dev Target output exceeds swap amount.
     */
    error TargetOutputExceeds();

    /**
     * @dev Set the `PoolManager` address.
     */
    constructor(IPoolManager _poolManager) BaseHook(_poolManager) {}

    /**
     * @dev Sets the target output and apply flag to be used in the `afterSwap` hook.
     *
     * NOTE: The target output is reset to 0 in the `afterSwap` hook regardless of the apply flag.
     */
    function _beforeSwap(address sender, PoolKey calldata key, SwapParams calldata params, bytes calldata hookData)
        internal
        virtual
        override
        returns (bytes4, BeforeSwapDelta, uint24)
    {
        // Get the target output and apply flag
        (uint256 targetOutput, bool applyTargetOutput) = _getTargetOutput(sender, key, params, hookData);

        // Set the target output and apply flag, overriding any previous values.
        _applyTargetOutput = applyTargetOutput;
        _targetOutput = targetOutput;

        return (this.beforeSwap.selector, BeforeSwapDeltaLibrary.ZERO_DELTA, 0);
    }

    /**
     * @dev Apply the target output to the unspecified currency of the swap using fees.
     * The fees are minted as ERC-6909 tokens, which can then be redeemed in the
     * {_afterSwapHandler} function. Note that if the underlying unspecified currency
     * is native, the implementing contract must ensure that it can receive native tokens
     * when redeeming.
     *
     * NOTE: The target output is reset to 0, both when the apply flag is set to `false`
     * and when set to `true`.
     */
    function _afterSwap(
        address sender,
        PoolKey calldata key,
        SwapParams calldata params,
        BalanceDelta delta,
        bytes calldata
    ) internal virtual override returns (bytes4, int128) {
        uint256 targetOutput = _targetOutput;

        // Reset storage target output to 0 and use one stored in memory
        _targetOutput = 0;

        // Skip if target output is not active
        if (!_applyTargetOutput) {
            return (this.afterSwap.selector, 0);
        }

        // Fee defined in the unspecified currency of the swap
        (Currency unspecified, int128 unspecifiedAmount) = (params.amountSpecified < 0 == params.zeroForOne)
            ? (key.currency1, delta.amount1())
            : (key.currency0, delta.amount0());

        // If fee is on output, get the absolute output amount
        if (unspecifiedAmount < 0) unspecifiedAmount = -unspecifiedAmount;

        // Revert if the target output exceeds the swap amount
        if (targetOutput > uint128(unspecifiedAmount)) revert TargetOutputExceeds();

        // Calculate the fee amount, which is the difference between the swap amount and the target output
        uint256 feeAmount = uint128(unspecifiedAmount) - targetOutput;

        // Mint ERC-6909 tokens for unspecified currency fee and call handler
        if (feeAmount > 0) {
            unspecified.take(poolManager, address(this), feeAmount, true);
            _afterSwapHandler(key, params, delta, targetOutput, feeAmount);
        }

        // Emit the swap event with the amounts ordered correctly
        if (unspecified == key.currency0) {
            emit HookFee(PoolId.unwrap(key.toId()), sender, feeAmount.toUint128(), 0);
        } else {
            emit HookFee(PoolId.unwrap(key.toId()), sender, 0, feeAmount.toUint128());
        }

        return (this.afterSwap.selector, feeAmount.toInt128());
    }

    /**
     * @dev Return the target output to be enforced by the `afterSwap` hook using fees.
     *
     * IMPORTANT: The swap will revert if the target output exceeds the output unspecified amount from the swap.
     * In order to consume all of the output from the swap, set the target output to equal the output unspecified
     * amount and set the apply flag to `true`.
     *
     * @return targetOutput The target output, defined in the unspecified currency of the swap.
     * @return applyTargetOutput The apply flag, which can be set to `false` to skip applying the target output.
     */
    function _getTargetOutput(address sender, PoolKey calldata key, SwapParams calldata params, bytes calldata hookData)
        internal
        virtual
        returns (uint256 targetOutput, bool applyTargetOutput);

    /**
     * @dev Handler called after applying the target output to a swap and receiving the currency amount.
     *
     * @param key The pool key.
     * @param params The swap parameters.
     * @param delta The balance delta from the swap.
     * @param targetOutput The target output, defined in the unspecified currency of the swap.
     * @param feeAmount The amount of the unspecified currency taken from the swap.
     */
    function _afterSwapHandler(
        PoolKey calldata key,
        SwapParams calldata params,
        BalanceDelta delta,
        uint256 targetOutput,
        uint256 feeAmount
    ) internal virtual;

    /**
     * @dev Set the hook permissions, specifically {beforeSwap}, {afterSwap} and {afterSwapReturnDelta}.
     *
     * @return permissions The hook permissions.
     */
    function getHookPermissions() public pure virtual override returns (Hooks.Permissions memory permissions) {
        return Hooks.Permissions({
            beforeInitialize: false,
            afterInitialize: false,
            beforeAddLiquidity: false,
            afterAddLiquidity: false,
            beforeRemoveLiquidity: false,
            afterRemoveLiquidity: false,
            beforeSwap: true,
            afterSwap: true,
            beforeDonate: false,
            afterDonate: false,
            beforeSwapReturnDelta: false,
            afterSwapReturnDelta: true,
            afterAddLiquidityReturnDelta: false,
            afterRemoveLiquidityReturnDelta: false
        });
    }
}
