// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "./Callee.sol";

contract CallerWithSideEffects {
    Callee calleeA;
    Callee calleeB;
    
    function setX(Callee _callee, uint256 _x) public {
        uint256 x = _callee.setX(_x);
    }

    function getX(Callee _callee) public returns(uint256){
        // return _callee.x();
        return _callee.getX();
    }


    function setValue(Callee _callee, uint256 _value) public {
        uint256 value = _callee.setValue(_value);
    }

    function getValue(Callee _callee) public returns(uint256){
        return _callee.value();
    }

    function setXFromAddress(address _addr, uint256 _x) public {
        Callee callee = Callee(_addr);
        callee.setX(_x);
    }

    function setXandSendEther(Callee _callee, uint256 _x) public payable {
        (uint256 x, uint256 value) = _callee.setXandSendEther{value: msg.value}(_x);
    }
}
