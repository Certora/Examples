methods {
     unresolved external in A.execute(address x, bytes calldata data) => NONDET;
}

rule NonDet {
    bool field_before = currentContract.a_field;
    env e;
    address x;
    bytes data;
    currentContract.execute(e, x, data);
    assert currentContract.a_field == field_before, "only the return value is nondet, the contract was not havoced.";
} 
