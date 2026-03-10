// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Tokens.sol";

struct TokenHolder {
    address token;
    uint256 weight;
}

contract BasicVault {
    address public primaryToken;
    address public immutable immutableToken;
    TokenHolder public holder;
    address[2] public fixedTokens;

    constructor(address _immutableToken) {
        immutableToken = _immutableToken;
    }

    function getPrimaryValue() external view returns (uint) {
        return IToken(primaryToken).getValue();
    }

    function getImmutableValue() external view returns (uint) {
        return IToken(immutableToken).getValue();
    }

    function getHolderValue() external view returns (uint) {
        return IToken(holder.token).getValue();
    }

    function getFixedTokenValue(uint i) external view returns (uint) {
        return IToken(fixedTokens[i]).getValue();
    }
}
