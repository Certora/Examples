
# Direct VS Wildcard Summary

This directory demonstrates using the following summary definitions:
- direct (contract level) summary of base and overloaded functions.
- wildcard summary of all library functions.

## AllDirect.spec 
    Every function being called (from solidity) is given its own direct summarization.
   
    Run this spec via ```certoraRun certora/conf/AllDirect.conf```

    [A report of this run](https://prover.certora.com/output/1902/b738721bc99c4540a15f865de4044479?anonymousKey=f15d0e9e5b5cda2df7538efcec3599876079c96c)

    The summarization ```function _.calleeOverloadedInInterfaceExternal()  external => ALWAYS(true) UNRESOLVED;```
    summarizes only unresolved functions. Therefore, `TestLibrary.calleeOverloadedInInterfaceExternal()` is not summarized and is false. Consequently, the rule `callOverloadedInInterfaceExternal` fails.

    The function `unresolved.calleeOverloadedInInterfaceExternal()` which is unresolved is summarized to true and the rule `callIOverloadedInInterfaceExternal` passes.

    The rule `callSummarizedFromCVL` fails because functions called from CVL are not summarized. Summarization are only from within Solidity code

