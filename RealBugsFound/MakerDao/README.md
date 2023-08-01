# fund-eq-of-dai-certora

The contract `Vat` represents an intermediate product during preparation for deployment of
`Multi Collateral DAI` on other domains. You can view the link on  https://github.com/makerdao/xdomain-dss.
A detailed blog on the contract and the found bug can be found in [DAI bug](https://hackmd.io/@SaferMaker/)DAICertoraSurprise

## Incorrect Code
The invariant `fundamental_equation_of_dai` fails because the function `Vat.init(ilk)` is called when `Vat.ils[ilk].Rate` is zero as required , yet Vat.ilks[ilk].Art is non-zero.
The `Vat.fold` function can set a `rate` back to zero after the associated `Art` becomes non-zero, allowing `init` to be called on an `ilk`` that has already been activated.

Run via ```certoraRun certora/conf/runVat.conf```

[The report of this run](https://prover.certora.com/output/1902/da91d0e3e7bf48308bbfc84782923107?anonymousKey=ac4fa747f326964bb63085fc47a0fafbe8352709)

## Correct Code
To fix the bug above we strengthened the `require` in `init` to require that also `Vat.ilks[ilk].Art` is zero.

Run the correct version via ```certoraRun certora/conf/runVatFixed.conf```

[The report of this run](https://prover.certora.com/output/1902/941036dc6ccd4450a08e4390991d0d69?anonymousKey=f30b296a2da9484a9c4f44be1707fb1c33cd25bf)






