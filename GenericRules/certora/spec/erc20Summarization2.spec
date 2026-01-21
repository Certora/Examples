methods {
   // function _.name() external => NONDET DELETE(true);
   // function _.symbol() external => NONDET DELETE(true);
    function _.decimals() external => NONDET;
    function _.totalSupply() external => erc20_totalSupply[calledContract] expect uint256 ;
    function _.balanceOf(address u) external => erc20_balances[calledContract][u] expect uint256;
    function _.allowance(address,address) external => NONDET; //TODO 
    function _.approve(address,uint256) external => NONDET; //TODO
    function _.transfer(address to, uint256 amount) external with (env e) => 
                    erc20_transfer(calledContract, e, to, amount) expect bool;
    function _.transferFrom(address from, address to, uint256 amount) external with (env e) => 
                    erc20_transferFrom(calledContract, e, from, to, amount) expect bool;
}

methods {
    function transfer(address to, uint256 amount) external returns (bool);
}

function erc20_transfer(address token, env e, address to, uint256 amount) returns bool {
   if token == currentContract {
        return transfer(e, to, amount);
    }
    else
    if (erc20_balances[token][e.msg.sender] <  amount)
        return false;
    else {
        erc20_balances[token][e.msg.sender] = assert_uint256(erc20_balances[token][e.msg.sender] - amount);
        erc20_balances[token][to] = require_uint256(erc20_balances[token][to] + amount);
        return true;
    }
        
}

function erc20_transferFrom(address token, env e, address from, address to, uint256 amount) returns bool {
   if token == currentContract {
        return transferFrom(e, from, to, amount);
    }
    //todo allowance... 
    else 
    if (erc20_balances[token][from] <  amount)
        return false;
    else {
        erc20_balances[token][from] = assert_uint256(erc20_balances[token][from] - amount);
        erc20_balances[token][to] = require_uint256(erc20_balances[token][to] + amount);
        return true;
    }
        
}

// tracking totalSupply for each erc20 address
ghost mapping(address => uint256) erc20_totalSupply;

// tracking balance for each erc20 address, a mapping for users to 
ghost mapping(address => mapping(address => uint256)) erc20_balances;

// tracking sum balance for each erc20 address, a mapping for users to 
ghost mapping(address => uint256) erc20_sum_balances;


// @title invariants to use as needed
invariant sumBalancesIsTotalSupply() 
     forall address t. erc20_sum_balances[t]==erc20_totalSupply[t];


invariant singleBalance() 
    forall address t. forall address u. erc20_balances[t][u]<=erc20_totalSupply[t];


