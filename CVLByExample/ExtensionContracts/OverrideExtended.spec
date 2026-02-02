using Extended as Extended;

rule overriddenReplaced {
    env e;
    assert Extended.foo(e) == "Extender.foo";
}

rule notOverriddenNotReplaced {
    env e;
    assert Extended.bar(e) == "Extended.bar";
}

use builtin rule sanity;
