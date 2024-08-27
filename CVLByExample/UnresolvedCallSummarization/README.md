# Unresolved Call Summarization Example

## Overview
This repository contains a smart contract named `TrusterLenderPool`, featuring a `flashLoan` function. However, there exists a significant vulnerability within this function. The vulnerability allows the pool contract to act as the `msg.sender` for any call, presenting a critical security flaw. This example showcases the utilization of a new feature in CVL called Unresolved Call Summarization. This feature accentuates how the vulnerability can be exploited to grant the attacker an infinite allowance, subsequently leading to the potential draining of all funds within the contract.

**NOTE** based on https://www.damnvulnerabledefi.xyz/

## Usage

```cvl
unresolved external in TrusterLenderPool.flashLoan(uint256,address,address,bytes) => DISPATCH(use_fallback=true) [
    token.approve(address, uint256),
    currentContract._
] default NONDET;
```
In this implementation, we summarize all unresolved calls in the `flashloan` function into one of the following categories:
- If the signature call matches the `approve` function, it is categorized as `token.approve(address, uint256)`.
- If the signature call matches any of the functions within `currentContract`, their implementations are utilized.
- If the callee contract has been resolved to `currentContract` but the signature did not match any of its functions, the fallback implementation will be used.
- Otherwise, it triggers a `NONDET` (nondeterministic) summary.

## Executions

1. **Certora Run Command**
    - Command:
        ```bash
        certoraRun unresolvedCallSummarization.conf
        ```
    - Execution Link: [Certora Run Output](https://prover.certora.com/output/1512/256a1f8bfcdd4136ad86e41ca2bb86b6?anonymousKey=cc61dfa585e9d6535762d8e50e65a7a5041eadc1)

2. **Results Analysis**
The analysis conducted reveals that the `flashLoan` function can be utilized to grant any user any amount of allowance from the contract. This potential exploitation could ultimately lead to the complete drainage of funds within the pool.

For a comprehensive guide on Certora Verification Language, please refer to the [Certora Documentation](https://docs.certora.com).