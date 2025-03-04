# Soroban Hello World Contract Example

This example demonstrates how to use Certora's Prover with a Soroban smart contract. It includes configurations for both the old and new formats to showcase their differences and execution.

---

## Overview

This project includes:
- A Soroban Hello World contract written in Rust.
- Configurations for running the Certora Prover with old and new formats.
- A `certora_build.py` script for compiling and preparing the project for verification.

---

## Contract Details

The contract is located in `lib.rs` and implements a simple `hello` function, which is used to demonstrate the Certora Prover's capabilities.

---

## Configuration Formats

### Old Format
The old format configuration (`hello_world_old_format.conf`) explicitly specifies the `files` field, pointing to the compiled WebAssembly (`.wasm`) file:

```json
{
    "files": [
        "soroban_hello_world_contract.wasm"
    ],
    "process": "emv",
    "optimistic_loop": true,
    "rule": "hello"
}
```

### New Format
The new format configuration (`hello_world_new_fromat.conf`) leverages a `build_script` for dynamic building and eliminates the need for hardcoded file paths:

```json
{
    "build_script": "./certora_build.py",
    "process": "emv",
    "optimistic_loop": true,
    "rule": "hello"
}
```

**Key Difference:**
- **Old Format:** Requires manual compilation and specification of the `.wasm` file.
- **New Format:** Automatically builds the project using the specified build script.

---

## Execution Examples

### Running with the New Format
```bash
certoraRun hello_world_new_fromat.conf
```

**Expected Output:**
```
INFO: Building from script ./certora_build.py
WARNING: certora-cli-alpha-master

Connecting to server...

Job submitted to server

Manage your jobs at https://vaas-stg.certora.com
Follow your job and see verification results at https://vaas-stg.certora.com/output/1512/c3effd5d69924d4ab6e5279c5615a9b6?anonymousKey=f9184e62e3c12c47df11f2a16c68fc08acc5c07e
```

### Running with the Old Format
```bash
certoraRun hello_world_old_format.conf

**Expected Output:**
```
WARNING: Note: attribute files value in CLI (hello_world_old_format.conf) overrides value stored in conf file (soroban_hello_world_contract.wasm)
WARNING: certora-cli-alpha-master

Connecting to server...

Job submitted to server

Manage your jobs at https://vaas-stg.certora.com
Follow your job and see verification results at https://vaas-stg.certora.com/output/1512/4be870495a214f2c955d02268219dd90?anonymousKey=a9907295b95f8c82bd0321fcc070cb894f9499d8
```

---

## Building the Project

The `certora_build.py` script compiles the contract and prepares it for verification:
```bash
python3 certora_build.py
```

This ensures the `soroban_hello_world_contract.wasm` file is up-to-date and properly configured.
And must be used when running the old format configuration but is not required for the new format.

---

## Build Script: Inputs and Outputs
The build script serves as a bridge between the project and the Certora Prover, handling compilation and providing necessary metadata. It must:
1. Compile the project
2. Return a JSON object with project details
3. Handle build failures appropriately

### Inputs
- `-o/--output`: Specifies output JSON file path
- `--json`: Dumps JSON to console
- `-l/--log`: Shows build logs
- `-v/--verbose`: Enables verbose mode

### Outputs
## Case using --json

Print to stdout JSON structure containing:
```json
{
    "project_directory": "<path>",
    "sources": ["src/**/*.rs", "Cargo.toml"],
    "executables": "target/.../contract.wasm",
    "success": true/false,
    "return_code": 0/or non-zero,
    "log": {
        "stdout": "path/to/stdout",
        "stderr": "path/to/stderr"
    }
}
```
## Case using --output
Save JSON structure to file specified by `--output` flag.

## Case not using --json or --output
return 0 if build was successful, 1 otherwise.
Note: This case is mandatory for the build script to work properly in Mutation Testing.
