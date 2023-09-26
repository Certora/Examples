contract Base {

    function foo(uint256 _x) public pure returns(uint256) {
        return _x + 5;
    }

    function bar(uint256 _x) public pure returns(uint256) {
        return _x + 50;
    }
}

contract Partial {
    function foo(uint256 _x) public pure returns(uint256) {
        return _x + 30;
    }
    
}

