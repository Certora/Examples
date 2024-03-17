# Summarizing a Square Root Function

In this example we'll try to prove that adding liquidity to a certain protocol is monotonic. But there is a problem,
the protocol computes some square roots as part of it's calculations.

Run the following spec:
```certoraRun runUnsummarizedSqrRoot.conf```
[A report of this run](https://prover.certora.com/output/15800/305a18aa989940d0857e3c928d26dd46?anonymousKey=1f2dd488f9d710622ae9757f27c84642f7d43e45)

As you can see, the prover timed out trying to prove the rule. This is due to the nature of the complex math square root operation.
In order to solve this timeout, we can try using a feature of the prover that will automatically use NONDET summarizations for
difficult* internal functions.
To enable this option you can add the flag `--auto_nondet_difficult_internal_funcs`, it is already included in the following conf.

Run it using:
```certoraRun runAutoSummarizedSqrRoot.conf```
[A report of this run](https://prover.certora.com/output/15800/2c57a7956db04b09b309fa6220dfa2d9?anonymousKey=719eaa90c86e6c73c6f2af637b5921a5b063d47a)

(*The prover calculates a difficulty score using various attributes of the functions.)

The timeout was solved and we got a counter example to the rule. If you'll look closely at the counter example you'll notice that
it seems wrong. This is because as we mentioned above, we used a NONDET summarization for the `sqrRoot` function, which is an integral part of the liquidity calculation, instead of actually calculating the square root.

What we can do, is use a smarter hand-crafted summarization. The spec `SummarizedSqrRoot.conf` contains a precise ghost summary for the function `sqrRoot`. The Certora team has proven the summarization is indeed equal to a square root operation.

To run this spec use:

```certoraRun.py runSummarizedSqrRoot.conf```
[A report of this run](https://prover.certora.com/output/15800/b91e56bd9fab47e69ab023e94b168ed3?anonymousKey=136f48b482a96179742e755d4c644e69abb1595e)

Now the rule is passing and we successfully proven the monotonicity property.


