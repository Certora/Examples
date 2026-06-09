// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {BaseHook} from "v4-periphery/src/utils/BaseHook.sol";

import {Hooks} from "v4-core/src/libraries/Hooks.sol";
import {IPoolManager, SwapParams, ModifyLiquidityParams} from "v4-core/src/interfaces/IPoolManager.sol";
import {PoolKey} from "v4-core/src/types/PoolKey.sol";
import {PoolId, PoolIdLibrary} from "v4-core/src/types/PoolId.sol";
import {BalanceDelta, toBalanceDelta} from "v4-core/src/types/BalanceDelta.sol";
import {BeforeSwapDelta, BeforeSwapDeltaLibrary} from "v4-core/src/types/BeforeSwapDelta.sol";

import {PointsToken} from "./PointsToken.sol";

contract PointsHook is BaseHook {
    PointsToken public pointsToken;
    constructor(IPoolManager _poolManager) BaseHook(_poolManager) {
        pointsToken = new PointsToken();
    }

    function getHookPermissions()
        public
        pure
        override
        returns (Hooks.Permissions memory)
    {
        return
            Hooks.Permissions({
                beforeInitialize: true,
                afterInitialize: false,
                beforeAddLiquidity: false,
                afterAddLiquidity: true,
                beforeRemoveLiquidity: false,
                afterRemoveLiquidity: false,
                beforeSwap: false,
                afterSwap: true,
                beforeDonate: false,
                afterDonate: false,
                beforeSwapReturnDelta: false,
                afterSwapReturnDelta: false,
                afterAddLiquidityReturnDelta: false,
                afterRemoveLiquidityReturnDelta: false
            });
    }

    function _beforeInitialize(
        address sender,
        PoolKey calldata key,
        uint160 sqrtPriceX96
    ) internal override returns (bytes4) {
        require (key.currency0.isAddressZero(), "Only ETH/TOKEN pools allowed");
        return BaseHook.beforeInitialize.selector;
    }


    function _afterSwap(
        address sender,
        PoolKey calldata key,
        SwapParams calldata swapParams,
        BalanceDelta delta,
        bytes calldata hookData
    ) internal override returns (bytes4, int128) {
        // We only award points in the ETH/TOKEN pools.
        if (!key.currency0.isAddressZero()) {
            return (BaseHook.afterSwap.selector, 0);
        }

        // We only award points if the user is buying the TOKEN
        if (!swapParams.zeroForOne) {
            return (BaseHook.afterSwap.selector, 0);
        }

        // Let's figure out who's the user
        address user = parseHookData(hookData);

        // How much ETH are they spending?
        uint256 ethSpendAmount = uint256(int256(-delta.amount0()));

        // And award the points!
        awardPoints(user, ethSpendAmount);

        return (BaseHook.afterSwap.selector, 0);
    }

    function _afterAddLiquidity(
        address sender,
        PoolKey calldata key,
        ModifyLiquidityParams calldata params,
        BalanceDelta delta,
        BalanceDelta feesAccrued,
        bytes calldata hookData
    ) internal override returns (bytes4, BalanceDelta) {
        // We only award points in the ETH/TOKEN pools.
        if (!key.currency0.isAddressZero()) {
            return (BaseHook.afterAddLiquidity.selector, delta);
        }

        // Let's figure out who's the user
        address user = parseHookData(hookData);

        // How much ETH are they spending?
        if (delta.amount0() < 0) {
            uint256 ethSpendAmount = uint256(int256(-delta.amount0()));

            // And award the points!
            awardPoints(user, ethSpendAmount);
        }
        return (BaseHook.afterAddLiquidity.selector, toBalanceDelta(0,0));
    }

    function getPointsForAmount(
        uint256 amount
    ) internal pure returns (uint256) {
        return amount; // 1:1 with ETH
    }

    function awardPoints(address to, uint256 amount) internal {
        pointsToken.mint(to, getPointsForAmount(amount));
    }

    function getHookData(address user) public pure returns (bytes memory) {
        return abi.encode(user);
    }

    function parseHookData(
        bytes calldata data
    ) public pure returns (address user) {
        return abi.decode(data, (address));
    }    
}
