// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.8.0;

import {ERC20} from "../../../solmate/tokens/ERC20.sol";
import {ERC4626} from "../../../solmate/tokens/ERC4626.sol";
import {Owned} from "../../../solmate/auth/Owned.sol";

/// @notice A harness implementation for the ERC4626 vault standard
/// @dev This contract implements the `totalAssets()` function by accounting 
///      every change to the contract's balance. 
///      The owner can account the accrued rewards using the `accrueRewards()` function.
contract ERC4626AccountingHarness is ERC4626 {
    constructor(address _asset) 
        ERC4626(ERC20(_asset), "ERC4626 Harness", "ERC4626H") 
        
    { owner = msg.sender ; }

    uint public currentBalance;
    address public owner;

    function beforeWithdraw(uint256 assets, uint256) internal override {
        // if no supply left - then start from fresh - no balance
        if (totalSupply == previewWithdraw(assets))
            currentBalance = 0;
        else
            currentBalance -= assets;
    }

    function afterDeposit(uint256 assets, uint256) internal override {
        currentBalance += assets;
    }


    function totalAssets() public view override returns (uint256) {
        return currentBalance;
    }

    function userAssets(address user) public view returns (uint256) { // harnessed
        return asset.balanceOf(user);
    }
}
