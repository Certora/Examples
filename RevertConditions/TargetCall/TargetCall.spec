methods{
    function _.doSomething(uint) external => NONDET;
}

rule targetCallRevertConditions()
{
    env e;
    uint x;

    forward@withrevert(e, x);
    bool isReverted = lastReverted;

    assert !isReverted <=> e.msg.value == 0;
}