// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity 0.8.24;

import {Mutexer} from "./Mutexer.sol";

enum Access {
    Contract,
    Function,
    Custom
}

contract MockMutexer is Mutexer {

    event Accessed(Access indexed access);

    constructor() contractLock{}

    function isLocked() external returns (bool){
        Mutex value;
        uint256 key = CONTRACT_LOCK;
        assembly {
             value := tload(key)
        }
        return value == Mutex.Locked;
    }
    

   // for testing

    function contractLevelAccess() external contractLock {
        emit Accessed(Access.Contract);
    }
    function changeLock() external  {
        _mocktstore(CONTRACT_LOCK, Mutex.Locked);
    }

     function _mocktstore(uint256 key, Mutex value) private {
        assembly {
            tstore(key, value)
        }
    }

}