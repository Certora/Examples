// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity ^0.8.24;

import {PointsHook} from "../../src/PointsHook.sol";
import {IPoolManager} from "v4-core/src/interfaces/IPoolManager.sol";
import {Hooks} from "v4-core/src/libraries/Hooks.sol";

contract PointsHookHarness is PointsHook {
    constructor(IPoolManager _poolManager) PointsHook(_poolManager) {}

    function checkHookPermission(uint160 flag)
        external
        view
        returns (bool)
    {
        validateHookAddress(this);
        return Hooks.hasPermission(this, flag); 
    }

    function wrapValidateHookAddress()
        external view
    {
        validateHookAddress(this);
    }

    function checkHookAddress()
        external
        view
        returns (bool)
    {
        try this.wrapValidateHookAddress() {
            return true;
        } catch {
            return false;
        }
    }
}
