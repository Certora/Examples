pragma solidity ^0.8.13;
import {ERC20} from "../src/ERC20.sol";
import {ConstantProductPool} from "../src/ConstantProductPoolMini.sol";

contract CPPSetup is ConstantProductPool {
    ConstantProductPool public cpp;

    constructor(address _token0, address _token1) ConstantProductPool(_token0,_token1) {
    }
    
    function externalTransfer(uint256 amount0, uint256 amount1) external {
        ERC20(token0).transferFrom(msg.sender, address(this), amount0);
        ERC20(token1).transferFrom(msg.sender, address(this), amount1);
    }

    function transferAndMint(uint256 amount0, uint256 amount1) external {
        ERC20(token0).transferFrom(msg.sender, address(this), amount0);
        ERC20(token1).transferFrom(msg.sender, address(this), amount1);
        mint();
    }


    function transferAndSwap(bool fromToken0, uint256 amount) external {
        address tokenIn = fromToken0 ? token0 : token1;
        ERC20(tokenIn).transferFrom(msg.sender, address(this), amount);
        swap(fromToken0);
    }

    

}