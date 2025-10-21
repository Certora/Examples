
using Asset as underlying;

methods
{
    function balanceOf(address)                      external returns(uint256) envfree;
    function totalSupply()                           external returns(uint256) envfree;
    function depositedAmount()                       external returns(uint256) envfree;
    function underlying.balanceOf(address)           external returns(uint256) envfree;
    function calcPremium(uint256) external returns (uint256) envfree;
    function _.executeOperation(uint256 amount,uint256 premium,address initiator) external => NONDET;
}

/** user pays exactly premium for the flash loan */
rule flashLoanIntegrity(env e){
    require e.msg.sender != currentContract && e.msg.sender != currentContract.owner;
    address receiver;
    uint256 amount;

    uint256 userUnderlyingBalanceBefore  = underlying.balanceOf(e.msg.sender);
    
    flashLoan(e, receiver, amount);

    uint256 userUnderlyingBalanceAfter = underlying.balanceOf(e.msg.sender);
    
    
    assert userUnderlyingBalanceAfter == userUnderlyingBalanceBefore - calcPremium(amount);

}

invariant assetsMoreThanSupply()
    depositedAmount() >= totalSupply();
    

rule monotonicSupplyRate( method f) 
{
    env e;
    calldataarg args;
    require e.msg.sender != currentContract && e.msg.sender != currentContract.owner;

    requireInvariant assetsMoreThanSupply();
    
    uint256 totalSupplyBefore = totalSupply();
    uint256 balanceBefore = depositedAmount();

    f(e,args);

    uint256 totalSupplyAfter = totalSupply();
    uint256 balanceAfter = depositedAmount();

    assert totalSupplyBefore!= 0 => 
    balanceAfter * totalSupplyBefore >= balanceBefore * totalSupplyAfter ;
}