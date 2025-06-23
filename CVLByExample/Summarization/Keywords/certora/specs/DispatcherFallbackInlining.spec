using IntGetterImpl as impl1;
using AnotherIntGetterImpl as impl2;

methods {
    function _.noSuchFun() external => DISPATCHER(optimistic=false, use_fallback=true);
}

rule fallback_should_be_reached_with_flag() {
    env e;
    
    // Instead of linking `CallsExternalContract:a=IntGetterImpl` which would make the callee resolved which would skip the DISPATCHER summary,
    // do this `require` to force at runtime the callee to always be `IntGetterImpl`.
    require currentContract.a == impl1;
    foo(e);
    uint n = impl1.var1;
    assert n == 5;
}

rule fallback_should_never_be_reached() {
    env e;
    require currentContract.a == impl2;
    require impl2.anothervar1 != 5;
    foo(e);
    uint n = impl2.anothervar1;
    assert n != 5;
}
