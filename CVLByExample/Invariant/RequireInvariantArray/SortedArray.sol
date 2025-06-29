// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SortedArray
 * @notice A simple contract maintaining a sorted array of uint256
 */
contract SortedArray {
    uint256[] public arr;

    /**
     * @notice Inserts a new value into the array, keeping it sorted in ascending order.
     * @param val The value to insert
     */
    function insert(uint256 val) external {
        // Simple linear approach:
        // 1. Find the position where 'val' should go.
        // 2. Insert it there, shifting subsequent elements.
        uint256 pos = 0;
        while (pos < arr.length && arr[pos] <= val) {
            pos++;
        }

        // Insert by pushing a dummy at the end, then shifting
        arr.push(val); // extends array by 1
        for (uint256 i = arr.length - 1; i > pos; i--) {
            arr[i] = arr[i - 1];
        }
        arr[pos] = val;
    }

    /**
     * @notice Removes the element at index `index`. 
     * @dev For simplicity, just shift down from 'index' onward; last element is pop'd.
     */
    function remove(uint256 index) external {
        require(index < arr.length, "Index out of range");
        for (uint256 i = index; i < arr.length - 1; i++) {
            arr[i] = arr[i + 1];
        }
        arr.pop(); // remove the last element
    }

    /**
     * @notice Returns the element at index `index`. 
     * @dev Exposes array reads to demonstrate the read hook in CVL.
     */
    function readAt(uint256 index) external view returns (uint256) {
        return arr[index];
    }
}
