pragma solidity ^0.8.13;

interface CurveToken{
    function mint(address to, uint256 value) external returns(bool);
    function burnFrom(address to, uint256 value) external returns(bool);
}
