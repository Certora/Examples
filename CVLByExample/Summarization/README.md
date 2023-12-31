
Summarization is a key feature of Certora Prover that enables:
1. Reasoning about external calls
2. [Modular verification](https://docs.certora.com/en/latest/docs/whitepaper/index.html#modularity) by symbolic representation of some part and splitting the verification problem into multiple independent subproblems. 
3. Checking properties in interface points 

See the [docs](https://docs.certora.com/en/latest/docs/cvl/methods.html#summaries) for more information.

This folder contains examples of the many features the Certora Prover allows:

1. Keywords - demonstrates the usage of summary keywords: `always`, `constant`, `nondet` and `HAVOC_ALL`, `Disaptcher` the difference between them, and using linking options.
2. Library - named vs wildcard, and user-defined data types. 
3. GhostSummary -  provides two examples for a  ghost summarization of math functions: interest_computation and sqrt. 
4. WithEnv - referencing env attributes in ghost and CVL function summarization. 
5. MultiContract - summarization of Solidity public functions 

