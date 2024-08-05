using Asset as underlying;

methods
{
    function totalSupply()                           external returns(uint256) envfree;
    function flashLoan(address, uint256)             external;
    function underlying.balanceOf(address)           external returns(uint256) envfree;
}

// Define strong invariant
strong invariant strongTotalSharesLessThanUnderlyingBalance()
    totalSupply() <= underlying.balanceOf(currentContract)
    filtered { f -> f.selector == sig:flashLoan(address,uint256).selector }
    

// Define weak invariant
weak invariant weakTotalSharesLessThanUnderlyingBalance()
    totalSupply() <= underlying.balanceOf(currentContract)
    filtered { f -> f.selector == sig:flashLoan(address,uint256).selector }
    