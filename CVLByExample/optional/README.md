This directory gives an example for using the method block option `optional`.
`optional` is a way to have a spec that is useful for several contracts which refers to functions that are defined only
in part of them. A rule is skipped in runs of configuartions where the --verify option is applied to a contract that does not define some function in the rule.

The contracts:
- `Base` - contains the function `bar(uint256)`.
- `Partial` - does not contain the function `bar`.

All rules in the spec contain references to bar(uint256). 

In the following command the main contract is `Base`:

[Report of this run](https://prover.certora.com/output/1902/e817a29d683f4ecb9bda9b150bef6083?anonymousKey=863734223abf15443e74ebbb22fad4a724302c31)

Since `bar` is defined in `Base`, all rules pass.

In the following command the main contract is `Partial`:

```certoraRun certora/conf/runPartialOptional.conf```

[Report of this run](https://prover.certora.com/output/1902/b5cd98af4a11465baea9b469459f9b6b?anonymousKey=2ffe394f28621fa9a74311fe9a52036f014acb42)

Since `bar` is undefined in `Partial` all rules are skipped.
