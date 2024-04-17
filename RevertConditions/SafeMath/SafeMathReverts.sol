// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity >=0.8.0;


contract SafeMathReverts {
    uint256 public value = 0;

    function increaseValue(uint256 amount) external {
        value += amount;
    }

    function decreaseValue(uint256 amount) external {
        value -= amount;
    }

    function divideValue(uint256 divideBy) external {
        value /= divideBy;
    }
}