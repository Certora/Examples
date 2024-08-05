contract Ints {
    uint public n;

    function addToN(uint x) public {
        n = n + x;
    }

    function castToInt(uint x) public returns (int) {
        return int(x);
    }
}