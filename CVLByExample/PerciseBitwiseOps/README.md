# Precise Bitwise Ops Example

## Overview
This repository contains a smart contract named `PreciseBitwiseOps`. It showcases two essential functions: `setBorrowing` and `isBorrowing`. The highlight of this example lies in demonstrating reasoning precisely about bitwise operation. By default, the Prover overapproximate bitwise operations applied in a non-standard way (xor, or, and non 2^n-1 masks for better running time. This feature can be activated either by passing the `--precise_bitwise_ops` flag during execution or by permanently setting it in the configuration file as `"precise_bitwise_ops": true`. By enabling this feature, the modeling of intricate bitwise operations becomes precise, thus preventing any misleading counter-examples.

## Usage

To utilize the `precise_bitwise_ops` feature, follow these steps:

1. Pass `--precise_bitwise_ops` as an argument during execution.
2. Alternatively, add `"precise_bitwise_ops": true` to the configuration file.

## Execution Steps

1. **Non-Precise Execution**
    - Command:
        ```bash
        certoraRun BrokenPreciseBitwiseOps.conf
        ```
    - Execution Output: [Certora Run Output](https://vaas-stg.certora.com/output/1512/328196fea5c948b980d91f0fe49667f6?anonymousKey=8bdc0c128fb64319a6b5942f09f418d7af10ccff)

**Results Analysis**
The analysis conducted indicates a violation in the `setBorrowing` rule. However, upon closer inspection, it becomes evident that the bitwise calculations lack precision.

2. **Precise Execution**
    - Command:
        ```bash
        certoraRun PreciseBitwiseOps.conf
        ```
    - Execution Output: [Certora Run Output](https://vaas-stg.certora.com/output/1512/a96ee5bb38e14eef85784dd9f89f03d4?anonymousKey=a4670ac866dcc11933fb27ee28f53055d0c3c58c)

**Results Analysis**
Upon executing with precise bitwise calculations, the analysis confirms the `setBorrowing` rule verified as expected, highlighting the effectiveness of the precise approach.