// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity 0.8.28;

contract TransientTest {
    bool transient locked;

    function lock() public returns (bool) {
        locked = true;
        return true;
    }

    function unlock() public returns (bool) {
        locked = false;
        return false;
    }

    function isLocked() public view returns (bool) {
        return locked;
    }

}
