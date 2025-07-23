using A as a;
using B as b;

rule AddressCall() {
    env e;
    address x;
    assert x.foo(e) >= 1 && x.foo(e) <= 2;
}
