using Asset as underlying;
using SymbolicFlashLoanReceiver as flashLoanReceiver;

methods
 {
      // pool's erc20 function
     function balanceOf(address) external returns(uint256) envfree;
     function totalSupply() external returns(uint256) envfree;
     function underlying.balanceOf(address) external returns(uint256) envfree;

     function _.executeOperation(uint256,uint256,address) external => DISPATCHER(true);
     function _.transfer(address, uint256) external returns (bool) => DISPATCHER(true);
     function _.transferFrom(address, address, uint256) external returns (bool) => DISPATCHER(true);
     function _.deposit(uint256) external returns(uint256)  => DISPATCHER(true);
     function _.withdraw(uint256) external returns (uint256)  => DISPATCHER(true);
     function _.FlashLoan(address, uint256)  external => DISPATCHER(true);
     function amountToShares(uint256 amount) external returns (uint256) envfree;
     function sharesToAmount(uint256 amount) external returns (uint256) envfree;
 };

    definition absDiff(mathint x, mathint y) returns mathint = x > y ? x - y : y - x;


     
invariant totalSupply_LE_balance();
    function totalSupply() <= underlying.balanceOf(currentContract) external;
{
        preserved with (env e){
        require e.msg.sender != currentContract;
         };
}

invariant totalSupply_vs_balance()
    totalSupply() == 0 <=> underlying.balanceOf(currentContract) == 0
{
        preserved with (env e){
        require e.msg.sender != currentContract;
         }
}

rule deposit_GR_zero(){ //failing due to bugs in the code
    env e;
    require e.msg.sender != currentContract;

    uint256 amount;
    uint256 amountMinted = deposit(e,amount);

    assert amount > 0 <=> amountMinted > 0;
}

rule more_user_shares_less_underlying(method f) // failures need to check
        filtered {f -> f.selector != sig:transfer(address,uint256).selector && f.selector != sig:transferFrom(address,address,uint256).selector && !f.isView }
        {
    env e;

    uint256 Underlying_balance_before = underlying.balanceOf(e.msg.sender);
    uint256 User_balance_before = balanceOf(e.msg.sender);

    global_requires(e);

        calldataarg args;
        f(e,args);

    uint256 Underlying_balance_after = underlying.balanceOf(e.msg.sender);
    uint256 User_balance_after = balanceOf(e.msg.sender);

    assert User_balance_after > User_balance_before <=> Underlying_balance_after < Underlying_balance_before;
    assert User_balance_after < User_balance_before <=> Underlying_balance_after > Underlying_balance_before;
}

rule more_shares_more_withdraw(){ //failing
    env e;

    uint256 sharesX;
    uint256 sharesY;
    uint256 amountX;
    uint256 amountY;

    global_requires(e);

    storage init = lastStorage;

    amountX =  withdraw(e,sharesX);
    amountY =  withdraw(e,sharesY) at init;

    assert sharesX > sharesY => amountX >= amountY;
}

rule flashLoan_adds_value(address receiver, uint256 amount){
    env e;

    global_requires(e);
    uint256 totalSupply_pre = totalSupply();
    // require totalSupply_pre != 0;
    uint256 balance_pre = underlying.balanceOf(currentContract);
    require balance_pre == 2 * totalSupply_pre;
    FlashLoan(e,receiver,amount);
    uint256 totalSupply_post = totalSupply();
    // require totalSupply_post != 0;
    uint256 balance_post = underlying.balanceOf(currentContract);
    
    assert flashLoanReceiver.callBackOption(e) == 0 => balance_post > balance_pre;
    //assert balance_post/totalSupply_post >= balance_pre/totalSupply_pre;
    assert balance_post * totalSupply_pre >= balance_pre * totalSupply_post;
}

