This directory gives an example for using the method block option `optional`.
`optional` is a way to have a spec that is useful for several contracts which refers to functions that are defined only
in part of them. A rule is skipped in runs of configuartions where the --verify option is applied to a contract that does not define some function in the rule.

The contracts:
- `Base` - contains the function `bar(uint256)`.
- `Partial` - does not contain the function `bar`.

There are two rules in the spec that contain references to bar(uint256) and one parametric rule calling the parametric
method.

In the following command the main contract is `Base`:

```certoraRun certora/conf/runBaseOptional.conf```

[Report of this run](https://prover.certora.com/output/1902/824f4c76e4ff4c99aab3894c4bfcd0b8?anonymousKey=7ae477960d6d4399a4875eeca3ead98445767abe)

Since `bar` is defined in `Base`, all rules pass.

In the following command the main contract is `Partial`:

```certoraRun certora/conf/runPartialOptional.conf```

[Report of this run](https://prover.certora.com/output/1902/f9364f3f537a4054bb43e792e78e78d7?anonymousKey=28c5350fb911e6aac4bb4e6a6c34ba4ef130d9da)

Since `bar` is undefined in `Partial` the non-parameterized rules are skipped while the parameterized rule instantiates
only the functions present in `Partial` and pass.

