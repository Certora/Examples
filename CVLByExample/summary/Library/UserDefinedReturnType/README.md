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

[A report of this run](https://prover.certora.com/output/1902/117e996e937f445abd6fcfc2e18a83b6?anonymousKey=c2e297677e43fde1e06641868240ec236f8655fc)
