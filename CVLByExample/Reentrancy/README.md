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
File `ViewReentrancy.spec` uses the `viewReentrancy` builtin rule.
see [docs](https://docs.certora.com/en/latest/docs/cvl/builtin.html#read-only-reentrancy-detection-viewreentrancy) for more information on how the Certora Prover checks for view reentrancy. 
The rule is violated for the `BankGuardFix.sol` because the guard does not protect third parties that use a view function.

### No Reentrancy 
File `Reentrancy.spec` contains the rule `no_reentrancy`, a double-parametric rule that is instantiated for every pair `(f,g)` where `f` and `g` are non-view external methods of the contract. In the rule, we call `f` and save the sighash of `g` into `g_sighhash` for future usage. We then hook on any call which is done directly and indirectly from `f` and we simulate a call to `g` using `g_sighhash`. We then save its reverted status in `g_reverted`. At the end of the rule, we have an assert that checks that if we called `g` during the callback, then `g` reverted. 

### Reentrancy Safety 
File `NoGuardSafety.spec` contains a rule `reentrancySafety` that verifies that all storage accesses are either before  or after external calls. This is an approach that allows reentrancy but keeps all storage updates safe.  The property checks that a reentrancy vulnerability cannot occur. It does not check the existence of this vulnerability. 



## Running the specs on the contracts

The folder certora/confs includes a configuration file for each spec on each of the different contracts to be run using `certoraRun <contract>_<spec>.conf`. Alternatively the script.sh can be used to run all specs on all contracts.
The results of the rules on the different contracts are: 

| Rule | VulnerableBank |  BankPartialFix | BankGuardFix | BankNoGuardFix |
| ---| ------------------ | ------- | ---------| --- |
|viewReentrancy| [violated](https://prover.certora.com/output/15800/0530d5603d914d2087a3560c73acff24?anonymousKey=b37e6db066f103ad50782c9e826a29de0e5b3628) |  [violated](https://prover.certora.com/output/15800/fe7c875f8eb74fc29ed0a879f6407611?anonymousKey=03f20f6b7ec263b3eaa661f7404572ab8df76bf0) | [violated](https://prover.certora.com/output/15800/4942ec88782b46a9bbc37dca8c8084a4?anonymousKey=92df0688d664c6aa44ccf0dbd1e23f8cfdebd4af) | [verified](https://prover.certora.com/output/15800/c36fd2fd42b342739131fb3768780df2?anonymousKey=d47d3aee7e0df77a1170b82502f5993dd7e1f6d8)  |
| no_reentrancy | [violated](https://prover.certora.com/output/15800/d15535a06707493a8a876b524c55f686?anonymousKey=ae997cd21a7515e14b1b8cd7583692171f50b3ce)  | [violated](https://prover.certora.com/output/15800/50141ab6b8e647fd983d08704a490206?anonymousKey=737c4f8de69a5c3910a23a985dbb9c0399237201) | [verified](https://prover.certora.com/output/15800/5c5d5559566b40aeb620f8c1837a4e35?anonymousKey=c5c7280348ea2a58fdc37b3a8b2fe16e8e744f8d) | [violated](https://prover.certora.com/output/15800/1718b661e61c47688becb29245d8c9e8?anonymousKey=eb85307095cff61801304e128808c111f1860a34) | 
| reentrancySafety | [violated](https://prover.certora.com/output/15800/13228cf0288043ccb78cea264540465e?anonymousKey=1726103528728e30575bf1ebee88f73b3f2ab7d9) | [violated](https://prover.certora.com/output/15800/f9c195f8157445dab458cb8953d6c593?anonymousKey=7245c6fe2c209f04e809d9f9a446ea1d62f9de85) | [violated](https://prover.certora.com/output/15800/33f4dd555c67472084bf871640b5b931?anonymousKey=a3c404bce15ae439f97e187cfeb5d7b76e0598fb) | [verified](https://prover.certora.com/output/15800/a20bc465020143f5b296eace903a4859?anonymousKey=0e057b320535c74920eb7eb540a2e66f0c01de14) |  
---


The reentrancySafety is violated on VulnerableBank for `withdraw` and `withdrawAll`. The violated case is when:
1. The access to storage in `getUserBalance` sets `storage_access_before_call` to true.
2. The call `msg.sender.call` sets `called_extcall` to true.
3. The storage access to `userBalances[msg.sender]` sets `storage_access_after_call` to true.

Note:
It also shows a violation for `BankGuardFix` as the property checked for does not hold, regardless of the code being a valid solution.


The `no_reentrancy` rule from `Reentrancy.spec` shows that BankPartialFix only has cross-function vulnerability issues. That is, a call to `withdraw` within a call to `withdraw` is not possible. But a call to `withdraw` is possible from within `withdrawAll.`
