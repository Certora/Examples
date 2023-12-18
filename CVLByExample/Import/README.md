# import
This directory demonstrates importing one specification file into another.
This includes:
- Using a rule/invariant defined in the imported specification.
- Overriding definitions from the imported specification.
- Overriding preserved from the imported specification.

## The imported spec `Base.spec`

Run this spec via
```certoraRun runImported.conf```

[The report of this run](https://prover.certora.com/output/15800/f78228233559427795d848d21602a5b0?anonymousKey=e190cef7409ac69f9c13fb7f83aa820ae2c8b80d)

The invariant `invInBase` fails for the function `minusSevenSomeUInt`.

## The importing spec `sub.spec`
In this specification the invariant above is strengthened with `preserved` blocks and passes.

Run this specification via
```certoraRun runImport.conf```

The rules `parametricRuleInBase` and `twoParametricRuleInBase` fail because they call `callF` that is `nonpayable` therefore `require msg.sender > 0` cannot hold.

[The report of this run](https://prover.certora.com/output/15800/709616ff05194b03b9de85fe11379de4?anonymousKey=8d06cef40ffd0bc8f84be5170bba63cd0597572c)

