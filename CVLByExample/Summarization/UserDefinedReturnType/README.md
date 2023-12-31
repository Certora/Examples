# Library Function Summarization
This directory demonstrates summarization of library functions vs. summarization of contract functions and when is each applied.

## LibraryVSContractSummary.spec

Run this spec via
```certoraRun runLibraryVSContractSummary.conf```

[A report of this run](https://prover.certora.com/output/15800/e6d908d2545d4b58ac21aa775da729ac?anonymousKey=be788458e07d22409288376b7ebcab2d2c523edd)

## UserDefinedTypeSummarization.spec

Functions returning struct or array are not summarized (the summary is not applied).
Functions returning enum can be summarized.

Run this spec via 
```certoraRun runUserDefinedTypeSummary.conf```

[A report of this run](https://prover.certora.com/output/15800/c08331acc235459db96264cb15fada59?anonymousKey=3169dabf1c16106c53e3727136207e35d32b9174)
