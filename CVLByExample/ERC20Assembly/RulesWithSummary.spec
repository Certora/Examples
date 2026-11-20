import "ERC20UtilsSummary.spec";
import "ETH.spec";

using main as main;

function tokensAreNotETH() {
    require erc20A != ETH();
    require erc20B != ETH();
    require erc20C != ETH();
}

rule call_through_transfer_ERC20(env e, address token) {
    tokensAreNotETH();
    require token != ETH();

    address recipient;
    uint256 amount;
    env e1;
    mathint recipient_balance_pre = main.getBalance(e1, token, recipient);
        bool result = main.safeTransfer(e, token, recipient, amount);
    mathint recipient_balance_post = main.getBalance(e1, token, recipient);

    /// If the transfer is successful and the recipient is not the contract, 
    /// then the balance must increase by amount. Otherwise, the balance doesn't change.
    assert (result && main != recipient) => recipient_balance_post - recipient_balance_pre == to_mathint(amount);
    assert !(result && main != recipient) => recipient_balance_post == recipient_balance_pre;
}

rule call_through_transfer_ETH(env e, address token) {
    tokensAreNotETH();
    require token == ETH();

    address recipient;
    uint256 amount;
    mathint recipient_native_pre = nativeBalances[recipient];
        bool result = main.safeTransfer(e, token, recipient, amount);
    mathint recipient_native_post = nativeBalances[recipient];

    /// If the transfer is successful and the recipient is not the contract, 
    /// then the balance must increase by amount. Otherwise, the balance doesn't change.
    assert (result && main != recipient) => recipient_native_post - recipient_native_pre == to_mathint(amount);
    assert !(result && main != recipient) => recipient_native_post == recipient_native_pre;
}

rule call_through_approve(env e, address token, address to) {
    tokensAreNotETH();

    main.approve(e, token, to);

    satisfy token != ETH();
}