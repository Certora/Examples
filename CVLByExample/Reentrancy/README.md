# Reentrancy
This directory contains 
  - different versions of a "bank" contract where some of them include Reentrancy vulnerabilities. 
  - CVL rules to detect reentrancy bugs.

## Contracts
The `VulnerableBank.sol`, `VulnerableBankEthernaut.sol`, `VulnerableBankBadFix.sol` include reentrancy vulnerabilities.

In the first contract `VulnerableBank.sol` a  malicious user can reenter the contract in both `withdraw` and `withdrawAll` using the external callbacks in the functions. As the `userBalances` data structure is updated only after calling the callback, a malicious user can drain all the bank's funds using this reentrancy vulnerability. 

The second contract `VulnerableBankEthernaut.sol` is taken from the Ethernaut course https://dev.to/nvn/ethernaut-hacks-level-10-re-entrancy-42o9 and it has a similar vulnerability. In this case, the user can reenter the contract using the callback in the `withdraw` and also drain all the funds of the token.

In `VulnerableBankFixed.sol` we show a good way to protect code from reentrancy using reentrancy guards. This ensures that if the contract is reentered, the whole transaction reverts. 

In `VulnerableBankBadFix.sol`, we show an incomplete way to fix the `VulnerableBank.sol` code, and it is conceptually similar to the Curve hack due to the Vyper bad implementation of reentrancy guards https://osec.io/blog/2023-08-01-vyper-timeline. This is because two different guards are used for the `withdraw` and `withdrawAll` functions. This protects the contract from reentrancy from one function to itself, but does not protect from cross reentrancy between two external functions. 

## Certora
The certora folder include two different folders, `spec` and `conf`. 

In the `spec` folder we added a two different specs `Reentrancy.spec` and `ReentrancyEthernaut.spec` to detect reentrancy in the different versions of `VulnerableBank` and `VulnerableBankEthernaut.sol` respectively. 

Both the versions are conceptually similar and based on an experimental feature which is available in the package `certora-cli-alpha-reentrancy` and will be publicly available in our upcoming versions. In order to use that, you need to first uninstall the official package (if it is already installed) by doing 
`pip uninstall certora-cli`  and then install this one using `pip install certora-cli-alpha-reentrancy`

The rule `no_reentrancy` is a parametric rule which will be instantiated for every pair `(f,g)` where `f` and `g` are non-view external methods of the contract. In the rule, we call `f` and save the sighash of `g` into `g_sighhash` for future usage. Then we hook on any call which is done directly and indirectly from `f` and we simulate a call to `g` using `g_sighhash`. We then save its reverted status in `g_reverted`. In the end of the rule, we have an assert that checks that if we called `g` during the callback, then `g` reverted. 


## Running the spec on the contracts

The `conf` folder includes configuration files to be run using `certoraRun certora/conf/<conf_file>` which run the reentrancy specs on each one of the different contracts. 

Here https://prover.certora.com/output/56986/b5c7f1a4b5934468aba839e35e5955b9?anonymousKey=10b84360717704e5a28b5833306d91c1e147eaf1 you can see the report of running the rule on the contract `VulnerableBank.sol`.

Run it via ```certoraRun certora/conf/ReentrancyVulnerableBank.conf```

Here https://prover.certora.com/output/56986/b5c7f1a4b5934468aba839e35e5955b9?anonymousKey=10b84360717704e5a28b5833306d91c1e147eaf1 you can see the report of running the rule on the contract `VulnerableBankBadFix.sol`.


Here https://prover.certora.com/output/56986/aadae96a3a714ca58819cf47b73bb5cd?anonymousKey=04a38a6e4b92e9081da91c048974588c19034a9b you can see the report of running the rule on the fixed contract `VulnerableBankFixed.sol`.


Here https://prover.certora.com/output/56986/1adecd3f881847f18a24305ca8324aa5?anonymousKey=27d353fb85507ad31f9f62364fee204b9fdf3529 you can see the report of running the rule on the fixed contract `VulnerableBankEthernaut.sol`.
