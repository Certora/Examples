This directory demonstrates importing a spec file in another spec file.
This includes:
- Using a function defined in the imported spec.
- Overriding definitions from the imported spec.
- Overriding preserved from the imported spec.

The imported spec is `Base.spec`.
The invariant `invInBase` fails because not strong enough.

Run this spec via
```certoraRun certora/conf/runImported.conf```

[The report of this run](https://prover.certora.com/output/1902/41975cd5c11248cc8bab03c8631ba3de?anonymousKey=e862f233939d5cc5c2e75e5b5001d96b37ffe87d)

The importing spec is `sub.spec`
In this spec the above invariant is strengthened with `preserved` blocks and passes.
Run this spec via
```certoraRun certora/conf/runImport.conf```

[The report of this run](https://prover.certora.com/output/1902/7490813e5ec94e8089de1e96abfd297f?anonymousKey=4316608d5e7c0b72c4e25aa551a31d3846f15cf9)

