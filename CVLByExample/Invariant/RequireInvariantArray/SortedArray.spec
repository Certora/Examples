

// ---------------------------------------------------------------
// Define the sorted invariant: arr[i] <= arr[i+1] for all valid i
// ---------------------------------------------------------------
// Check array bounds carefully to avoid out-of-range checks
invariant isSorted(uint256 i) 
    i < currentContract.arr.length - 1 => currentContract.arr[i] <= currentContract.arr[require_uint256(i + 1)] ;


// ----------------------------------------------------------------
// An incorrect invariant that is not violated in the old semantics 
// ----------------------------------------------------------------
invariant incorrect(uint256 i) 
    i < currentContract.arr.length => currentContract.arr[i] == 71;


// ----------------------------------------------------------------------------
// Load and Store Hooks: whenever 'arr[i]' is accessed assume the invariants 
// ----------------------------------------------------------------------------
hook Sload uint256 ret currentContract.arr[INDEX uint256 index] {
        requireInvariant isSorted(index);
        requireInvariant incorrect(index);
}

hook Sstore currentContract.arr[INDEX uint256 index]  uint256 val {
        requireInvariant isSorted(index);
        requireInvariant incorrect(index);
}
