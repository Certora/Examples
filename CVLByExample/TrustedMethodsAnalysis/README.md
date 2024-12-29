# Trusted Method Analysis

This feature checks for external calls and checks the calls against an allow lists by specifying a new built in parametric rule: `use builtin rule trustedMethods`.

The rule succeeds if all external calls are fully resolved (i.e. sighash and target) and are on the defined trusted methods list. Otherwise the analysis reports violated for this method. This entails that the rule fails as soon as there is any call that is unresolved due to a missing target or a missing unresolved sighash, for instance as the deployed contract requires linking.

The allow list must be set via `"prover_resource_files": ["trustedMethods:ExampleTrustedMethods.json"]` in the config file.

**How to specify custom trusted methods**

You can use a different set of trusted methods by specifying your own `trustedMethod.json` file in the following format:
```
{
    "0xe0f5206bbd039e7b0592d8918820024e2a7437b9": ["0x4c6c6213","0x8f6462c3",...],
    "0xe918820024e2a7437b90f5206bbd039e7b0592d8": ["0x62134c6c","0x2c38f646",...]
}
```
And the adding `"prover_resource_files": ["trustedMethods:trustedMethod.json"]` to the config file.

It's also possible to define a wildcard for the contract address or for the method sighash by using "_".