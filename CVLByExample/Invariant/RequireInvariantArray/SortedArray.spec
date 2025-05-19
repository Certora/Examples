// ---------------------------------------------------------
// 1. Declare the contract methods we want to call or inspect
// ---------------------------------------------------------
methods {
    function insert(uint256) external envfree;
    function remove(uint256) external envfree;
    function readAt(uint256) external returns (uint256) envfree;
}

// ---------------------------------------------------------
// 2. Define the sorted invariant: arr[i] <= arr[i+1] for all valid i, **Violated** under the new semantics and **Verified** under the old semantics.
// ---------------------------------------------------------
// Check array bounds carefully to avoid out-of-range checks
// We only enforce i < arr.length - 1 => arr[i] <= arr[i+1]
invariant isSorted(uint256 i) 
    i < currentContract.arr.length - 1 => currentContract.arr[i] <= currentContract.arr[require_uint256(i + 1)];


// ---------------------------------------------------------
// 3. A function that calls 'requireInvariant' with the isSorted(i) invariant
// ---------------------------------------------------------
function safeSortedAssumption(uint256 i) {
    requireInvariant isSorted(i);
}

// ---------------------------------------------------------
// 4. Read Hook: whenever 'arr[i]' is accessed via 'readAt(i)', call 'safeSortedAssumption(i)'
// ---------------------------------------------------------
hook Sload uint256 ret currentContract.arr[INDEX uint256 index] {
    safeSortedAssumption(index);
}
