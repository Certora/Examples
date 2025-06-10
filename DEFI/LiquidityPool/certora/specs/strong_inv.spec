using Asset as underlying;

methods {
    function underlying.balanceOf(address) external returns (uint256) envfree;
    function depositedAmount() external returns (uint256) envfree;
}

invariant strongDepositedAmountLessThanContractUnderlyingAsset() depositedAmount() <= underlying.balanceOf(currentContract) {
    preserved with (env e) {
        require e.msg.sender != currentContract;
 }

invariant weakDepositedAmountLessThanContractUnderlyingAsset() depositedAmount() <= underlying.balanceOf(currentContract) {
    preserved with (env e) {
        require e.msg.sender != currentContract;
 }