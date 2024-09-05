using A as a;
using B as b;

rule AddressCall {
    env e;
    address x;
    require x == a || x == b;
    assert x.foo(e) >= 1 && x.foo(e) <= 2;
}

// Without the require the address dispatch is not constrained and x can be any address.
// In this case where x is not a or b, assert false will be triggered by the default case.
rule AddressCallDefaultCase {
    env e;
    address x;
    assert x.foo(e) >= 1 && x.foo(e) <= 2;
}