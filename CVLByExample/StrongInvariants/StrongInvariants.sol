pragma solidity 0.8.24;

interface SomeInterface {
    function externalCall() external;
}

contract StrongInvariants {
    uint256 public storageValue = 1;

    function modifyAndExternalCall(SomeInterface token) external {
        storageValue = 2;
        token.externalCall();
        storageValue = 1;
    }
}