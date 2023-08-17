/***
 * # Native balances Example
 *
 * This is an example specification for using nativeBalances.
 */


//// Basic rules ////////////////////////////////////////////////////

// Since the function `multiplicate` is payable, the balance of `this` is already increased by msg.value when
// reaching the `if` in the function. Therefore when msg.value > 0 the if condition in `multiplicate` does not hold. 
// The rule fails because nativeBalances[this] increases by the function `multiplicate` 
// but nativeBalances[adr] does not change.
rule senderBalanceStaysTheSameShouldFail(){
    env e;
    storage init = lastStorage;
    address adr;

    mathint balanceBefore = nativeBalances[e.msg.sender] + nativeBalances[adr];
    // At the entrance to `multiplicate` balanceOf(this) = balanceOf(this) at init + msg.value
    multiplicate(e, adr);
    assert(assert_uint256(balanceBefore) == assert_uint256(nativeBalances[e.msg.sender] + nativeBalances[adr]),
    "Sum of balances of sender and reciever changes");
}

// This rule fails because the if condition in `multiplicate` never happens so receiver's balance does not change.
rule receiverGetsAtLeastMsgValueShouldFail(){
    env e;
    address receiver;

    mathint balanceBefore = nativeBalances[receiver];
    multiplicate(e, receiver);
    assert(nativeBalances[receiver] >= assert_uint256(balanceBefore + e.msg.value ),
    "receiver gets less than msg.value");
}

// This rule fails because the if condition in `multiplicate` never holds so adr's balance does not change.
rule receiverBalanceChangesShouldFail() {
    env e;
    require e.msg.value > 0;
    address receiver;

    mathint balanceBefore = nativeBalances[receiver];
    multiplicate(e, receiver);
    assert(nativeBalances[receiver] > assert_uint256(balanceBefore + e.msg.value),
        "Receiver balance does not change" );
}

// This shows that rule receiverBalanceChanges never holds.
rule witnessForReceiverBalanceChangesVacuous() {
    env e;
    require e.msg.value > 0;
    address receiver;

    mathint balanceBefore = nativeBalances[receiver];
    multiplicate(e, receiver);
    satisfy(nativeBalances[receiver] > assert_uint256(balanceBefore + e.msg.value) );
}

// This rule fails because `multiplicate` tranfers msg.value from msg.sender to this and the if does not hold
// so the `transfer` never executes and therefore the balance of `receiver` != this never increases so 
// (nativeBalances[receiver] >  receiverBalanceBefore) never holds.
rule receiverBalancesIncreasesIffSenderDecreasesShouldFail() {
    env e;
    require e.msg.value > 0;
    address receiver;

    uint256 receiverBalanceBefore = nativeBalances[receiver];
    uint256 senderBalanceBefore = nativeBalances[e.msg.sender];

    multiplicate(e, receiver);
    assert((nativeBalances[receiver] >  receiverBalanceBefore) <=>
            (nativeBalances[e.msg.sender] < senderBalanceBefore),
            "Balance of sender increases if and only if balance of receiver increases");
}

// In the witness to the rule `receiverBalancesIncreasesIffSenderDecreases` the receiver is
// this, because payable `multiplicate` tranfers msg.value from msg.sender to this.
rule witnessReceiverBalancesIncreasesIffSenderDecreases() {
    env e;
    require e.msg.value > 0;
    address receiver;

    uint256 receiverBalanceBefore = nativeBalances[receiver];
    uint256 senderBalanceBefore = nativeBalances[e.msg.sender];

    multiplicate(e, receiver);
    satisfy((nativeBalances[receiver] >  receiverBalanceBefore) <=>
            (nativeBalances[e.msg.sender]) < senderBalanceBefore);
}

