using Proxy as Proxy;
using Implementation as Implementation;

methods {
    function callAddition(address,uint32,uint256,uint256) external returns(uint256) envfree;
    function _._ external => DISPATCH [
        Proxy._,
        Implementation._
    ] default NONDET;
}

rule ProxyFallbackNeverRevertsWhenCallingAddition {
    address proxy;
    uint32 methodsig;
    uint256 x;
    uint256 y;

    require proxy == Proxy;
    require methodsig == sig:Implementation.addition(uint256,uint256).selector;

    callAddition@withrevert(proxy, methodsig, x, y);

    assert !lastReverted;
}
