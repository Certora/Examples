# Library Function Summarization
This directory demonstrates summarization of library functions vs. summarization of contract functions and when is each applied.

## LibraryVSContractSummary.spec

Run this spec via
```certoraRun runLibraryVSContractSummary.conf```

[A report of this run](https://prover.certora.com/output/1902/cb0d51bc02f54551a0967b8586d1c9a6?anonymousKey=e8f3e3676fa7b811c2de466fe2b68104cd6e16d1)

## UserDefinedTypeSummarization.spec

Functions returning struct or array are not summarized (the summary is not applied).
Functions returning enum can be summarized.

Run this spec via 
```certoraRun runUserDefinedTypeSummary.conf```

[A report of this run](https://prover.certora.com/output/1902/605ad25bf03b4a809a10db61f0a4b7a4?anonymousKey=2009f88b25a771c1b5eb19a1d03ee2582221a3a6)
