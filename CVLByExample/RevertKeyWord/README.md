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
   - Verifying the `lastReverted` flag matches expected behavior.

## Usage

1. **Command**
    ```shell
    certoraRun example.conf --server production --prover_version master
    ```
2. **Expected Output**
    - The output should confirm that the spec passes, with the expected behavior of `lastReverted` in each case.
    - Link: [Example Output](https://prover.certora.com/output/1512/5891181678d0461cb8bcf35122816e8a?anonymousKey=1980299435d6469aa3673d883de13982c204431a)


3. **Examine the Rules**  
   - **`testFooWithRevert`** confirms that calling `foo` with `@withrevert` sets `lastReverted` exactly when the argument is false.
   - **`testCvlFunctionWithRevert`** confirms that a CVL function can revert and sets `lastReverted` accordingly.
   - **`testCanRevert`** uses a wrapper function to capture the return value of the revert signal from `canRevert`.


## Conclusion

With these files (`C.sol`, `example.spec`, and this `README.md`), you can see how the new CVL revert feature works in practice. By enabling `-cvlFunctionRevert`, you can write more expressive and accurate specs that treat reverts in CVL and Solidity calls consistently, capturing those reverts in **`lastReverted`** for precise modeling in your verification.
