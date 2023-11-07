
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
    is false. Consequantly the rule `callOverloadedInInterfaceExternal` fails.
    The function `unresolved.calleeOverloadedInInterfaceExternal()` which is unresolved is summarized to true and the rule `callIOverloadedInInterfaceExternal` passes.
    The rule `callSummarizedFromCVL` fails because a function called from CVL is not summarized.

- `AllWildcard.spec` - summarizes all functions using a wildcard `_`.
    
    Run this version via ```certoraRun certora/conf/AllWildcard.conf```

    [A report of this run](https://prover.certora.com/output/1902/569d5c5865fa4f0b8c84dac3443bef27?anonymousKey=f447885e97470795e3c7adb2554be09ff2bc95e6)

    The same rules fail as in `AllDirect.spec` for the same reasons.

