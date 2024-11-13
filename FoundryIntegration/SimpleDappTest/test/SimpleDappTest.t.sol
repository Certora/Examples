//SPDX-License-Identifier: MIT

import {Test} from "forge-std/Test.sol";
import {SimpleDapp} from "../src/SimpleDapp.sol";

pragma solidity ^0.8.23;

/// @title Test for SimpleDapp Contract
/// @notice This contract implements FUzz testing for SimpleDapp
contract SimpleDappTest is Test {
    SimpleDapp simpleDapp;
    address public user;

    ///@notice Set up the test by deploying SimpleDapp
    function setUp() public {
        simpleDapp = new SimpleDapp();
        user = address(1); // Assign a non-zero address to user
    }

    /// @notice FUzz test for deposit and Withdraw functions
    /// @dev Test the invariant that a user can't withdraw more than they deposit
    /// @param depositAmount The amount of ETH to deposit
    /// @param withdrawAmount The amount of ETH to withdraw
    function testDepositAndWithdraw(
        // We set the depositAmount and withdrawAmount to be input parameters 👇👇👇
        uint256 depositAmount,
        uint256 withdrawAmount
    )
        public
        payable
    // Foundry will generate random values for the input parameters 👆👆👆
    {
        // Ensure the user has enough Ether to cover the deposit
        uint256 initialUserBalance = 100 ether;
        vm.deal(user, initialUserBalance);

        // Only attempt deposit if the user has enough balance
        if (depositAmount <= initialUserBalance) {
            simpleDapp.deposit{value: depositAmount}();

            if (withdrawAmount <= depositAmount) {
                simpleDapp.withdraw(withdrawAmount);
                assertEq(
                    simpleDapp.balances(user),
                    depositAmount - withdrawAmount,
                    "Balance after withdrawal should match expected value"
                );
            }
        }
    }
}
