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

The spec `ghostSums.spec` uses the new `sum` keyword for an invariant that checks that the total supply of tokens is always equal to the sum of balances.

To run this spec use:
```
certoraRun ghostSums.conf
```
[A report of this run](https://prover.certora.com/output/15800/bd1d17a747e14492a2ba045cc030f620?anonymousKey=359cd5fa902d410378ca59fb32029681eae61ab3)