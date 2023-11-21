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

This folder includes a configuration file to be run using `certoraRun Reentrancy.conf` which can be adopted to check the reentrancy specs on each of the different contracts. Alternatively the script.sh can be used to run all specs on all contracts.
The results of the rules on the different contracts are: 

| Rule | VulnerableBank |  BankPartialFix | BankGuardFix | BankNoGuardFix |
| ---| ------------------ | ------- | ---------| --- |
|viewReentrancy| [violated](https://prover.certora.com/output/40726/fcf0a1dcbd184eac9aaf1e19fa7cc7ca/?anonymousKey=cb6a74f8400a1d701364f80ee8b043aec6d3fa5e) |  [violated](https://prover.certora.com/output/40726/2d7af3d99ef34315a83d1aee70cf341d/?anonymousKey=d06ad0c34b5e1aa20114a630a869fb60a98e494e) | [violated](https://prover.certora.com/output/40726/e9613f2f235d4ad8a0890086948abdce/?anonymousKey=3d145bf95ccb691856057ea34dc4e557742959bd) | [verified](https://prover.certora.com/output/40726/a46a13552cf642a6a81fdc10c9162048/?anonymousKey=fde611f643b0707f0f00759dd0dacdf0ab863313)  |
| no_reentrancy | [violated](https://prover.certora.com/output/40726/862a961b0a074d3fb74118f6100169b8/?anonymousKey=b3e832314b390e81537d6b326be7b90176955ad6)  | [violated](https://prover.certora.com/output/40726/251dd2aaad664dc2a4374919b0cc83fd/?anonymousKey=5fe9a9c43124a7be4ab103d40ea2cfa6b32a70c9) | [verified](https://prover.certora.com/output/40726/41cc34259f4e4d1f8e648a31e1ec0a1b/?anonymousKey=7e924f5d443ca0e800f08064e1b439b117d3848c) | [violated](https://prover.certora.com/output/40726/b89c7e2afc4740c891e96ad4c70e2e8e/?anonymousKey=eda258e003d4462743c72710c4690559c1862da4) | 
| reentrancySafety | [violated](https://prover.certora.com/output/40726/2badf195c7684ca1a4ee5c42c3db3393/?anonymousKey=d00dd0ba0d1c49719781edfa6f2763c676f20505) | [violated](https://prover.certora.com/output/40726/5fd3187562b34dd483ada1112ff6136c/?anonymousKey=de48a3eb6871883a30f27043bb1393eb4c94c458) | [violated](https://prover.certora.com/output/40726/b62e2d9e904544ac9593460d69e338d7/?anonymousKey=bfd6700d53766f021225452a499a9b937681865d) | [verified](https://prover.certora.com/output/40726/983c9e07e81f44e18a08d898465ae30b/?anonymousKey=fc8047593fc9bf9e96a3e1a948f1cc3736df964f) |  
---


The reentrancySafety is violated on VulnerableBank for `withdraw` and `withdrawAll`. The violated case is when:
1. The access to storage in `getUserBalance` sets `storage_access_before_call` to true.
2. The call `msg.sender.call` sets `called_extcall` to true.
3. The storage access to `userBalances[msg.sender]` sets `storage_access_after_call` to true.

Note:
It also shows a violation for `BankGuardFix` as the property checked for does not hold, regardless of the code being a valid solution.


The `no_reentrancy` rule from `Reentrancy.spec` shows that BankPartialFix only has cross-function vulnerability issues. That is, a call to `withdraw` within a call to `withdraw` is not possible. But a call to `withdraw` is possible from within `withdrawAll.`
