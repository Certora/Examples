# Ghost Summations (`sum`/`usum`)
Given a ghost mapping we can sum over some subset (or all) of the keys to the mapping, and the value is the sum of all values that were written to the ghost over those indices.
To do it CVL introduces 2 new keywords:
* `sum` - Used to sum elements with signed values (e.g. int).
* `usum` - Used to sum elements with unsigned values (e.g. uint) including `mathint`.

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
* We only sum values that were written to the ghost, we don't know what there is in the other slots.

The spec `ghostSums.spec` provides some example rules that use the keywords `sum` and `usum` in different scenarios.
To run this spec on `ghostSums.sol` use:
```
certoraRun ghostSums.conf
```
[A report of this run](https://prover.certora.com/output/15800/c88c78a33c9a4e91ad5c9f112bced351?anonymousKey=b8ef9513392aee530f51aa940c0515cc918805c4)