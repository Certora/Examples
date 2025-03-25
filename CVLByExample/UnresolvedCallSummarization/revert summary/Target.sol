// SPDX-License-Identifier: AGPL-3.0-or-later
pragma solidity ^0.8.21;

/// @title Intermediate contract that makes low level calls
contract Target {
    function calculate(uint256 x) external pure returns (uint256) {
        return x * x;
    }
    
    function calculate2(uint256 x) external pure returns (uint256) {
        return x + 2;
    }
}
