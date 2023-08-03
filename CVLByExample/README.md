

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

3. `hook`
   - [Sstore](https://github.com/Certora/Examples/blob/master/CVLByExample/ERC20/certora/specs/ERC20.spec)
   - [Sload]

4. `invariant`
   - [Simple](https://github.com/Certora/Examples/blob/5d7145a760e6b1a3aba692ae556aa078adc88cf4/CVLByExample/BallGame/certora/specs/BallGameCorrect.spec#L7C1-L7C40)
    - [strengthening](https://github.com/Certora/Examples/blob/5d7145a760e6b1a3aba692ae556aa078adc88cf4/CVLByExample/ERC20/certora/specs/ERC20.spec)
    - [preserved](https://github.com/Certora/Examples/blob/master/CVLByExample/ERC20)

5. `methods` block 
   - [ERC20](https://github.com/Certora/Examples/blob/master/CVLByExample/ERC20)

