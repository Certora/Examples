// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IBaseAdminUpgradeabilityProxy {
    function upgradeTo(address newImplementation) external;
}
