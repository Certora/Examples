using RootStruct as rootStruct;

methods {
    function workOnS(uint x, RootStruct.Simple s) external => workOnSCVL(x, s);
}

function workOnSCVL(uint x, RootStruct.Simple s) {
    havoc rootStruct.s.b1;
    require rootStruct.s.b1 == (x > 3);
}

rule checkWorkOnS(uint x) {
    require x < 3;
    env e;
    workOnSExt(e, x);
    assert rootStruct.s.b1;
}
