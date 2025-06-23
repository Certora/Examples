methods {
    function justANonPayableFunction() external;
}

rule NonPayableRevertingConditions() {
    env e;
    justANonPayableFunction@withrevert(e);
    assert lastReverted <=> e.msg.value > 0;
}

rule NonPayableRevertExample() {
    env e;
    justANonPayableFunction@withrevert(e);
    assert !lastReverted;
}