rule user_solvency(address user){
env e;

require user != currentContract && user != flashLoanReceiver.to(e) && user != flashLoanReceiver;
global_requires(e);

uint256 shares1 = balanceOf(user);
uint256 poolBalance1 = underlying.balanceOf(currentContract);
uint256 supply1 = totalSupply();

require supply1 != 0;
// require shares1 < 2^128 && poolBalance1 < 2^128;

mathint withdrawableAmount1 = shares1 * poolBalance1 / supply1;
require withdrawableAmount1 * supply1 == shares1 * poolBalance1;

uint256 userBalance1 = underlying.balanceOf(user);
mathint total_pre = withdrawableAmount1 + userBalance1;

uint256 amount;

FlashLoan(e,flashLoanReceiver, amount);

uint256 shares2 = balanceOf(user);
uint256 poolBalance2 = underlying.balanceOf(currentContract);
uint256 supply2 = totalSupply();

require supply2 != 0;
require shares1 <= supply1 && shares2 <= supply2; // invariant shares <= supply
// require shares2 < 2^128 && poolBalance2 < 2^128;

mathint withdrawableAmount2 = shares2 * poolBalance2 / supply2;
require withdrawableAmount2 * supply2 == shares2 * poolBalance2;

uint256 userBalance2 = underlying.balanceOf(user);
mathint total_post = withdrawableAmount2 + userBalance2;

uint256 premium = calc_premium(e,amount);
mathint fee_for_LP = premium*shares2/supply2 + 1;
require fee_for_LP > 0;
mathint fee_for_none_LP = premium ;
require fee_for_none_LP > 0;
// if (fee_for_none_LP == 0) {fee_for_none_LP = 1;}

// assert shares1 == shares2;
// assert poolBalance2 > poolBalance1 => f.selector == sig:FlashLoan(address flashLoanReceiver,uint256 amount).selector;
// assert total_post > total_pre =>  total_post - total_pre <= fee  && user!=e.msg.sender;
// assert toatal_post < total_pre => total_pre - total_post <= fee  && user==e.msg.sender;

mathint diffTotals = sub_math(total_post, total_pre);
assert (user != e.msg.sender && shares1 != 0) => (diffTotals <= fee_for_LP);
mathint diffTotals2 = sub_math(total_pre, total_post);
assert (user == e.msg.sender && shares1 != 0) => (diffTotals2 < fee_for_LP);
assert (user != e.msg.sender && shares1 == 0) => (total_pre == total_post);
assert (user == e.msg.sender && shares1 == 0) => (diffTotals2 == fee_for_none_LP);
}

rule user_solvency_without_flashloan(address user, method f)filtered { f-> /*f.selector != sig:FlashLoan(address,uint256).selector  
&& */ f.selector != sig:transferFrom(address,address,uint256).selector }{
env e;
// require user != e.msg.sender;
require user != currentContract && user != flashLoanReceiver ;
global_requires(e);

uint256 shares1 = balanceOf(user);
//require shares1 != 0 => shares1 > 1000;
uint256 poolBalance1 = underlying.balanceOf(currentContract);
uint256 supply1 = totalSupply();
require shares1 <= supply1; // invariant shares <= supply

//require supply1 != 0;
// require shares1 < 2^128 && poolBalance1 < 2^128;

uint256 withdrawableAmount1 = sharesToAmount(shares1);
uint256 userBalance1 = underlying.balanceOf(user);
mathint total_pre = withdrawableAmount1 + userBalance1;

calldataarg args;
f(e,args);

uint256 shares2 = balanceOf(user);
uint256 poolBalance2 = underlying.balanceOf(currentContract);
uint256 supply2 = totalSupply();

//require supply2 != 0;
// require shares2 < 2^128 && poolBalance2 < 2^128;

uint256 withdrawableAmount2 = sharesToAmount(shares2);
uint256 userBalance2 = underlying.balanceOf(user);
mathint total_post = withdrawableAmount2 + userBalance2;

//mathint max_diff = absDiff(total_pre,total_post);
//mathint costOfOneShare = poolBalance1/supply1 +1; //cost of one share
//assert max_diff < costOfOneShare;
assert (e.msg.sender == user ) => total_pre >= total_post;
assert (e.msg.sender != user ) => total_pre <= total_post;
// uint256 temp = add(total_post,2);
// assert total_pre <= temp; //add(total_post,10000000);
//  ||
//        total_pre == sub_math(total_post,10000000) ||
//        total_pre == total_post;
}

function global_requires(env e){
    require e.msg.sender != currentContract;
    require e.msg.sender != flashLoanReceiver.to(e);
    require e.msg.sender != flashLoanReceiver;
    requireInvariant totalSupply_vs_balance();
    requireInvariant totalSupply_LE_balance();
    // address user;
    // requireInvariant balance_SE_supply(user);
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
