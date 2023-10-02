
# Direct VS Wildcard Summary
This directory demonstrates using the following summary definitions:
- direct summary of base and overloaded functions.
- wildcard summary of all functions.

There are several specs each summarizing different functions.
- `AllDirect.spec` - every function being called (from solidity) is given its own direct summarization.
    Run this version via ```certoraRun.py certora/conf/AllDirect.conf```
    [A report of this run](https://prover.certora.com/output/1902/77851fbff6744e4085427af3893fbe4c/?anonymousKey=33ac02c05c3ebcc27ccca253ea70ec748fd1135d)

- `AllWildcard.spec` - summarizes all functions using a wildcard `_`.
    
    Run this version via ```certoraRun.py certora/conf/AllWildcard.conf```

    [A report of this run](https://prover.certora.com/output/1902/16fce0397cbb45d28be8d7815988188b/?anonymousKey=c3674e16e7c2b2ca601c9387578b9c3ee034d87e)

- `NoOverloadings.spec` - summarizes only TestLibrary functions and does not summarize the overloaded functions.

    Run this version via 
        ```certoraRun.py certora/conf/NoOverloadings.conf```

    [A report of this run](https://prover.certora.com/output/1902/2b1a17c626194f5f8ccc7459fa6688c0/?anonymousKey=074fb4b8573583a049adbb3e79e91c34dc5c502e)

- `OnlyOverloadings.spec` - summarizes only the overloaded functions.
    Run this version via ```certoraRun.py certora/conf/OnlyOverloadings.conf```

    [A report of this run](https://prover.certora.com/output/1902/fc60688d02f1452bbcc33dc460497ba3/?anonymousKey=59c19050da3da666894ec1586b4f560e30b9c974)

