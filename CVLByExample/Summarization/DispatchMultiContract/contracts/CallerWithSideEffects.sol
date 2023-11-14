// SPDX-License-Identifier: MIT

import "./Callee.sol";

contract CallerWithSideEffects {
    CalleeA public calleeA;
    CalleeB public calleeB;
    
    function setXA(uint256 _x) public {
        calleeA.setX(_x);
    }

    function getXA() public returns(uint256){
        return calleeA.getX();
    }

    function setXB(uint256 _x) public {
        calleeB.setX(_x);
    }

    function getXB() public returns(uint256){
        return calleeB.getX();
    }

    function setValueA(uint256 _value) public {
        calleeA.setValue(_value);
    }

    function getValueA() public returns(uint256){
        return calleeA.getValue();
    }

    function setValueB(uint256 _value) public {
        uint256 value = calleeB.setValue(_value);
    }

    function getValueB() public returns(uint256){
        return calleeB.getValue();
    }

    function getDummyB() public returns(uint256) {
        return calleeB.dummyB();
    }

    function setXFromAddress(address _addr, uint256 _x) public {
        Callee callee = Callee(_addr);
        callee.setX(_x);
    }

    function setXandSendEther(Callee _callee, uint256 _x) public payable {
        (uint256 x, uint256 value) = _callee.setXandSendEther{value: msg.value}(_x);
    }
}
