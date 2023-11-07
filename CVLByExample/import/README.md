# import
This directory demonstrates importing a spec file in another spec file.
This includes:
- Using a rule/invariant defined in the imported spec.
- Overriding definitions from the imported spec.
- Overriding preserved from the imported spec.

## The imported spec `Base.spec`.

Run this spec via
```certoraRun certora/conf/runImported.conf```

[The report of this run](https://prover.certora.com/output/1902/7c187b4f4307426d996f6f51bff1fc2d/?anonymousKey=6cd69a609d7a778f9c791b2be036c14bcf06c7cc)

The invariant `invInBase` fails for the function `minusSevenSomeUInt`.

## The importing spec `sub.spec`
In this spec the above invariant is strengthened with `preserved` blocks and passes.
Run this spec via
```certoraRun certora/conf/runImport.conf```

The rules `parametricRuleInBase` and `twoParametricRuleInBase` fail because they call `callF` that is nonpayable therefore `require msg.sender > 0` cannot hold.


[The report of this run](https://prover.certora.com/output/1902/6993e42943214f84b915a66de18f4b2b?anonymousKey=d6949f0b501694156a965515e0885fcdf9b18c52)

