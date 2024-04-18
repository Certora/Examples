methods{
    function _.execute(uint) external => NONDET;
}

rule returnSizeRevertConditions()
{
    env e;
    address contract;
    uint x;

    callerFunction@withrevert(e, contract, x);
    bool isReverted = lastReverted;

    assert !isReverted <=> e.msg.value == 0;
}