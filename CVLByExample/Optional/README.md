# optional

This directory gives an example for using the method block option `optional`.
`optional` is a way to have a spec that is useful for several contracts which refers to functions that are defined only
in part of them. A rule is skipped in runs of configuartions where the --verify option is applied to a contract that does not define some function in the rule.

## The contracts:
- `Base` - contains the function `bar(uint256)`.
- `Partial` - does not contain the function `bar`.

## The spec
There are two rules in the spec that contain references to bar(uint256) and one parametric rule calling the parametric
method.

In the following command the main contract is `Base`:

```certoraRun runBaseOptional.conf```

[Report of this run](https://prover.certora.com/output/15800/506806227cfa4bf8adb33216eff2a10c?anonymousKey=c7f370dbcfce5051d9d25092c7f06bc91b00c3d2)

Since `bar` is defined in `Base`, all rules pass.

In the following command the main contract is `Partial`:

```certoraRun runPartialOptional.conf```

[Report of this run](https://prover.certora.com/output/15800/212d2c2419bd4663ade6238d3d9ed73c?anonymousKey=4a58c3ba998ff8b7279666c1f439060fa0ae77a0)

Since `bar` is undefined in `Partial` the non-parameterized rules are skipped while the parameterized rule instantiates
only the functions present in `Partial` and pass.

