# Examples for CVL Commands

- `array`
   - access
      - [In a statement](https://github.com/Certora/Examples/blob/master/CVLByExample/Structs/BankAccounts/certora/specs/structs.spec#L88)
      - [In SStore parameter](https://github.com/Certora/Examples/blob/master/CVLByExample/Structs/BankAccounts/certora/specs/structs.spec#L146)
      - [by function call](https://github.com/Certora/Examples/blob/master/CVLByExample/Structs/BankAccounts/certora/specs/structs.spec#L77)
   - [function declaration in method block](https://github.com/Certora/Examples/blob/master/CVLByExample/Structs/BankAccounts/certora/specs/structs.spec#L21)
- [`assert`](https://github.com/Certora/Examples/blob/master/DEFI/ConstantProductPool/certora/spec/ConstantProductPool.spec#L75)

- [`assert_uint256`](https://github.com/Certora/Examples/blob/master/DEFI/ERC20/certora/specs/ERC20Fixed.spec#L180)

- [`at`](https://github.com/Certora/Examples/blob/master/CVLByExample/Storage/certora/specs/storage.spec#L113)

- [builtin rule](https://github.com/Certora/Examples/blob/master/CVLByExample/Reentrancy/certora/spec/ReadOnlyReentrancy.spec#L1)

- [`calldataarg`](https://github.com/Certora/Examples/blob/master/DEFI/ERC20/certora/specs/ERC20Fixed.spec#L83)

- [cvldoc @param](https://github.com/Certora/Examples/blob/master/CVLByExample/Structs/BankAccounts/certora/specs/structs.spec#L44)
- [cvldoc @title](https://github.com/Certora/Examples/blob/master/CVLByExample/NativeBalances/certora/specs/Auction.spec#L11)

- [CVL function](https://github.com/Certora/Examples/blob/master/DEFI/LiquidityPool/certora/specs/pool.spec#L24)
    - [`override`](https://github.com/Certora/Examples/blob/master/CVLByExample/Import/certora/specs/sub.spec#L38)

- [`definition`](https://github.com/Certora/Examples/blob/master/CVLByExample/Import/certora/specs/base.spec#L22)

- [`env`](https://github.com/Certora/Examples/blob/master/DEFI/ERC20/certora/specs/ERC20Fixed.spec#L20)

- [`envfree`](https://github.com/Certora/Examples/blob/master/DEFI/ERC20/certora/specs/ERC20Fixed.spec#L8)

- [`expect`](https://github.com/Certora/Examples/blob/master/CVLByExample/Summarization/MultiContract/certora/specs/FunctionSummary.spec#L11)

- [`filtered`](https://github.com/Certora/Examples/blob/master/CVLByExample/Reentrancy/certora/spec/Reentrancy.spec#L29)

- [`forall`](https://github.com/Certora/Examples/blob/master/CVLByExample/QuantifierExamples/DoublyLinkedList/certora/spec/dll-linkedcorrectly.spec#L13)

- [Function call](https://github.com/Certora/Examples/blob/master/DEFI/ERC20/certora/specs/ERC20Fixed.spec#L123)

- `ghost`
   - [ghost variable]
      - [simple variable example](https://github.com/Certora/Examples/blob/master/DEFI/ERC20/certora/specs/ERC20Full.spec#L72)

      - [ghost mapping](https://github.com/Certora/Examples/blob/master/CVLByExample/Structs/BankAccounts/certora/specs/structs.spec#L118)
   - [ghost function](https://github.com/Certora/Examples/blob/master/CVLByExample/QuantifierExamples/DoublyLinkedList/certora/spec/dll-linkedcorrectly.spec#L24)
   - [`init_state`](https://github.com/Certora/Examples/blob/master/DEFI/ConstantProductPool/certora/spec/ConstantProductPool.spec#L219)
   - [`axiom`](https://github.com/Certora/Examples/blob/master/CVLByExample/Structs/BankAccounts/certora/specs/structs.spec#L120)
   - [ghost summary](https://github.com/Certora/Examples/blob/master/CVLByExample/Summarization/GhostSummary/GhostMapping/certora/specs/WithGhostSummary.spec#L4)

- `hook`
   - [`Sstore`](https://github.com/Certora/Examples/blob/master/DEFI/ERC20/certora/specs/ERC20Full.spec#L88)
   - [`Sload`](https://github.com/Certora/Examples/blob/master/DEFI/ERC20/certora/specs/ERC20Full.spec#L84)

- [`import`](https://github.com/Certora/Examples/blob/master/CVLByExample/Import/certora/specs/sub.spec#L1)

- `invariant`
   - [simple](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/BallGame/certora/specs/BallGameCorrect.spec#L7)
    - [strengthening](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/BallGame/certora/specs/BallGameCorrect.spec#L7)
    - [`preserved`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20.spec#L128)
      - [`with (env e)`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20.spec#L128)

    - `requireInvariant`
        - [in a rule](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L178)
        - [in a `CVL` function](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/LiquidityPool/certora/specs/pool.spec#L27)

- [`lastreverted`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20.spec#L49)

- [`laststorage`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/storage/certora/specs/storage.spec#L28)

- [`mathint`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L23C5-L23C12)

- [`method`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L83)

- `methods` block 
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

- [`nativeBalances`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/NativeBalances/certora/specs/Auction.spec#L24)

- [`optional`](https://github.com/Certora/Examples/blob/2b5dabe83d8fae7292ce7c2b59e89a24fd2bcbdc/CVLByExample/optional/certora/specs/Base.spec#L5)
- `override`
   - [`definition`](https://github.com/Certora/Examples/blob/be09cf32c55e39f5f5aa8cba1431f9e519b52365/CVLByExample/import/certora/specs/sub.spec#L36)
   - [`function`](https://github.com/Certora/Examples/blob/be09cf32c55e39f5f5aa8cba1431f9e519b52365/CVLByExample/import/certora/specs/sub.spec#L38)

- [`require`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L44)

- [`require_uint256`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20.spec#L166)

- `rule`
   - [simple](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/LiquidityPool/certora/specs/pool.spec#L54)
   - [parameterized]
      -[simple parameters](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/LiquidityPool/certora/specs/pool.spec#L24)
      - [method parameter](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L94)

- [`satisfy`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L243)

- [`selector`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L92)

- [`sig`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L92)

- [`storage`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/storage/certora/specs/storage.spec#L28)
    - [of a contract](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/storage/certora/specs/storage.spec#L87)
    - [of a ghost](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/storage/certora/specs/storage.spec#L149)
    - [of nativeBalances](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/storage/certora/specs/storage.spec#L117)
    - [full storage](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/storage/certora/specs/storage.spec#L107)
    - [`laststorage`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/storage/certora/specs/storage.spec#L28)
    - [direct storage access](https://github.com/Certora/Examples/blob/e28367462ee52f31e5ac84bad7fa26cf6b808cdc/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L48)

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

- Summarization
   - [`ALWAYS`](https://github.com/Certora/Examples/blob/8d58ba44af0b22cc8f7703542c248cd225d26ccc/CVLByExample/function-summary/multi-contract/certora/specs/spec_with_summary.spec#L22) 
   - [`CONSTANT`](https://github.com/Certora/Examples/blob/8136b977cfe2fbf8e9e7ab0d74896cc62403fdb8/CVLByExample/function-summary/simple/certora/specs/ConstantVSNondet.spec#L5)
   - [`NONDET`](https://github.com/Certora/Examples/blob/bf3255766c28068eea2d0513edb8daca7bcaa206/CVLByExample/function-summary/with-side-effects/certora/specs/HavocAllVSNondet.spec#L5)
   - [`HAVOC_ALL`](https://github.com/Certora/Examples/blob/8d58ba44af0b22cc8f7703542c248cd225d26ccc/CVLByExample/function-summary/with-side-effects/certora/specs/HavocAllVSNondet.spec#L3)
   - [`DISPATCHER`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L36C4-L36C4)
   - Summary Application
      - [ALL](https://github.com/Certora/Examples/blob/8d58ba44af0b22cc8f7703542c248cd225d26ccc/CVLByExample/function-summary/multi-contract/certora/specs/spec_with_summary.spec#L23)
      - [UNRESOLVED](https://github.com/Certora/Examples/blob/752bb111907f7aa538c81672aa960d932ffca1f5/CVLByExample/function-summary/Library/DirectSummary/certora/specs/AllDirect.spec#L27)
      - [direct summarization](https://github.com/Certora/Examples/blob/752bb111907f7aa538c81672aa960d932ffca1f5/CVLByExample/function-summary/Library/DirectSummary/certora/specs/AllDirect.spec#L6)
      - [wildcard summarization](https://github.com/Certora/Examples/blob/752bb111907f7aa538c81672aa960d932ffca1f5/CVLByExample/function-summary/Library/DirectSummary/certora/specs/AllDirect.spec#L27)
   - [CVL Function Summary](https://github.com/Certora/Examples/blob/8d58ba44af0b22cc8f7703542c248cd225d26ccc/CVLByExample/function-summary/multi-contract/certora/specs/spec_with_summary.spec#L6)
   - [Ghost Summary](https://github.com/Certora/Examples/blob/7a13d19cb450effac1b937115ca7b20c23f1ab74/CVLByExample/function-summary/ghost-summary/certora/specs/WithGhostSummary.spec#L3)


- [`to_mathint`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L45C66-L45C76)

- `use`
   - `rule`
      - [with filters](https://github.com/Certora/Examples/blob/be09cf32c55e39f5f5aa8cba1431f9e519b52365/CVLByExample/import/certora/specs/sub.spec#L3)
      - [overriding imported filters](https://github.com/Certora/Examples/blob/be09cf32c55e39f5f5aa8cba1431f9e519b52365/CVLByExample/import/certora/specs/sub.spec#L3)
   - [`invariant`](https://github.com/Certora/Examples/blob/be09cf32c55e39f5f5aa8cba1431f9e519b52365/CVLByExample/import/certora/specs/sub.spec#L8)
      - [overriding imported `preserved`](https://github.com/Certora/Examples/blob/be09cf32c55e39f5f5aa8cba1431f9e519b52365/CVLByExample/import/certora/specs/sub.spec#L10)
      - [adding a `preserved` block](https://github.com/Certora/Examples/blob/be09cf32c55e39f5f5aa8cba1431f9e519b52365/CVLByExample/import/certora/specs/sub.spec#L14)
   - [builtin rule](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/ReadOnlyReentrancy/certora/spec/ReadOnlyReentrancy.spec#L1)

- [`using`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/LiquidityPool/certora/specs/pool_link.spec#L14)

- [`withrevert`](https://github.com/Certora/Examples/blob/14668d39a6ddc67af349bc5b82f73db73349ef18/CVLByExample/storage/certora/specs/storage.spec#L45C19-L45C19)


These examples can serve as an introduction to CVL ( Certora Verification Language ).
It also contains examples that are based on real-life code and the spec that have caught critical bugs.

See https://docs.certora.com for a complete guide. 


To run the examples, use the provided configuration: 
```
cd ConstantProductPoolExample 
certoraRun ConstantProductPoolExample/certora/conf/run.conf 
```

This will result in a run with violations as seen [here](https://prover.certora.com/output/40726/b2c63e002e864e9d94b6ee03bf49cef0?anonymousKey=b8b428b78410796d656109f8f2b6436202e139f5).

For the fixed version, ConstantProductPoolFixed.sol run:
```certoraRun ConstantProductPoolExample/certora/conf/runFixed.conf```

runNondetSummary and runHavocSummary wait for https://certora.atlassian.net/browse/CERT-3825?filter=-2
