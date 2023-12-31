
# Direct VS Wildcard Summary

This directory demonstrates using the following summary definitions:
- direct (contract level) summary of base and overloaded functions.
- wildcard summary of all library functions.

## AllDirect.spec 
    Every function being called (from solidity) is given its own direct summarization.
   
    Run this spec via ```certoraRun AllDirect.conf```

    [A report of this run](https://prover.certora.com/output/15800/9688edc297024247a0aef14c5f5bcbe9?anonymousKey=7410e26bdb1d90c4f56d783c7c6f34fd4106e0b1)

    The summarization ```function _.calleeOverloadedInInterfaceExternal()  external => ALWAYS(true) UNRESOLVED;```
    summarizes only unresolved functions. Therefore, `TestLibrary.calleeOverloadedInInterfaceExternal()` is not summarized and is false. Consequently, the rule `callOverloadedInInterfaceExternal` fails.

    The function `unresolved.calleeOverloadedInInterfaceExternal()` which is unresolved is summarized to true and the rule `callIOverloadedInInterfaceExternal` passes.

    The rule `callSummarizedFromCVL` fails because functions called from CVL are not summarized. Summarization are only from within Solidity code

