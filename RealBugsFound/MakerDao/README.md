# fund-eq-of-dai-certora

The contract `Vat` represents an intermediate product during preparation for deployment of
`Multi Collateral DAI` on other domains. You can view the link on  https://github.com/makerdao/xdomain-dss.
A detailed blog on the contract and the found bug can be found in [DAI bug](https://hackmd.io/@SaferMaker/)DAICertoraSurprise

## Incorrect Code
The invariant `fundamental_equation_of_dai` fails because the function `Vat.init(ilk)` is called when `Vat.ils[ilk].Rate` is zero as required , yet Vat.ilks[ilk].Art is non-zero.
The `Vat.fold` function can set a `rate` back to zero after the associated `Art` becomes non-zero, allowing `init` to be called on an `ilk`` that has already been activated.

Run via ```certoraRun runVat.conf```

[The report of this run](https://prover.certora.com/output/15800/a4fd351f2b4e4568a29a4ab7b0732f42?anonymousKey=1c6f501bb2fbadc8db8b9f0341b4b7f784ecce14)

## Correct Code
To fix the bug above we strengthened the `require` in `init` to require that also `Vat.ilks[ilk].Art` is zero.

Run the correct version via ```certoraRun runVatFixed.conf```

[The report of this run](https://prover.certora.com/output/15800/bf7e3a51a0694a37af100f4295f5b946?anonymousKey=a1ca390af5fbce537e867fbce33be5952f9593ff)






