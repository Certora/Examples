# Ercecover Example

## Overview
This repository contains a smart contract named `Verify` that implements a signature verification mechanism using the `ecrecover` function. The contract includes a function `executeMyFunctionFromSignature` that allows a user to execute a specific function if the provided signature is valid. The example demonstrates new CVL feature which is cvl function version of the same ercecover function implemented in CVL.

## Executions

1. **Certora Run for ecrecover**
    - Command:
        ```bash
        certoraRun Fullecrecover.conf --server production --prover_version master
        ```
    - Execution Link: [Certora Run Output](https://prover.certora.com/output/1512/01ce19bfd3fa4a3b98e216bf2c085c24?anonymousKey=f85d1e9348a4e5f8293700660f90f41eb96aa83e)

2. **Certora Mutate**
    - Command:
        ```bash
        certoraMutate --mutation_conf mutation.mconf --prover_conf Fullecrecover.conf --server production
        ```
    - Mutation Link: [Certora Mutate Output](https://mutation-testing.certora.com/?id=71f2ffd2-80ea-47b5-b3b9-29cc73c91752&anonymousKey=d3f0379a-9a60-4b34-9edb-7210e763a91e)

The mutation execution contains 2 manual injection bugs locating under ManualMutation folder.

## Smart Contract

The smart contract, `Verify`, provides a method `isSigned` for signature verification and `executeMyFunctionFromSignature` for executing a function based on a valid signature. It also includes a method `getHash` for generating a hash used in the signature process.

The contract follows the EIP-712 standard for domain separation and signature verification. The functions implement checks for signature uniqueness, zero value, determinism, and dependencies on `r` and `s`.

## Certora Verification Language (CVL) Properties

### ecrecover Properties

1. **Zero Value**
   - `ecrecover(0, v, r, s) == 0`

2. **Deterministic**
   - `ecrecover(msgHash, v, r, s) == _addr` on different calls

3. **Uniqueness of Signature**
   - `ecrecover(msgHash, v, r, s) != 0 => ecrecover(msgHash', v, r, s) == 0` where `msgHash' != msgHash`

4. **Dependency on r and s**
   - `ecrecover(msgHash, v, r, s) != 0 => ecrecover(msgHash, v, r', s) == 0` where `r' != r`
   - `ecrecover(msgHash, v, r, s) != 0 => ecrecover(msgHash, v, r, s') == 0` where `s' != s`

### High-Level Properties

1. **Single Verifier**
   - A single address can verify a signature, and different addresses cannot verify the same signature.

2. **Owner Signature Uniqueness**
   - For a given address, two different messages cannot have the same valid signature.

3. **Hash Uniqueness**
   - Two different sets of parameters result in unique hash values.

4. **Only Single User Can Execute**
   - Only a single user, specified by the address, can successfully execute a function.

5. **Signed Params and Deadline**
   - The parameters and deadlines signed by the same address are the same.

6. **Two Different Signatures**
   - Two different messages signed by the same address have different signatures.

7. **Signed Messages Executed Once**
   - Once a message is executed, it cannot be executed again.


For a comprehensive guide on Certora Verification Language, refer to [Certora Documentation](https://docs.certora.com).