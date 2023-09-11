

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
```
certoraRun ConstantProductPoolExample/certora/conf/runFixed.conf 
```

## Examples for CVL Commands

- [`assert`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L75C5-L75C12)

- [`calldataarg`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L115C3-L115C14)

- [CVL function](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/LiquidityPool/certora/specs/pool.spec#L24)
    - [`override`]

- [`env`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L19C5-L19C8)

- `envFree` 
   - [envfree](https://github.com/Certora/Examples/tree/master/CVLByExample/ERC20#:~:text=ERC20.spec%20as-,envfree,-but%20it%20refers)

- [`exists`]

- [`forall`](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/QuantifierExamples/DoublyLinkedList/certora/spec/dll-linkedcorrectly.spec#L13C22-L13C28)

- [Function call](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L117C3-L117C13)

- `ghost`
   - [ghost variable](https://docs.certora.com/en/latest/docs/confluence/anatomy/definitions.html?highlight=ghost#basic-definitions )
   - [simple variable example](https://github.com/Certora/Examples/blob/2d729bcc944a776d94676a86044163fb545df28e/CVLByExample/ERC20/certora/spec/ERC20.spec#L115)
   -[`init_state`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L207C2-L207C12)

- `hook`
   - [Sstore](https://github.com/Certora/Examples/blob/master/CVLByExample/ERC20/certora/specs/ERC20.spec)
   - [Sload]

- [`init_state``](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L207C2-L207C12)

- `invariant`
   - [Simple](https://github.com/Certora/Examples/blob/5d7145a760e6b1a3aba692ae556aa078adc88cf4/CVLByExample/BallGame/certora/specs/BallGameCorrect.spec#L7C1-L7C40)
    - [strengthening](https://github.com/Certora/Examples/blob/5d7145a760e6b1a3aba692ae556aa078adc88cf4/CVLByExample/ERC20/certora/specs/ERC20.spec)
    - [preserved](https://github.com/Certora/Examples/blob/master/CVLByExample/ERC20)
      - [`with (env e)`]

    - [requireInvariant]
        - [in a rule](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L178C5-L178C21)
        - [in a `CVL` function](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/LiquidityPool/certora/specs/pool.spec#L27)

- [`lastreverted`](https://github.com/Certora/Examples/blob/master/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec)

- [`laststorage`](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L112C23-L112C35)


- [`mathint`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L27C5-L27C12)

- [`method`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L116C3-L116C9)

- `methods` block 
   - [Calls to external contracts](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L29C14-L29C31)
   - [envfree](https://github.com/Certora/Examples/tree/master/CVLByExample/ERC20#:~:text=ERC20.spec%20as-,envfree,-but%20it%20refers)
   - [Function Summary]
        - [DISPATCHER](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L36C4-L36C4)
        - [`ALWAYS`] 
        - [`CONSTANT`]
        - [`PER_CALLEE_CONSTANT`]
        - [`NONDET`]
        - [`HAVOC_ECF`]
        - [`HAVOC_ALL`]
        - [`AUTO`]
        - [`URESOLVED`]
        - [`DISPATCHER`] - liquidity/flashloan
        - [CVL Function Summary]
        - [Ghost Summary]
        
    - [`expects`]
    - [`optional`]

- [`nativeBalances`](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/NativeBalances/certora/specs/Auction.spec#L15C29-L15C43)     

- [`require`] (https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L236C5-L236C12)

- [`satisfy`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L243C5-L243C12)

- [`storage`](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L95C5-L95C13)
    - [of a contract](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/storage/certora/specs/storage.spec#L93)
    - [of a ghost](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/storage/certora/specs/storage.spec#L187)
    - [of nativeBalances](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/storage/certora/specs/storage.spec#L98)
    - [full storage](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/storage/certora/specs/storage.spec#L62)

- [`struct`]
   - [struct return type](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L17C5-L17C84)
   - [`struct` in `methods` block]
      - [`struct` parameter](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L23)
      - [`struct` return type](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L19)
      - [returning a `struct` as a tuple](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L21)
   - [`struct` in a `CVL` function]
      - [`struct` parameter to a `CVL` function](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L36)
      - [`struct` return type of a `CVL` function](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L47)
      - [returning `struct` as a tuple](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L53)
   - [assignment to struct](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L59C5-L59C41)
   - [Assigning `struct` to a tuple](https://github.com/Certora/Examples/blob/6f2488a137d92cf722eb2663c42a8a1936afce35/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L77)


- [`to_mathint`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L75C5-L75C12)

- `use`
   - `rule`
   - `invariant`

- [Function Summarization]
   - [`ALWAYS`] 
   - [`CONSTANT`]
   - [`PER_CALLEE_CONSTANT`]
   - [`NONDET`]
   - [`HAVOC_ECF`]
   - [`HAVOC_ALL`]
   - [`AUTO`]
   - [`URESOLVED`]
   - [`DISPATCHER`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L36C4-L36C4) maybe take liquidity/flASHLoan instead.
   - [CVL Function Summary]
   - [Ghost Summary]

- [`using`](https://github.com/Certora/Examples/blob/sitvanit/struct-examples/CVLByExample/LiquidityPool/certora/specs/pool_link.spec)

- [`withrevert`](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L94C5-L94C24)

- [`description`]
- [`good_description`]
- [`havoc assuming`]
- [`sort`]




 






