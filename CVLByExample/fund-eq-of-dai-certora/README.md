# fund-eq-of-dai-certora

The contract `Vat` represents an intermediate product during preparation for deployment of
`Multi Collateral DAI` on other domains. See https://github.com/makerdao/xdomain-dss.
A detailed blog on the contract and the found bug can be found in https://hackmd.io/@SaferMaker/DAICertoraSurprise

## Instructions for Checking the Vat Contract
1. Install [Certora CLI](https://certora.atlassian.net/wiki/spaces/CPD/pages/7274497/Installation+of+Certora+Prover)
2. Install [solc-select](https://pypi.org/project/solc-select/)
3. Use solc-select to install solc 0.8.13 via `solc-select install 0.8.13`
4. Clone this repository via `git clone https://github.com/kmbarry1/fund-eq-of-dai-certora.git`

## Incorrect Code
The invariant `fundamental_equation_of_dai` fails because 
the function `Vat.init(ilk)` is called when `Vat.ils[ilk].Rate` is zero as required , yet Vat.ilks[ilk].Art is non-zero.
The `Vat.fold` function can set a `rate` back to zero after the associated `Art` becomes non-zero, allowing `init` to be called on an `ilk`` that has already been activated.

Run via ```certoraRun certora/conf/runVat.conf```

## Correct Code
To fix the above bug we strenghtened the `require` in `init` to require that also `Vat.ilks[ilk].Art` is zero.


Run the correct version via ```certoraRun certora/conf/runVatFixed.conf```





