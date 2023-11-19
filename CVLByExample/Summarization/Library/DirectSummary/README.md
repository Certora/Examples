
# Direct VS Wildcard Summary
This directory demonstrates using the following summary definitions:
- direct (contract level) summary of base and overloaded functions.
- wildcard summary of all library functions.

There are several specs each summarizing different functions.
- `AllDirect.spec` - every function being called (from solidity) is given its own direct summarization.
   
    Run this version via ```certoraRun certora/conf/AllDirect.conf```

    [A report of this run](https://prover.certora.com/output/1902/1c2659cb4fd44abd82992d6585e0e345?anonymousKey=eab39d9370595a2b31c450c14d3b6ddff047c01e)

    The summarization ```function _.calleeOverloadedInInterfaceExternal()  external => ALWAYS(true) UNRESOLVED;```
    summarizes only unresolved functions.
    Therefore, `TestLibrary.calleeOverloadedInInterfaceExternal()` is not summarized and
    is false. Consequently, the rule `callOverloadedInInterfaceExternal` fails.
    The function `unresolved.calleeOverloadedInInterfaceExternal()` which is unresolved is summarized to true and the rule `callIOverloadedInInterfaceExternal` passes.
    The rule `callSummarizedFromCVL` fails because functions called from CVL are not summarized. Summarization are only from within Solidity code

