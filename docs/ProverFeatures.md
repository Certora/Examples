# Certora Prover Features

## Rule
- [simple](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/LiquidityPool/certora/specs/pool.spec#L54)
- parameterized
	-[simple parameters](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/LiquidityPool/certora/specs/pool.spec#L24)
	- [method parameter](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L94)
- [builtin rule](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ReadOnlyReentrancy/certora/spec/ReadOnlyReentrancy.spec#L1)


## Handling user defined types
- `struct`
	- [struct return type](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L46)
- `struct` in `methods` block
	- [`struct` parameter](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L22)
	- [`struct` return type](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L18)
	- [returning a `struct` as a tuple](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L20)
- `struct` in a `CVL` function
	- [`struct` parameter to a `CVL` function](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L35)
	- [`struct` return type of a `CVL` function](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L46)
	- [returning `struct` as a tuple](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L52)
- [assignment to struct](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L97)
- [Assigning `struct` to a tuple](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L76)

- `array`
	- access
		- [In a statement](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L87)
		- [In SStore parameter](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L146)
		- [by function call](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L76)
	- [function declaration in method block](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L20C5-L20C74)
- `enum` 

## Invariant
	- [simple](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/BallGame/certora/specs/BallGameCorrect.spec#L7)
    - [strengthening](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/BallGame/certora/specs/BallGameCorrect.spec#L7)
    - [`preserved`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20.spec#L128)
      - [`with (env e)`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20.spec#L128)

    - `requireInvariant`
        - [in a rule](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L178)
        - [in a `CVL` function](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/LiquidityPool/certora/specs/pool.spec#L27)

## Multiple Contracts
	- [how to call external contract from spec](https://github.com/Certora/Examples/blob/8cf3807dd1aaa13c09140a8072790f786bee9d56/CVLByExample/LiquidityPool/certora/specs/pool_link.spec#L28)

## Method declaration
- [Calls to external contracts](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L29)
    - [envfree](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L19C50-L19C57)
    - [`with (env)`]
    - Summary
        - [`ALWAYS`](https://github.com/Certora/Examples/blob/8d58ba44af0b22cc8f7703542c248cd225d26ccc/CVLByExample/function-summary/multi-contract/certora/specs/spec_with_summary.spec#L22)
        - [`AUTO`]
        - [`CONSTANT`](https://github.com/Certora/Examples/blob/8136b977cfe2fbf8e9e7ab0d74896cc62403fdb8/CVLByExample/function-summary/simple/certora/specs/ConstantVSNondet.spec#L5)
        - [DISPATCHER](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L36C4-L36C4)

        - [`NONDET`](https://github.com/Certora/Examples/blob/bf3255766c28068eea2d0513edb8daca7bcaa206/CVLByExample/function-summary/with-side-effects/certora/specs/HavocAllVSNondet.spec#L5)
        - [`HAVOC_ALL`](https://github.com/Certora/Examples/blob/bf3255766c28068eea2d0513edb8daca7bcaa206/CVLByExample/function-summary/with-side-effects/certora/specs/HavocAllVSNondet.spec#L3)
        - Summary Application
            - [ALL](https://github.com/Certora/Examples/blob/8d58ba44af0b22cc8f7703542c248cd225d26ccc/CVLByExample/function-summary/multi-contract/certora/specs/spec_with_summary.spec#L23)
            - [UNRESOLVED](https://github.com/Certora/Examples/blob/752bb111907f7aa538c81672aa960d932ffca1f5/CVLByExample/function-summary/Library/DirectSummary/certora/specs/AllDirect.spec#L27)
        - [direct summarization](https://github.com/Certora/Examples/blob/752bb111907f7aa538c81672aa960d932ffca1f5/CVLByExample/function-summary/Library/DirectSummary/certora/specs/AllDirect.spec#L6)
        - [wildcard summarization](https://github.com/Certora/Examples/blob/752bb111907f7aa538c81672aa960d932ffca1f5/CVLByExample/function-summary/Library/DirectSummary/certora/specs/AllDirect.spec#L27)
        - [CVL Function Summary](https://github.com/Certora/Examples/blob/bf3255766c28068eea2d0513edb8daca7bcaa206/CVLByExample/function-summary/multi-contract/certora/specs/spec_with_summary.spec#L6))
        - [Ghost Summary](https://github.com/Certora/Examples/blob/7a13d19cb450effac1b937115ca7b20c23f1ab74/CVLByExample/function-summary/ghost-summary/certora/specs/WithGhostSummary.spec#L3)
        
    - [`optional`](https://github.com/Certora/Examples/blob/2b5dabe83d8fae7292ce7c2b59e89a24fd2bcbdc/CVLByExample/optional/certora/specs/Base.spec#L5)
    - ['expect'](https://github.com/Certora/Examples/blob/bf3255766c28068eea2d0513edb8daca7bcaa206/CVLByExample/function-summary/multi-contract/certora/specs/spec_with_summary.spec#L6)


## Relation
	- [`at`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/storage/certora/specs/storage.spec#L114)


## revert
	- [`lastreverted`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20.spec#L49)
	- [`withrevert`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/storage/certora/specs/storage.spec#L45C19-L45C19)

## Ghost
	- [ghost variable](https://docs.certora.com/en/latest/docs/confluence/anatomy/definitions.html?highlight=ghost#basic-definitions)
		- [simple variable example](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20.spec#L113)

		- [ghost mapping](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L117)
	- [ghost function](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/QuantifierExamples/DoublyLinkedList/certora/spec/dll-linkedcorrectly.spec#L24)
	- [`init_state`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L207)
	- [`axiom`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L119)
	- [ghost summary](https://github.com/Certora/Examples/blob/7a13d19cb450effac1b937115ca7b20c23f1ab74/CVLByExample/function-summary/ghost-summary/certora/specs/WithGhostSummary.spec#L3)

## Summaries 





