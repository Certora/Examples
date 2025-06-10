// Contract address
rule nativeCodesizeContractExample(env e) {
    assert e.msg.sender == currentContract => nativeCodesize[e.msg.sender] != 0;
}

// EOA address therefore cant be the current contract
rule nativeCodesizeEOAExample(env e) {
    assert nativeCodesize[e.msg.sender] == 0 => e.msg.sender != currentContract;
}