// --------------------------------------------------------
// 1. Declare the methods we want to call or inspect
// --------------------------------------------------------
methods {
    function breakInvariant(address, int256) external returns bool envfree;
    function accessInvariant(address) external returns bool envfree;
}

// --------------------------------------------------------
// 2. Define the invariant: alwaysPositive **should be violated** with the new semantics but should be verified with the old semantics
// --------------------------------------------------------
invariant alwaysPositive(address a)
    currentContract.balance[a] >= 0;

// --------------------------------------------------------
// 3. A helper function that enforces the invariant
// --------------------------------------------------------
function safeAssumptions(address user) {
    requireInvariant alwaysPositive(user);
}

// --------------------------------------------------------
// 4. Hook: whenever we read `accessInvariant[user]`, call `safeAssumptions(user)`
// --------------------------------------------------------
hook Sload bool b currentContract.accessInvariant[KEY address user] {
    safeAssumptions(user);
}
