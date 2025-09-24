// Represents a symbolic/dummy ERC20 token

// SPDX-License-Identifier: agpl-3.0
pragma solidity ^0.8.0;

import "../../src/ERC20.sol";

contract DummyERC20B is ERC20 {
    string public name = "ERC20B";
    function mint(address account, uint256 amount) external  {
        _mint(account,amount);
    } 
}