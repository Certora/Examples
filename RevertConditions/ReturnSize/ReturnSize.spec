methods{
    function _.calledFunction(uint) external => NONDET;
}

rule returnSizeRevertConditions()
{
    env e;
    address lib;
    uint x;

    callerFunction@withrevert(e, lib, x);
    bool isReverted = lastReverted;

    assert !isReverted <=> e.msg.value == 0;
}