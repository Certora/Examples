interface I {
    function bar(uint n) external returns (uint);
}

contract C {
    I i;

    function foo(uint n) external returns (uint) {
        return i.bar(n);
    }
}

contract D is I {
    function bar(uint n) external returns (uint) {
        return n;
    }
}

contract E is I {
    function bar(uint n) external returns (uint) {
        return n+1;
    }
}