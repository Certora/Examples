using Asset as underlying;

methods
{
    function underlying.balanceOf(address)           external returns(uint256) envfree;
    function depositedAmount()                       external returns(uint256) envfree;
}

strong invariant strongDepositedAmountLessThanContractUnderlyingAsset()
    depositedAmount() <= underlying.balanceOf(currentContract)
    filtered { f -> f.selector == sig:flashLoan(address,uint256).selector }
    {
        preserved with(env e) {
            require e.msg.sender != currentContract;
        }
    }

weak invariant weakDepositedAmountLessThanContractUnderlyingAsset()
    depositedAmount() <= underlying.balanceOf(currentContract)
    filtered { f -> f.selector == sig:flashLoan(address,uint256).selector }
    {
        preserved with(env e) {
            require e.msg.sender != currentContract;
        }
    }