
Summarization is a key feature of Certora Prover that enables:
1. Reasoning about external calls
1. [Modular verification](https://docs.certora.com/en/latest/docs/whitepaper/index.html#modularity) by symbolic representation of some part and splitting the verification problem into multiple independent subproblems. 
1. Checking properties in interface points 

See the [docs](https://docs.certora.com/en/latest/docs/cvl/methods.html#summaries) for more information.

This folder contains examples of the many features the Certora Prover allows:

1. Keyword - demonstrates the usage of summary keywords: `always`, `constant`, `nondet` and `HAVOC_ALL`, `Disaptcher` the difference between them, and using linking options.
1. Library - named vs wildcard, and user-defined data types. 
1. GhostSummary -  provides two examples for a  ghost summarization of math functions: interest_computation and sqrt. 
1. WithEnv - referencing env attributes in ghost and CVL function summarization. 
1. MultiContract - summarization of Solidity public functions 

