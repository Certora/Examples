// ---------------------------------------------------------
// 1. Declare the contract methods we want to verify/inspect
// ---------------------------------------------------------
methods {
    // Contract functions that may revert
    function foo(bool) external envfree;
    function canRevert(bool) external returns bool envfree;
}

// ---------------------------------------------------------
// 2. CVL function that explicitly uses the 'revert' keyword
// ---------------------------------------------------------
function cvlFunctionThatMayRevert(bool input) {
    // If input is false, we revert with a message
    if (!input) {
        revert("Input was false in CVL function");
    }
}

// ---------------------------------------------------------
// 3. Demonstration #1: Calling 'foo' with @withrevert directly
// ---------------------------------------------------------
rule testFooWithRevert {
    bool condition;
    // Using @withrevert to see if 'foo' reverts
    foo@withrevert(condition);

    // 'foo' reverts exactly when 'condition' is false
    // => 'lastReverted' == !condition
    assert lastReverted <=> !condition;
}

// ---------------------------------------------------------
// 4. Demonstration #2: Calling a CVL function with @withrevert
// ---------------------------------------------------------
rule testCvlFunctionWithRevert {
    bool condition;
    // If 'cvlFunctionThatMayRevert' reverts, 'lastReverted' becomes true
    cvlFunctionThatMayRevert@withrevert(condition);

    // Check that 'lastReverted' matches whether 'condition' was false
    assert lastReverted <=> !condition;
}

// ---------------------------------------------------------
// 5. Demonstration #3 (Old Approach): 'canRevert' using @withrevert INSIDE the wrapper
// ---------------------------------------------------------
function wrapperForCanRevertInline(bool condition) returns bool {
    // Here we call canRevert WITH @withrevert internally
    canRevert@withrevert(condition);
    return lastReverted; // We return the revert status
}

rule testCanRevertInline {
    bool condition;
    bool outcome = wrapperForCanRevertInline(condition);

    // 'outcome' is true iff 'canRevert' reverted, which happens if condition == false
    assert outcome <=> !condition;
}

// ---------------------------------------------------------
// 6. Demonstration #4 (New Approach): Revert "bubbling up" through a CVL function
// ---------------------------------------------------------
// In this approach, 'canRevert' is called WITHOUT @withrevert inside the function.
// Then, from the rule, we call the wrapper itself with @withrevert, allowing the
// revert to "bubble up" and set 'lastReverted' if an internal revert occurs.
function wrapperForCanRevertBubble(bool condition) {
    // Notice: no @withrevert here
    canRevert(condition); 
}

rule testCanRevertBubbleUp {
    bool condition;
    // We call the wrapper with @withrevert from the rule
    wrapperForCanRevertBubble@withrevert(condition);

    // If 'canRevert(condition)' reverts internally when condition == false,
    // that revert will bubble up and set 'lastReverted' to true.
    assert lastReverted <=> !condition;
}
