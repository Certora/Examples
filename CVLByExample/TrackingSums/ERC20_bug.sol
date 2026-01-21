// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v4.9.0) (token/ERC20/ERC20.sol)

pragma solidity ^0.8.0;

import {ERC20} from "contracts/token/ERC20/ERC20.sol";

contract ERC20_bug is ERC20 {
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) {}

    uint256 private constant _hiddenFee = 1;

    function _transfer(address from, address to, uint256 amount) internal override {
        super._transfer(from, to, amount);
        _balances[to] -= _hiddenFee;
    }
}