# Unresolved Call Summarization Example

## Overview
This repository contains a smart contract named `TrusterLenderPool`, featuring a `flashLoan` function. However, there exists a significant vulnerability within this function. The vulnerability allows the pool contract to act as the `msg.sender` for any call, presenting a critical security flaw. This example showcases the utilization of a new feature in CVL called Unresolved Call Summarization. This feature accentuates how the vulnerability can be exploited to grant the attacker an infinite allowance, subsequently leading to the potential draining of all funds within the contract.

## Usage

```cvl
function _._ external => DISPATCH [
    token.approve(address, uint256), 
    currentContract._
] default NONDET;
```
In this implementation, we summarize all unresolved calls into one of the following categories:
- If the signature call matches the `approve` function, it is categorized as `token.approve(address, uint256)`.
- If the signature call matches any of the functions within `currentContract`, their implementations are utilized.
- Otherwise, it triggers a `NONDET` (nondeterministic) summary.

## Executions

1. **Certora Run Command**
    - Command:
        ```bash
        certoraRun truster.conf --server production --prover_version master
        ```
    - Execution Link: [Certora Run Output](https://prover.certora.com/output/1512/06475b1b09f54738878f41df691da63d?anonymousKey=0d071bf246bc1285e041a0555c2aa295aaee865)

2. **Results Analysis**
The analysis conducted reveals that the `flashLoan` function can be utilized to grant any user any amount of allowance from the contract. This potential exploitation could ultimately lead to the complete drainage of funds within the pool.

For a comprehensive guide on Certora Verification Language, please refer to the [Certora Documentation](https://docs.certora.com).