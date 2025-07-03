// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Storage Pointer Rerouting Example
 * @notice This contract demonstrates the use of rerouting summaries for internal functions
 *         that take storage pointers as parameters.
 */

// Library to handle rerouting of internal function calls
library ReroutingLibrary {
    /**
     * @notice Reroutes the internal storage update operation
     * @param data Storage mapping reference
     * @param user Address key for the mapping
     * @param newValues New values to set
     * @return The previous values before update
     */
    function rerouteStorageUpdate(
        mapping(address => uint256[]) storage data,
        address user,
        uint256[] memory newValues
    ) external returns (uint256[] memory) {
        uint256[] memory previousValues = data[user];
        data[user] = newValues;
        return previousValues;
    }
}

contract StoragePointerExample {
    // Main storage mapping
    mapping(address => uint256[]) public userDataArrays;
    
    // Counter for tracking operations
    uint256 public operationCounter;

    /**
     * @notice Internal function that updates storage using storage pointers
     * @param storageRef Reference to the storage mapping
     * @param user Address of the user
     * @param newData New data to store
     * @return Previous data before the update
     */
    function updateStorageInternal(
        mapping(address => uint256[]) storage storageRef,
        address user,
        uint256[] memory newData
    ) internal returns (uint256[] memory) {
        uint256[] memory oldData = storageRef[user];
        storageRef[user] = newData;
        operationCounter++;
        return oldData;
    }

    /**
     * @notice External function that calls the internal storage update
     * @param user Address of the user
     * @param newData New data to store
     * @return Previous data before the update
     */
    function updateUserData(
        address user,
        uint256[] memory newData
    ) external returns (uint256[] memory) {
        return updateStorageInternal(userDataArrays, user, newData);
    }

    /**
     * @notice Get user data array
     * @param user Address of the user
     * @return User's data array
     */
    function getUserData(address user) external view returns (uint256[] memory) {
        return userDataArrays[user];
    }

    /**
     * @notice Get the length of user's data array
     * @param user Address of the user
     * @return Length of the array
     */
    function getUserDataLength(address user) external view returns (uint256) {
        return userDataArrays[user].length;
    }
}
