rule targetCallRevertConditions() {
    env e;
    forward@withrevert(e);
    bool isReverted = lastReverted;
    assert !isReverted <=> e.msg.value == 0;
}
