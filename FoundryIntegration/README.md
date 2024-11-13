# Foundry Fuzz Testing Integration

The Certora Prover offers seamless integration with Foundry fuzz tests, allowing for the formal verification of test cases through a simple specification file and by setting `"foundry_tests_mode": true` in the configuration file.

Unlike the standard Foundry fuzz tester, which executes tests with random inputs to discover any input combinations that cause test case failures, the Certora Prover transforms the test into a symbolic representation and applies SMT solvers to formally verify it. In essence, if a test is verified by the Prover, it is verified against all possible combinations of input values.

For further information, please refer to [Certora's Documentation](https://docs.certora.com/en/latest/docs/cvl/foundry-integration.html).

This directory contains several examples showcasing Foundry integrations, demonstrating usage as well as the Prover’s reporting format.

*Note: This feature is currently in an early alpha phase.*
