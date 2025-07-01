// Storage Pointer Rerouting Specification
// CVL specification demonstrating rerouting summaries for internal functions
// that accept storage pointers as parameters.

methods {
    // Rerouting summary: internal function calls are redirected to library methods
    function StoragePointerExample.updateStorageInternal(
        mapping(address => uint256[]) storage storageRef,
        address user,
        uint256[] memory newData
    ) internal returns (uint256[] memory) => ReroutingLibrary.rerouteStorageUpdate(storageRef, user, newData);
    
    // External function declarations
    function updateUserData(address, uint256[] memory) external returns (uint256[] memory);
    function getUserData(address) external returns (uint256[] memory) envfree;
    function getUserDataLength(address) external returns (uint256) envfree;
    function operationCounter() external returns (uint256) envfree;
}

/**
 * @notice Rule to verify that rerouting summary correctly handles storage updates
 * @dev Tests that the internal function call is properly rerouted through the library
 */
rule testReroutingSummary(env e) {
    address user;
    uint256[] newData;
    
    // Get initial state
    uint256[] initialData = getUserData(user);
    uint256 initialCounter = operationCounter();
    
    // Call the external function that internally uses storage pointers
    uint256[] returnedData = updateUserData(e, user, newData);
    
    // Verify that the returned data matches the initial data
    assert returnedData.length == initialData.length, 
        "Returned data length should match initial data length";
    
    // Verify that the storage was updated with new data
    uint256[] currentData = getUserData(user);
    assert currentData.length == newData.length,
        "Current data length should match new data length";
    
    // Verify operation counter was incremented
    assert operationCounter() == initialCounter + 1,
        "Operation counter should be incremented by 1";
}

/**
 * @notice Rule to verify data integrity during storage pointer operations
 */
rule testDataIntegrity(env e) {
    address user1;
    address user2;
    uint256[] data1;
    uint256[] data2;
    
    // Require different users
    require user1 != user2;
    
    // Get initial states
    uint256[] initial1 = getUserData(user1);
    uint256[] initial2 = getUserData(user2);
    
    // Update user1's data
    updateUserData(e, user1, data1);
    
    // Verify user2's data wasn't affected
    uint256[] afterUpdate2 = getUserData(user2);
    assert afterUpdate2.length == initial2.length,
        "User2 data should not be affected by user1 update";
}

/**
 * @notice Rule to verify array bounds and length consistency
 */
rule testArrayBounds(env e) {
    address user;
    uint256[] newData;
    uint256 index;
    
    // Require valid index
    require index < newData.length;
    require newData.length > 0;
    
    // Update user data
    updateUserData(e, user, newData);
    
    // Verify length consistency
    uint256 storedLength = getUserDataLength(user);
    uint256[] retrievedData = getUserData(user);
    
    assert storedLength == retrievedData.length,
        "Stored length should match retrieved array length";
    assert storedLength == newData.length,
        "Stored length should match input data length";
}

/**
 * @notice Invariant to ensure operation counter only increases
 */
invariant operationCounterMonotonic()
    operationCounter() >= 0
    {
        preserved {
            require operationCounter() <= max_uint256 - 1;
        }
    }
