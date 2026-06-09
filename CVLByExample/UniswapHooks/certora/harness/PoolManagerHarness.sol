// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity 0.8.26;

import {PoolManager} from "v4-core/src/PoolManager.sol";
import {BalanceDelta, toBalanceDelta} from "v4-core/src/types/BalanceDelta.sol";
import {Currency} from "v4-core/src/types/Currency.sol";
import {CurrencyDelta} from "v4-core/src/libraries/CurrencyDelta.sol";

contract PoolManagerHarness is PoolManager {
    using CurrencyDelta for Currency;
    
    constructor(address initialOwner) PoolManager(initialOwner) {}

    function computeBalanceDelta(int128 _amount0, int128 _amount1) external pure returns (BalanceDelta) {
        return toBalanceDelta(
            _amount0,
            _amount1
        );
    }


    function getDelta(Currency currency, address account) external view returns (int256 delta) {
        return currency.getDelta(account);
    }
}
