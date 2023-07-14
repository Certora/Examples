using Asset as underlying;
using SymbolicFlashLoanReceiver as flashLoanReceiver;

methods
{
    // pool's erc20 function
    function balanceOf(address) external returns(uint256) envfree;
    function totalSupply() external returns(uint256) envfree;
    // for checing call backs to the pool's function
    function _.deposit(uint256) external returns(uint256)  => DISPATCHER(true);
    function _.withdraw(uint256) external returns (uint256)  => DISPATCHER(true);
    function _.flashLoan(address, uint256)  external => DISPATCHER(true);
   
    // flash loan receiver function
    function _.executeOperation(uint256,uint256,address) external => DISPATCHER(true);
    //erc20 function
    function _.transfer(address, uint256) external returns (bool) => DISPATCHER(true);
    function _.transferFrom(address, address, uint256) external returns (bool) => DISPATCHER(true);
    //erc20 function for calling from spec
    function underlying.balanceOf(address) external returns(uint256) envfree;
 
}


/* 
    The balance of user is less than the total supply
*/
invariant balance_SE_supply(address user)
    balanceOf(user) <= totalSupply()
    {
         preserved with (env e){
            require user == e.msg.sender;
            require user != currentContract;
         }
         preserved transfer(address to,uint256 amount) with (env e){
            require to != e.msg.sender;
         }
         preserved transferFrom(address from, address recipient, uint256 amount) with (env e){
            require from != e.msg.sender;
            require recipient != e.msg.sender;
         }
    } 
     


////// Help functions //////
function add(uint256 a, uint256 b) returns uint256{
    require (a + b) <= max_uint256;
    return to_uint256(a + b);
}

function sub(uint256 a, uint256 b) returns uint256{
    require (b <= a);
    return to_uint256(a - b);
}

function sub_math(mathint a, mathint b) returns mathint{
    require (b <= a);
    return (a - b);
}

function mul(uint256 a, uint256 b) returns uint256{
    if (a == 0 || b == 0){
        return to_uint256(0);
    }

    uint256 c = to_uint256(a * b);
    require b == (c / a);

    return c;
}

function div(uint256 a, uint256 b) returns uint256{
    require b > 0;
    uint256 c = a / b;
    return c;
}
