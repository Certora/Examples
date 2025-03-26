/***
This example demonstrate a critical bug found with the Certora Prover 
***/

// reference from the spec to additional contracts used in the verification 
using DummyERC20A as _token0;
using DummyERC20B as _token1;
using ConstantProductPool as _pool;


/*
    Declaration of methods that are used in the rules. `envfree` indicates that
    the method is not dependent on the environment (`msg.value`, `msg.sender`).
    Methods that are not declared here are assumed to be dependent on the
    environment.
*/

methods{
    function token0() external returns (address) envfree;
    function token1() external returns (address) envfree;
    function allowance(address,address) external returns (uint256) envfree;
    function totalSupply() external returns (uint256)  envfree;
    
    function DummyERC20A.balanceOf(address) external returns (uint256)  envfree; 
    function DummyERC20B.balanceOf(address) external returns (uint256)  envfree; 
    function DummyERC20A.allowance(address,address) external returns (uint256)  envfree; 
    function DummyERC20B.allowance(address,address) external returns (uint256)  envfree; 
    //external calls to be resolved by dispatcher - taking into account all available implementations 
    function _.transfer(address recipient, uint256 amount) external => DISPATCHER(true);
    function _.balanceOf(address) external => DISPATCHER(true);
    // mathematical summary
    function Math.sqrt(uint256 y) internal returns (uint256) => floorSqrt(y);
    
}


// A precise summarization of sqrt
ghost floorSqrt(uint256) returns uint256 {    
                // sqrt(x)^2 <= x
    axiom forall uint256 x. floorSqrt(x)*floorSqrt(x) <= to_mathint(x) && 
                // sqrt(x+1)^2 > x 
                (floorSqrt(x) + 1)*(floorSqrt(x) + 1) > to_mathint(x);
}

// a cvl function for precondition assumptions 
function setup(env e){
    address zero_address = 0;
    uint256 MINIMUM_LIQUIDITY = 1000;
    require totalSupply() == 0 || currentContract._balances[zero_address] == MINIMUM_LIQUIDITY;
    require currentContract._balances[zero_address] + currentContract._balances[e.msg.sender] <= totalSupply();
    require _token0 == token0();
    require _token1 == token1();
    require e.msg.sender != currentContract;
}

invariant allowanceOfPoolAlwaysZero(address a)
    _token0.allowance(_pool, a) == 0 && _token1.allowance(_pool, a) == 0
    {
        preserved with (env e){
         setup(e);
        }
    }


/*
Property: For both token0 and token1 the balance of the system is at least as much as the reserves.

This property is implemented as an invariant. 
Invariants are defined as a specification of a condition that should always be true once an operation is concluded.
In addition, the invariant also checks that it holds immediately after the constructor of the code runs.

*/

invariant balanceGreaterThanReserve()
    (currentContract.reserve0 <= _token0.balanceOf(currentContract))&&
    (currentContract.reserve1 <= _token1.balanceOf(currentContract))
    {
        preserved with (env e){
         setup(e);
         requireInvariant allowanceOfPoolAlwaysZero(e.msg.sender);
        }

        
    }


/*
Property: Integrity of totalSupply with respect to the amount of reserves. 

This is a high level property of the system - the ability to pay back liquidity providers.
If there are any LP tokens (the totalSupply is greater than 0), then neither reserves0 nor reserves1 should ever be zero (otherwise the pool could not produce the underlying tokens).

This invariant catches the original bug in Trident where the amount to receive is computed as a function of the balances and not the reserves.

Formula:
    (totalSupply() == 0 <=> getReserve0() == 0) &&
    (totalSupply() == 0 <=> getReserve1() == 0)
*/

invariant integrityOfTotalSupply()
    
    (totalSupply() == 0 <=> currentContract.reserve0 == 0) &&
    (totalSupply() == 0 <=> currentContract.reserve1 == 0)
    {
        preserved with (env e){
            requireInvariant balanceGreaterThanReserve();
            setup(e);
        }
    }
