/***
 * # Native balances Example
 *
 * This is an example specification for using structs.
 */


// using BankAccountRecord as baccountrecord;


//// Basic rules ////////////////////////////////////////////////////

// This rule fails because when msg.value > 0 nativeBalances[e.msg.sender] decreases by `multiplicate` 
// but nativeBalances[adr]
// does not change because the if condition in `multiplicate` does not hold as this.balance is already increased
// by msg.value.
rule senderBalanceStaysTheSameShould(){
    env e;
    storage init = lastStorage;
    address adr;

    mathint balanceBefore = nativeBalances[e.msg.sender] + nativeBalances[adr];
    multiplicate(e, adr);
    assert(assert_uint256(balanceBefore) == assert_uint256(nativeBalances[e.msg.sender] + nativeBalances[adr]));
}

// This rule fails because the if condition in `multiplicate` never happens so adr's balance does not change.
rule receiverGetsAtLeastMsgValue(){
    env e;
    address receiver;

    mathint balanceBefore = nativeBalances[receiver];
    multiplicate(e, receiver);
    assert(nativeBalances[receiver] >= assert_uint256(balanceBefore + e.msg.value ));
}

// This rule fails because the if condition in `multiplicate` never happens so adr's balance does not change.
rule receiverBalanceChanges() {
    env e;
    require e.msg.value > 0;
    address receiver;

    mathint balanceBefore = nativeBalances[receiver];
    multiplicate(e, receiver);
    assert(nativeBalances[receiver] > assert_uint256(balanceBefore + e.msg.value) );
}

// This shows that rule receiverBalanceChanges never holds.
rule witnessForReceiverBalanceChanges() {
    env e;
    require e.msg.value > 0;
    address receiver;

    mathint balanceBefore = nativeBalances[receiver];
    multiplicate(e, receiver);
    satisfy(nativeBalances[receiver] > assert_uint256(balanceBefore + e.msg.value) );
}

// In the witness to the rule `witnessForReceiverBalanceChanges` the receiver is
// this, because payable `multiplicate` tranfers msg.value from msg.sender to this.
rule receiverBalancesIncreasesIffSenderDecreases() {
    env e;
    require e.msg.value > 0;
    address receiver;

    uint256 receiverBalanceBefore = nativeBalances[receiver];
    uint256 senderBalanceBefore = nativeBalances[e.msg.sender];

    multiplicate(e, receiver);
    satisfy((nativeBalances[receiver] >  receiverBalanceBefore) <=>
            (nativeBalances[e.msg.sender]) < senderBalanceBefore);
}

