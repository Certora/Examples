# Non-payable Function msg.value Revert
A payable function in Solidity is a function that can receive ether when called. When trying to send ether to a function that is not defined as payable the transaction will automatically revert.

The spec provided has 2 rules:
* `NonPayableRevertExample` fails intentionally to show how a revert like the one described above is shown in the prover calltrace.
* `NonPayableRevertingConditions` proves the conditions of reverts for a non payable empty function.


Run this spec using:
```certoraRun NonPayableRevert.conf```

[A report of this run](https://prover.certora.com/output/15800/6cefdfb056544633b5383996dc139fb4?anonymousKey=46a60fd9d0714031b14a13e106367d473e76b765)