using Test as test;

rule checkSendEth() {
    env e;
    address owner;

    require e.msg.value > 0;
    test.sendEth(e);
    assert test.getEth(e) > 0;
}
