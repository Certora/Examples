// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity ^0.8.0;

/// @title Double Linked List.
/// @author Morpho Labs.
/// @custom:contact security@morpho.xyz
/// @notice Modified double linked list with capped sorting insertion.
library DoubleLinkedList {
    /* STRUCTS */

    struct Account {
        address prev;
        address next;
        uint256 value;
    }

    struct List {
        mapping(address => Account) accounts;
        address head;
        address tail;
    }

    /* ERRORS */

    /// @notice Thrown when the account is already inserted in the double linked list.
    error AccountAlreadyInserted();

    /// @notice Thrown when the account to remove does not exist.
    error AccountDoesNotExist();

    /// @notice Thrown when the address is zero at insertion.
    error AddressIsZero();

    /// @notice Thrown when the value is zero at insertion.
    error ValueIsZero();

    /* INTERNAL */

    /// @notice Returns the `account` linked to `id`.
    /// @param list The list to search in.
    /// @param id The address of the account.
    /// @return The value of the account.
    function getValueOf(List storage list, address id) internal view returns (uint256) {
        return list.accounts[id].value;
    }

    /// @notice Returns the address at the head of the `list`.
    /// @param list The list to get the head.
    /// @return The address of the head.
    function getHead(List storage list) internal view returns (address) {
        return list.head;
    }

    /// @notice Returns the address at the tail of the `list`.
    /// @param list The list to get the tail.
    /// @return The address of the tail.
    function getTail(List storage list) internal view returns (address) {
        return list.tail;
    }

    /// @notice Returns the next id address from the current `id`.
    /// @param list The list to search in.
    /// @param id The address of the account.
    /// @return The address of the next account.
    function getNext(List storage list, address id) internal view returns (address) {
        return list.accounts[id].next;
    }

    /// @notice Returns the previous id address from the current `id`.
    /// @param list The list to search in.
    /// @param id The address of the account.
    /// @return The address of the previous account.
    function getPrev(List storage list, address id) internal view returns (address) {
        return list.accounts[id].prev;
    }

    /// @notice Removes an account of the `list`.
    /// @param list The list to search in.
    /// @param id The address of the account.
    function remove(List storage list, address id) internal {
        Account memory account = list.accounts[id];
        if (account.value == 0) revert AccountDoesNotExist();

        if (account.prev != address(0)) list.accounts[account.prev].next = account.next;
        else list.head = account.next;
        if (account.next != address(0)) list.accounts[account.next].prev = account.prev;
        else list.tail = account.prev;

        delete list.accounts[id];
    }

    /// @notice Inserts an account in the `list` at the right slot based on its `value`.
    /// @param list The list to search in.
    /// @param id The address of the account.
    /// @param value The value of the account.
    /// @param maxIterations The max number of iterations.
    function insertSorted(List storage list, address id, uint256 value, uint256 maxIterations) internal {
        if (value == 0) revert ValueIsZero();
        if (id == address(0)) revert AddressIsZero();
        if (list.accounts[id].value != 0) revert AccountAlreadyInserted();

        uint256 numberOfIterations;
        address next = list.head; // If not added at the end of the list `id` will be inserted before `next`.

        while (numberOfIterations < maxIterations && next != address(0) && list.accounts[next].value >= value) {
            next = list.accounts[next].next;
            unchecked {
                ++numberOfIterations;
            }
        }

        // Account is not the new tail.
        if (numberOfIterations < maxIterations && next != address(0)) {
            // Account is the new head.
            if (next == list.head) {
                list.accounts[id] = Account({prev: address(0), next: next, value: value});
                list.head = id;
                list.accounts[next].prev = id;
            }
            // Account is not the new head.
            else {
                address prev = list.accounts[next].prev;
                list.accounts[id] = Account({prev: prev, next: next, value: value});
                list.accounts[prev].next = id;
                list.accounts[next].prev = id;
            }
        }
        // Account is the new tail.
        else {
            // Account is the new head.
            if (list.head == address(0)) {
                list.accounts[id] = Account({prev: address(0), next: address(0), value: value});
                list.head = id;
                list.tail = id;
            }
            // Account is not the new head.
            else {
                address tail = list.tail;
                list.accounts[id] = Account({prev: tail, next: address(0), value: value});
                list.accounts[tail].next = id;
                list.tail = id;
            }
        }
    }
}
