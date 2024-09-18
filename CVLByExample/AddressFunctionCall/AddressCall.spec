using A as a;
using B as b;
using C as c;

rule AddressCall {
    env e;
    address x;

    assert x.foo(e) >= 1 && x.foo(e) <= 2;

    assert x != c;
    assert x.foo(e) == 1 => x == a;
    assert x.foo(e) == 2 => x == b;
}
