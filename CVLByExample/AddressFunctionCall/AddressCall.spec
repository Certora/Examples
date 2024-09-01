using A as a;
using B as b;

rule AddressCall {
    env e;
    address x;
    require x == a || x == b;
    assert x == a => x.balaceOf(e) == 1;
    assert x == b => x.balaceOf(e) == 2;
}