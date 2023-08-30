

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
1. `envFree` 
   - [envfree](https://github.com/Certora/Examples/tree/master/CVLByExample/ERC20#:~:text=ERC20.spec%20as-,envfree,-but%20it%20refers)

2. `ghost`
   - [ghost variable](https://docs.certora.com/en/latest/docs/confluence/anatomy/definitions.html?highlight=ghost#basic-definitions )
   - [simple variable example](https://github.com/Certora/Examples/blob/2d729bcc944a776d94676a86044163fb545df28e/CVLByExample/ERC20/certora/spec/ERC20.spec#L115)
   -[`init_state`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L207C2-L207C12)

3. `hook`
   - [Sstore](https://github.com/Certora/Examples/blob/master/CVLByExample/ERC20/certora/specs/ERC20.spec)
   - [Sload]

4. `invariant`
   - [Simple](https://github.com/Certora/Examples/blob/5d7145a760e6b1a3aba692ae556aa078adc88cf4/CVLByExample/BallGame/certora/specs/BallGameCorrect.spec#L7C1-L7C40)
    - [strengthening](https://github.com/Certora/Examples/blob/5d7145a760e6b1a3aba692ae556aa078adc88cf4/CVLByExample/ERC20/certora/specs/ERC20.spec)
    - [preserved](https://github.com/Certora/Examples/blob/master/CVLByExample/ERC20)
    - [requireInvariant](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L178C5-L178C21)

5. `methods` block 
   - [ERC20](https://github.com/Certora/Examples/blob/master/CVLByExample/ERC20)
   - [Calls to external contracts](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L29C14-L29C31)
   - [DISPATCHER](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L36C4-L36C4)
   - [envfree](https://github.com/Certora/Examples/tree/master/CVLByExample/ERC20#:~:text=ERC20.spec%20as-,envfree,-but%20it%20refers)

6. [`require`] (https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L236C5-L236C12)

7. [`satisfy`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L243C5-L243C12)

8. [`to_mathint`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L75C5-L75C12)

9. [`assert`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L75C5-L75C12)

10. [`init_state``](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ConstantProductPool/certora/spec/ConstantProductPool.spec#L207C2-L207C12)

11. [`mathint`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L27C5-L27C12)

12. [`env`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L19C5-L19C8)

13 [Function call](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L117C3-L117C13)

14. [`method`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L116C3-L116C9)

15. [`calldataarg`](https://github.com/Certora/Examples/blob/631ba01b47f126dad8d1c067dd2277fb58bf616b/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec#L115C3-L115C14)

16. [`withrevert`](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L94C5-L94C24)

17. [`lastreverted`](https://github.com/Certora/Examples/blob/master/CVLByExample/ERC20/certora/specs/ERC20Fixed.spec)

18. [`using`](https://github.com/Certora/Examples/blob/sitvanit/struct-examples/CVLByExample/LiquidityPool/certora/specs/pool_link.spec)

19. `struct``
- [struct return type](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L17C5-L17C84)
- [Assignment to `struct`]
- [Assigning `struct` to a tuple]
- [`struct` in `methods` block]
   - [`struct` parameter]
   - [`struct` return type]
- [`struct` parameter to a cvl function]

20. [assignment to struct](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L59C5-L59C41)

21. [`storage`](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L95C5-L95C13)

22. [`laststorage`](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/structs/BankAccounts/certora/specs/Bank.spec#L112C23-L112C35)

23. [`nativeBalances`](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/NativeBalances/certora/specs/Auction.spec#L15C29-L15C43)

24. [`forall`](https://github.com/Certora/Examples/blob/be53640d5698afc1589ba0a2bd662d8c1512b69f/CVLByExample/QuantifierExamples/DoublyLinkedList/certora/spec/dll-linkedcorrectly.spec#L13C22-L13C28)

25. `use`
   - `rule`
   - `invariant`

- [Function summarization]
   - [`ALWAYS`] {
   - `CONSTANT`
   - `PER_CALLEE_CONSTANT``
 NONDET" {
    debug(" NONDET",yytext());
    return symbol(sym.NONDET,yytext());
}
<YYINITIAL> "HAVOC_ECF" {
    debug(" HAVOC_ECF",yytext());
    return symbol(sym.HAVOC_ECF,yytext());
}
<YYINITIAL> "HAVOC_ALL" {
    debug(" HAVOC_ALL",yytext());
    return symbol(sym.HAVOC_ALL,yytext());
}
<YYINITIAL> "AUTO" {
    debug(" AUTO",yytext());
    return symbol(sym.AUTO,yytext());
}
<YYINITIAL> "UNRESOLVED" {
    debug(" UNRESOLVED",yytext());
    return symbol(sym.UNRESOLVED,yytext());
}






