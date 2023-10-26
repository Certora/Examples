/**
  Base contains all functions used in the spec
*/
contract Base {

    function foo(uint256 _x) public pure returns(uint256) {
        return _x + 5;
    }

    function bar(uint256 _x) public pure returns(uint256) {
        return _x + 50;
    }

    // The function called from the spec through which the summarization of bar() is applied.
    // We need this function to apply the summary because functions called from the spec are never summarized.
    function callBar(uint256 _x) public pure returns(uint256) {
        return bar(_x);
    }
}

/**
    Partial does not have the function bar() used in the spec.
*/
contract Partial {
    function foo(uint256 _x) public pure returns(uint256) {
        return _x + 30;
    }

    function callFoo(uint256 _x) public pure returns(uint256) {
        return foo(_x);
    }
  
}

