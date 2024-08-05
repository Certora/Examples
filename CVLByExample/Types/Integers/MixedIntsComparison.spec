methods {
    function n() external returns (uint) envfree;
    function addToN(uint) external envfree;
    function castToInt(uint) external returns (int) envfree;
}

rule uint_positive {
    uint a;
    int b;
    require b < 0;

    assert b < a;
}

rule fun_with_sums {
    uint x;
    uint old_n = n();
    addToN@withrevert(x);
    assert lastReverted == (x + old_n > max_uint256);

    assert !lastReverted => (n() == old_n + x);
}

rule can_pick_bigger {
    uint a;
    uint8 b;
    require b == max_uint8;

    satisfy a > b;
}

rule cannot_pick_bigger_should_fail {
    uint a;
    uint8 b;
    require a > max_uint8;

    satisfy b > a;
}

rule overflow_in_solidity_cast {
   uint a;
   uint b;
   require b > 2^255;
   int signedB = castToInt(b);
   assert signedB < a;
}