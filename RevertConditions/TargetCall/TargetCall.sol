pragma solidity ^0.8.20;

interface SomeCaller {
    function execute() external returns (bool, uint);
}

contract TargetCall {
    address public target;

    constructor(address _target) {
        target = _target;
    }

    function forward() public {
        SomeCaller(target).execute();   
    }
}