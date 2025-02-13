# Ghost Summations (`sum`/`usum`)
Given a ghost mapping we can sum over some subset (or all) of the keys to the mapping, and the value is the sum of all values that were written to the ghost over those indices.
To do it CVL introduces 2 new keywords:
* `sum` - Used to sum elements with signed values (e.g. int).
* `usum` - Can be used to sum elements with unsigned values (e.g. uint) including `mathint`. It functions similarly to `sum` but adds more assumptions to promise that the sum is greater than it's parts.

For example:
```
ghost mapping(address => mapping(uint => int)) myGhost;
rule r {
    ... // some stuff that writes values to myGhost
	address a;
    assert sum uint u. myGhost[a][u] > 0;
}
```

Restrictions:
* We can only sum ghosts, not e.g. direct storage access of mappings.
* The summed variables must be used, and can only be used as indices to the ghost (so e.g. sum uint u. myGhost[a][u*2] won't work).
* for `sum` we only sum values that were written to the ghost, we don't know what there is in the other slots.

## SimpleToken
The contract `SimpleToken` is a simple token implementation that supports balances of users, and minting, burning and transferring tokens.

The spec `ghostSums.spec` uses the new `sum` keyword for a rule that checks that the total supply of tokens is equal to the sum of balances after every function activation.

To run this spec use:
```
certoraRun ghostSums.conf
```
[A report of this run](https://vaas-stg.certora.com/output/15800/3fa0a8471c4949bcbf36f2ba4523ef20?anonymousKey=df74bdd5c4d125425645dcda6fbe8bf347338692)