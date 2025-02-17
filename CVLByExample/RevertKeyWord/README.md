# CVL Revert Feature Example

This folder demonstrates the newly introduced **CVL revert functionality** and the **`@withrevert`** annotation. These features allow you to:

1. **Explicitly revert** inside CVL functions (e.g. `revert("some reason")`).
2. **Capture revert signals** when calling any function—Solidity or CVL—using the `@withrevert` annotation, which sets the built-in CVL variable `lastReverted` to `true` if a revert occurs.

## Files

1. **`C.sol`**  
   A simple Solidity contract with functions that may revert. The contract contains:
   - `foo(bool b)`: sets a flag and reverts if `b` is false.  
   - `canRevert(bool b)`: returns `b` or reverts if `b` is false.  
   - Additional helper functions: `callFooFromContract`, `summarizeMe`, `callSummarizeMe`.

2. **`example.spec`**  
   A CVL spec demonstrating:
   - Calling a Solidity function with `@withrevert`, e.g. `foo@withrevert(b)`.
   - Writing a CVL function (`cvlFunctionThatMayRevert`) that explicitly reverts when a condition fails.
   - Two different ways to handle potential reverts from `canRevert(bool)`, illustrating how revert can either be captured inline or bubble up through a CVL wrapper.

## Usage

1. **Command**
    ```shell
    certoraRun example.conf --server production --prover_version master
    ```
2. **Expected Output**
    - The output should confirm that the spec passes, with the expected behavior of `lastReverted` in each case.
    - Link: [Example Output](https://prover.certora.com/output/1512/5891181678d0461cb8bcf35122816e8a?anonymousKey=1980299435d6469aa3673d883de13982c204431a)

3. **Examine the Rules**  
   - **`testFooWithRevert`**: Confirms that calling `foo` with `@withrevert` sets `lastReverted` exactly when the argument is false.  
   - **`testCvlFunctionWithRevert`**: Demonstrates how a CVL function (`cvlFunctionThatMayRevert`) can explicitly revert, and how `@withrevert` captures that.  
   - **`testCanRevertInline`**: Uses `wrapperForCanRevertInline(bool)` which internally calls `canRevert@withrevert(condition)`, returning `lastReverted`.  
   - **`testCanRevertBubbleUp`**: Illustrates revert **bubbling up**. In `wrapperForCanRevertBubble(bool)`, we call `canRevert(condition)` *without* `@withrevert`, but then call the wrapper itself with `@withrevert` from the rule. The internal revert propagates, setting `lastReverted`.

## Conclusion

With these files (`C.sol`, `example.spec`, `Example.conf`, and this `README.md`), you can see how the new CVL revert feature works in practice. By enabling the `-cvlFunctionRevert` flag, you can write more expressive and accurate specs that treat reverts in CVL and Solidity calls consistently, capturing those reverts in **`lastReverted`** for precise modeling in your verification. The **bubble-up** behavior especially highlights how deeper CVL calls can now propagate reverts just like Solidity calls.
