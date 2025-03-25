# ERC4626 - Full Spec

A specification file of ERC4626.

This spec can be checked against implementations of ERC4626.

We have an implementation of [Solmate](https://github.com/transmissions11/solmate) ERC4626 contract in `certora/harnesses/tokens/ERC4626AccountingHarness.sol`.

You can run this conf using
```certoraRun runERC4626Full.conf```

[Report of this run](https://prover.certora.com/output/40726/7900f52fe75f4716a69e133099c065e8/?anonymousKey=ab556122086a606ac1bf13a479268f172ec51871)

[ERC4626](certora/harnesses/tokens/ERC4626Broken.sol) is version of ERC4626 which is vulnerable to a donation attack. Instead of internal accounting, the contract uses the external asset balance of the contract. In this case some rules can be altered to take the fact that the external balance can be greater than the actual one. However still some rules are broken demonstrating a vulnerability.   