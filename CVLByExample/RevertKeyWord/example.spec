// We declare the external methods (functions) that we want to call or reference:
methods {
    function foo(bool) external envfree;
    function canRevert(bool) external returns bool envfree;
}

// --------------------
// Example CVL function that can revert:
// --------------------
function cvlFunctionThatMayRevert(bool input) {
    // The new 'revert' keyword in CVL
    if (!input) {
        revert("Input was false in CVL function");
    }
}

// --------------------
// Example rule: calling 'foo' with @withrevert
// --------------------
rule testFooWithRevert {
    bool condition;
    // Using @withrevert to capture whether 'foo' reverts
    foo@withrevert(condition);

    // 'lastReverted' is true if and only if 'foo' reverts
    // 'foo' reverts when 'condition' is false
    assert lastReverted <=> !condition;
}

// --------------------
// Example rule: calling a CVL function with @withrevert
// --------------------
rule testCvlFunctionWithRevert {
    bool condition;
    // If 'cvlFunctionThatMayRevert' reverts, 'lastReverted' is set to true
    cvlFunctionThatMayRevert@withrevert(condition);

    // This rule checks that 'lastReverted' is exactly when 'condition' is false
    assert lastReverted <=> !condition;
}

// --------------------
// Example rule: calling 'canRevert' within a CVL wrapper and using @withrevert
// --------------------
function wrapperForCanRevert(bool condition) returns bool {
    // If 'canRevert(condition)' reverts, 'lastReverted' is set to true here
    canRevert@withrevert(condition);
    return lastReverted;
}

rule testCanRevert {
    bool condition;
    bool outcome = wrapperForCanRevert(condition);

    // This rule checks that 'lastReverted' is exactly when 'condition' is false
    assert outcome <=> !condition;
}
