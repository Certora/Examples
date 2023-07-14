// SPDX-License-Identifier: GNU AGPLv3
pragma solidity ^0.8.0;

import "./DoubleLinkedList.sol";

contract MockDLL {
    using DoubleLinkedList for DoubleLinkedList.List;

    // VERIFICATION INTERFACE

    DoubleLinkedList.List public dll;

    uint256 public maxIterations;

    uint256 internal dummy_state_variable;

    function dummy_state_modifying_function() public {
        // to fix a CVL error when only one function is accessible
        dummy_state_variable = 1;
    }

    function getValueOf(address _id) public view returns (uint256) {
        return dll.getValueOf(_id);
    }

    function getHead() public view returns (address) {
        return dll.getHead();
    }

    function getTail() public view returns (address) {
        return dll.getTail();
    }

    function getNext(address _id) public view returns (address) {
        return dll.getNext(_id);
    }

    function getPrev(address _id) public view returns (address) {
        return dll.getPrev(_id);
    }

    function remove(address _id) public {
        dll.remove(_id);
    }

    function insertSorted(
        address _id,
        uint256 _value,
        uint256 _maxIterations
    ) public {
        dll.insertSorted(_id, _value, _maxIterations);
    }

    function getLength() public view returns (uint256) {
        uint256 len;
        for (address current = getHead(); current != address(0); current = getNext(current)) len++;
        return len;
    }

}
