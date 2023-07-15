We use two harnesses:

- AaveTokenV3Harness adds a few simple getters to the original AaveTokenV3 code

- AaveTokenV3HarnessStorage is used to verify general.spec. It changes delegationState field in _balances
to be uint8 instead of DelegationState enum. The harness files are produced by running `make munged` which
patches the original code with `applyHarness.patch` patch.
