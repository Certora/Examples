// SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.13;
import "./ERC20.sol";
import "./CurveToken.sol";

contract CurveTokenExample is CurveToken, ERC20{

    constructor() ERC20("ExampleLPToken", "ExCrvLP") {}

    function mint(address to, uint256 value) external returns(bool){
        _mint(to, value);
        return true;
    }
    function burnFrom(address to, uint256 value) external returns(bool){
        _burn(to, value);
        return true;
    }
}
