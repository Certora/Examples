This directory demonstrates summarizing functions by ghosts.
The function `continuous_interest` includes some arithmetic that is very difficult for the underlying SMT solver to reason about and two things may happen.

The Prover uses "overapproximations" of the arithmetic operations in the resulting formula. Basically this means that we allow 
behaviors that include the behavior of the function, but also additional behaviors. Basically, this means that a counterexample may not be a real counterexample (i.e. not actually possible program behavior).

With the current specification the tool reports a wrong violation of the rule `yield_monotonic`. This is where function summarization becomes useful, since we get to decide how we would like to overapproximate our function. 

This version is run via
```certoraRun.py certora/conf/runInterestNotSummarized.conf```
[A report of this run](https://prover.certora.com/output/1902/18f536c055eb4ec9914a29be80311b6b?anonymousKey=727bc70281ed3f35a0840d6a4b4db8abcf0e854d)

The function `continuous_interest` is replaced by the ghost `ghost_interest` that includes an axiom that assures monotonicity.
With this specification the rule passes.

This version is run via
```certoraRun.py certora/conf/runInterest.conf```

[A report of this run](https://prover.certora.com/output/1902/73a895f7ded84eb8825a0148f34d8239?anonymousKey=c6fb5f93904323fc4026e4f05e22ca6d56329c46)