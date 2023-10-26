This directory gives an example for using the method block option `optional`.
`optional` is a way to have a spec that is useful for several contracts which refers to functions that are defined only
in part of them. A rule is skipped in runs of configuartions where the --verify option is applied to a contract that does not define some function in the rule.

The contracts:
- `Base` - contains the function `bar(uint256)`.
- `Partial` - does not contain the function `bar`.

There are two rules in the spec that contain references to bar(uint256) and one parameteric rule calling the parameteric
method.

In the following command the main contract is `Base`:

[Report of this run](https://prover.certora.com/output/1902/a6759bcddb27453da64df5ab78688399?anonymousKey=62ddd4345b37b05aab6f944c6d58c723cf0d6cf7)

Since `bar` is defined in `Base`, all rules pass.

In the following command the main contract is `Partial`:

```certoraRun certora/conf/runPartialOptional.conf```

[Report of this run](https://prover.certora.com/output/1902/4debeed49dc8454c9f93b997a171ee7a?anonymousKey=f4bf333d142c0fa80380f791576379e44fb920bf)

Since `bar` is undefined in `Partial` the non-parameterized rules are skipped while the parameterized rule instantiates
only the functions present in `Partial` and pass.

