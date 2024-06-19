pragma solidity 0.8.24;

import {CallBacker} from './CallBacker.sol';

contract Vault {
    bytes32 slot = keccak256("transient");
    bytes32 lock = keccak256("lock");
    int256 storageValue;

    function tload(bytes32 key) internal returns (int) {
        int value;
        assembly {
            value := tload(key)
        }
        return value;
    }
    function tstore(bytes32 key, int256 value) internal{
        assembly {
            tstore(key, value)
        }
    }
    
    modifier onlyLocked {
        require (getLock() == 1);
        _;
    }

    function getDelta() public returns (int256) {
        return tload(slot);
    }


    function getLock() public returns (int256) {
        return tload(lock);
    }
    
    function addDelta(int256 delta) internal {
        int256 value = getDelta();
        value = value + delta;
        tstore(slot, value);
    }
    
    function borrow(int256 delta) external onlyLocked {
        storageValue += delta;
        addDelta(delta);
    }
    
    function repay(int256 delta) external onlyLocked {
        storageValue -= delta;
        addDelta(-delta);
    }
    
    function lockFunction(CallBacker callbackContract) external {
        require (getLock() == 0);
        tstore(lock, 1);
        callbackContract.callback();
        require (getDelta() == 0);
        tstore(lock, 0);
    }

}