// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.8.0;

import {ERC20} from "../../../solmate/tokens/ERC20.sol";
import {ERC4626} from "../../../solmate/tokens/ERC4626.sol";
import {Owned} from "../../../solmate/auth/Owned.sol";

/// @notice A harness implementation for the ERC4626 vault standard
/// @dev This contract is vulnerable to a first depositor attack 
contract ERC4626Broken is ERC4626 {
    constructor(address _asset) 
        ERC4626(ERC20(_asset), "ERC4626 Harness", "ERC4626H") 
        
    { }

    function totalAssets() public view override returns (uint256) {
        return asset.balanceOf(address(this));
    }

    function userAssets(address user) public view returns (uint256) { // harnessed
        return asset.balanceOf(user);
    }
}
