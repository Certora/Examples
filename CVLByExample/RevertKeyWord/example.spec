// ---------------------------------------------------------
// 1. Declare the contract methods we want to verify/inspect
// ---------------------------------------------------------
methods {
    // Contract functions that may revert
    function foo(bool) external envfree;
    function canRevert(bool) external returns bool envfree;

    // For demonstrating summary usage
    function callSummarizeMe(bool) external envfree;
    function summarizeMe(bool b) external => cvlSummarizeMe(b);
}

// ---------------------------------------------------------
// 2. CVL function that explicitly uses the 'revert' keyword
// ---------------------------------------------------------
function cvlFunctionThatMayRevert(bool input) {
    if (!input) {
        revert("Input was false in CVL function");
    }
}

// ---------------------------------------------------------
// 3. A summary function that can revert.
// ---------------------------------------------------------
// The contract's `summarizeMe(bool b)` is mapped to `cvlSummarizeMe(b)` in CVL.
// If `b` is false, we revert with a message. When called via `callSummarizeMe@withrevert(b)`,
// any revert here bubbles up and sets `lastReverted`.
function cvlSummarizeMe(bool b) {
    if (!b) {
        revert("Summarize revert because b is false");
    }
}

// ---------------------------------------------------------
// 4. Example rule: calling 'foo' with @withrevert
// ---------------------------------------------------------
rule testFooWithRevert {
    bool condition;
    // Using @withrevert to capture whether 'foo' reverts
    foo@withrevert(condition);

    // 'foo' reverts when 'condition' is false
    assert lastReverted <=> !condition;
}

// ---------------------------------------------------------
// 5. Example rule: calling a CVL function with @withrevert
// ---------------------------------------------------------
rule testCvlFunctionWithRevert {
    bool condition;
    // If 'cvlFunctionThatMayRevert' reverts, 'lastReverted' is set to true
    cvlFunctionThatMayRevert@withrevert(condition);

    // Check that 'lastReverted' matches whether 'condition' was false
    assert lastReverted <=> !condition;
}

// ---------------------------------------------------------
// 6. Demonstration #1 for canRevert: inline approach
// ---------------------------------------------------------
function wrapperForCanRevertInline(bool condition) returns bool {
    // Here we call canRevert WITH @withrevert internally
    canRevert@withrevert(condition);
    return lastReverted; // We return the revert status
}

rule testCanRevertInline {
    bool condition;
    bool outcome = wrapperForCanRevertInline(condition);

    // 'outcome' is true exactly when 'condition' is false (i.e., canRevert reverts)
    assert outcome <=> !condition;
}

// ---------------------------------------------------------
// 7. Demonstration #2 for canRevert: revert "bubbling up"
// ---------------------------------------------------------
// We call 'canRevert(condition)' WITHOUT '@withrevert' inside the wrapper,
// letting the revert bubble up to the outer call (the rule).
function wrapperForCanRevertBubble(bool condition) {
    canRevert(condition);
}

rule testCanRevertBubbleUp {
    bool condition;
    // We call the wrapper with @withrevert, so if 'canRevert' reverts, it bubbles up
    wrapperForCanRevertBubble@withrevert(condition);

    // If 'condition' is false => 'canRevert' reverts => bubble up => lastReverted = true
    assert lastReverted <=> !condition;
}

// ---------------------------------------------------------
// 8. Summarize-Me case: the "most interesting" scenario
// ---------------------------------------------------------
// The contract function callSummarizeMe(b) calls summarizeMe(b),
// which is summarized by cvlSummarizeMe(b). That summary reverts
// if b == false. We'll use the 'sanity' tag to see the call trace.
rule testCallSummarizeMe{
    bool condition;
    // Because summarizeMe is mapped to cvlSummarizeMe in CVL (which can revert),
// calling callSummarizeMe with @withrevert will set lastReverted if condition == false.
    callSummarizeMe@withrevert(condition);

    // If condition is false => revert => lastReverted = true
    // If condition is true => no revert => lastReverted = false
    assert lastReverted <=> !condition;
}
