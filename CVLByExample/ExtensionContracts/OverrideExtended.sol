contract Extended {
    function foo() external returns (string memory) {
        return "Extended.foo";
    }

    function bar() external returns (string memory) {
        return "Extended.bar";
    }
}

contract Extender {
    function foo() external returns (string memory) {
        return "Extender.foo";
    }
}
