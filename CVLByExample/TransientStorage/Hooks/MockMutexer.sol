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

    // getters
    function lockValue() external returns (uint){
        return uint(Mutex.Locked);
    }
    function getContractLock() public returns (uint256){
        return CONTRACT_LOCK;
    }

   // for testing

    function contractLevelAccess() external contractLock {
        emit Accessed(Access.Contract);
    }
}