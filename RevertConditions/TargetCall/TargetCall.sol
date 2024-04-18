pragma solidity ^0.8.20;

contract TargetCall {
    address public target;

    constructor(address _target) {
        target = _target;
    }

    function forward(uint256 _value) public {
        if (_value %2 == 0){
            // Use delegatecall to forward the call to the target contract
        (bool success, bytes memory data) = target.delegatecall(abi.encodeWithSignature("doSomething(uint256)", _value));
        } else {
            // Use delegatecall to forward the call to the target contract
        (bool success, bytes memory data) = target.call(abi.encodeWithSignature("doSomething(uint256)", _value));
        }   
    }
}