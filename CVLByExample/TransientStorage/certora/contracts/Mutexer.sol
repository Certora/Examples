// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity 0.8.24;

/// @title Mutexer
/// @author jtriley.eth
/// @notice Mutli-granularity Mutex
abstract contract Mutexer {
    error Locked(uint256 key);

    enum Mutex {
        Unlocked,
        Locked
    }

    uint256 internal constant CONTRACT_LOCK = 5;

    modifier contractLock() {
        if (_tload(CONTRACT_LOCK) == Mutex.Locked) revert Locked(CONTRACT_LOCK);

        _tstore(CONTRACT_LOCK, Mutex.Locked);
        _;
        _tstore(CONTRACT_LOCK, Mutex.Unlocked);
    }

    function _tstore(uint256 key, Mutex value) private {
        assembly {
            tstore(key, value)
        }
    }

    function _tload(uint256 key) private view returns (Mutex value) {
        assembly {
            value := tload(key)
        }
    }
}