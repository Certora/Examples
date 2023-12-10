# Reentrancy
This directory contains 
  - A "bank" with reentrancy vulnerabilities. 
  - Different fixes to the contract to avoid the vulnerabilities.
  - CVL rules to verify reentrancy safety properties.

## Contracts
The contract `VulnerableBank.sol`, based on [Ethernaut course](https://dev.to/nvn/ethernaut-hacks-level-10-re-entrancy-42o9) ,  includes reentrancy vulnerabilities.
A malicious user can re-enter the contract in both `withdraw` and `withdrawAll` using the external callbacks in the functions. As the `userBalances` data structure is updated only after calling the callback, a malicious user can drain all the bank's funds using this reentrancy vulnerability. 

In contract `BankGuardFix.sol` the standard reentrancy guard is used to protect from reentrancy. This ensures that if the contract is reentered, the whole transaction reverts. 

In `BankPartialFix.sol`, we show an incomplete way to fix the `VulnerableBank.sol` code, and it is conceptually similar to the Curve hack due to the [Vyper implementation bug in the reentrancy guards](https://osec.io/blog/2023-08-01-vyper-timeline). This is because two different guards are used for the `withdraw` and `withdrawAll` functions. This protects the contract from reentrancy from one function to itself, but does not protect from cross-function reentrancy. 

The contract in `BankNoGuardFix.sol` contains another common approach to reentrancy safety that allows reentrancy calls though all the external calls are either at the beginning or at the end of the transaction.

## Spec
The `certora\spec` folder contains three different reentrancy checks.

### Read Only Reentrancy 
File `ReadOnlyReentrancy.spec` uses the `viewReentrancy` builtin rule.
see [docs](https://docs.certora.com/en/latest/docs/cvl/builtin.html#read-only-reentrancy-detection-viewreentrancy) for more information on how the Certora Prover checks for view reentrancy. 
The rule is violated for the `BankGuardFix.sol` because the guard does not protect third parties that use a view function.

### No Reentrancy 
File `Reentrancy.spec` contains the rule `no_reentrancy`, a double-parametric rule that is instantiated for every pair `(f,g)` where `f` and `g` are non-view external methods of the contract. In the rule, we call `f` and save the sighash of `g` into `g_sighhash` for future usage. We then hook on any call which is done directly and indirectly from `f` and we simulate a call to `g` using `g_sighhash`. We then save its reverted status in `g_reverted`. At the end of the rule, we have an assert that checks that if we called `g` during the callback, then `g` reverted. 

### Reentrancy Safety 
File `NoGuardSafety.spec` contains a rule `reentrancySafety` that verifies that all storage accesses are either before  or after external calls. This is an approach that allows reentrancy but keeps all storage updates safe.  The property checks that a reentrancy vulnerability cannot occur. It does not check the existence of this vulnerability. 



## Running the specs on the contracts

This folder includes a configuration file for each rule on each contract to be run using `certoraRun <contract>_<rule>.conf`. Alternatively the script.sh can be used to run all specs on all contracts.
The results of the rules on the different contracts are: 

| Rule | VulnerableBank |  BankPartialFix | BankGuardFix | BankNoGuardFix |
| ---| ------------------ | ------- | ---------| --- |
|viewReentrancy| [violated](https://vaas-stg.certora.com/output/99814/a53c86a31be34833a6c3540db3b28cd5?anonymousKey=27248c3660d699ed0492d64e4ac321cfcc6aee81) |  [violated](https://vaas-stg.certora.com/output/99814/ae3c14eb115444f3a154f75894c6cad1?anonymousKey=80c30ca0a10e864bcbe99c9f507a62c814acd638) | [violated](https://vaas-stg.certora.com/output/99814/ffc6df5b2e544ee28c88acd4080ef621?anonymousKey=69adbd3dcfb4139114c69bf5e0a2c91a94c03d27) | [verified](https://vaas-stg.certora.com/output/99814/8f21165e5bd3454a8f15ed9a2eabbb67?anonymousKey=980c51c8ecfead1c1d13c43a0db8b1b8b34ef9de)  |
| no_reentrancy | [violated](https://vaas-stg.certora.com/output/99814/08d61d0ce38b4149b6f136d7cd04247f?anonymousKey=765ec2a97968d73911cbf04b2fc2ba886ca4e202)  | [violated](https://vaas-stg.certora.com/output/99814/30dc52655d8c4ebbb539bdb4ecfd4d19?anonymousKey=f56c0a2b99e3769d631b91550e2c9b620d978ed4) | [verified](https://vaas-stg.certora.com/output/99814/e5de5eaf995d4a6b95be435d8f9e9d35?anonymousKey=25e238487eb966e2220283688b4b7a8b0679e80d) | [violated](https://vaas-stg.certora.com/output/99814/8740e5e6ea3748fab2fca5a232c123a4?anonymousKey=55f92150d2236baf47a23c2b0afac4e742cca86f) | 
| reentrancySafety | [violated](https://vaas-stg.certora.com/output/99814/b4f39835031a41baa482e93fedebcbe2?anonymousKey=93f2082c7a341df047766c9f1f1c89f7cd982936) | [violated](https://vaas-stg.certora.com/output/99814/f38cb1b11e0c4692902e3ba7c798fc49?anonymousKey=0b743cc0e47577ecfa3e46c2a313a880d570897b) | [violated](https://vaas-stg.certora.com/output/99814/2e4f3cdaae38433781c382a80b04e0a4?anonymousKey=8c859aa6a3e7f6b351e48a807087f9ddc4b06ae0) | [violated](https://vaas-stg.certora.com/output/99814/319f974723a34152989eb6bd3fcb92dd?anonymousKey=597e208730e4da85e1e5fed86a1c931d5f34cbf0) |  
---


The reentrancySafety is violated on VulnerableBank for `withdraw` and `withdrawAll`. The violated case is when:
1. The access to storage in `getUserBalance` sets `storage_access_before_call` to true.
2. The call `msg.sender.call` sets `called_extcall` to true.
3. The storage access to `userBalances[msg.sender]` sets `storage_access_after_call` to true.

Note:
It also shows a violation for `BankGuardFix` as the property checked for does not hold, regardless of the code being a valid solution.


The `no_reentrancy` rule from `Reentrancy.spec` shows that BankPartialFix only has cross-function vulnerability issues. That is, a call to `withdraw` within a call to `withdraw` is not possible. But a call to `withdraw` is possible from within `withdrawAll.`
