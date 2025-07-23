using D as d;
using E as e;

rule r(uint n) {
    env environ;
    uint ret = foo(environ, n);
    assert currentContract.i == d || currentContract.i == e, "optimistic dispatching should promise this";
    assert currentContract.i == d => ret == n;
    assert currentContract.i == e => ret == n + 1;
}
