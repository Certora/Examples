contract Callee {
    uint256 public x;
    uint256 public value;

    function setX(uint256 _x) public returns (uint256) {
        x = _x;
        return x;
    }

    function getX() public view returns (uint256) {
        return x;
    }

    function getValue() public view returns (uint256) {
        return value;
    }

    function setValue(uint256 _value) public returns (uint256) {
        value = _value;
        return value;
    }

    function setXandSendEther(uint256 _x) public payable returns (uint256, uint256) {
        x = _x;
        value = msg.value;

        return (x, value);
    }
}

contract CalleeA is Callee {
    function dummyA() public view returns (uint256) {
        return x + value;
    }
}

contract CalleeB is Callee {
    function dummyB() public view returns (uint256) {
        return 222;
    }
}
 