// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Tokens.sol";
import {TokenHolder} from "./BasicVault.sol";

contract AdvancedRegistry {
    // Multi-target dispatch: address could be one of several contracts
    address public multiTarget;

    // Dynamic array
    address[] public dynamicTokens;

    // Uint-keyed mapping
    mapping(uint256 => address) public tokenMap;

    // Address-keyed mapping (contract alias can be used as key in spec)
    mapping(address => address) public addrMap;

    // For wildcard + concrete precedence demo
    address[] public precedenceTokens;

    // Bytes4-keyed mapping
    mapping(bytes4 => address) public bytes4Map;

    // Nested mapping
    mapping(uint256 => mapping(uint256 => address)) public mapMap;

    // Struct in array
    TokenHolder[] public holderArray;

    // --- Accessor functions ---

    function getMultiTargetValue() external view returns (uint) {
        return IToken(multiTarget).getValue();
    }

    function getDynamicTokenValue(uint i) external view returns (uint) {
        return IToken(dynamicTokens[i]).getValue();
    }

    function dynamicTokensLength() external view returns (uint) {
        return dynamicTokens.length;
    }

    function getTokenMapValue(uint key) external view returns (uint) {
        return IToken(tokenMap[key]).getValue();
    }

    function getAddrMapValue(address key) external view returns (uint) {
        return IToken(addrMap[key]).getValue();
    }

    function getPrecedenceValue(uint i) external view returns (uint) {
        return IToken(precedenceTokens[i]).getValue();
    }

    function precedenceTokensLength() external view returns (uint) {
        return precedenceTokens.length;
    }

    function getBytes4MapValue(bytes4 key) external view returns (uint) {
        return IToken(bytes4Map[key]).getValue();
    }

    function getMapMapValue(uint i, uint j) external view returns (uint) {
        return IToken(mapMap[i][j]).getValue();
    }

    function getHolderArrayValue(uint i) external view returns (uint) {
        return IToken(holderArray[i].token).getValue();
    }

    function holderArrayLength() external view returns (uint) {
        return holderArray.length;
    }
}
