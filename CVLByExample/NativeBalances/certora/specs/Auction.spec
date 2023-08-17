/***
 * # Native balances Example
 *
 * This is an example specification for using nativeBalances.
 */


//// Basic rules ////////////////////////////////////////////////////


rule bidSuccessfully() {

    env e;
    address to;
    uint256 balanceBefore = nativeBalances[currentContract];
    bid(e,to);
    assert to!=currentContract =>  nativeBalances[currentContract] >= balanceBefore;
}

