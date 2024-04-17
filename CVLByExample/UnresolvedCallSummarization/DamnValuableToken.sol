pragma solidity ^0.8.20;

import "./ERC20.sol";

contract DamnValuableToken is ERC20 {

    // Decimals are set to 18 by default in `ERC20`
    constructor() public ERC20("DamnValuableToken", "DVT", 32) {
        mint(msg.sender, 2**256 - 1);
    }
}