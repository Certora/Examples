// SPDX-License-Identifier: GNU AGPLv3
pragma solidity ^0.8.0;

import "./EnumerableSet.sol";

contract MockSet {
    using EnumerableSet for EnumerableSet.Bytes32Set;

    // VERIFICATION INTERFACE

    EnumerableSet.Bytes32Set internal set;

    uint256 internal dummy_state_variable;

    function dummy_state_modifying_function() public {
        // to fix a CVL error when only one function is accessible
        dummy_state_variable = 1;
    }

    function add(bytes32 value) public returns (bool) {
        return set.add(value);
    }
    function remove(bytes32 value) public returns (bool) {
        return set.remove(value);
    }

    function contains(bytes32 value) public view returns (bool) {
        return set.contains(value);
    }

    function length() public view returns (uint256) {
        return set.length();
    }

    function elemAt(uint256 index) public view returns (bytes32) {
        return set.at(index);
    }
}
