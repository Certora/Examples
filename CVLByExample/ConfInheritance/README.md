# Inheriting Configurations with `override_base_config`

## Overview

This folder demonstrates the **new `override_base_config`** feature in Certora’s configuration files. By defining shared verification settings in a **base** config (`parent.conf`) and referencing it from a **child** config (`run.conf`), we can easily **inherit** and **override** only what we need.

### Files

1. **`MainContract.sol`**  
   A simple contract showcasing a bidding function (`bid()`) with specific requirements related to native balances.

2. **`MainSpec.spec`**  
   A spec file with rules verifying how the contract’s native balance changes under different conditions.

3. **`parent.conf`** (Base Config)  
   Contains common verification parameters:
   - Files to verify (e.g., `MainContract.sol`)  
   - The contract-to-spec pairing (`"verify": "MainContract:MainContract.spec"`)  
   - Default settings like `"optimistic_loop": true` and `"loop_iter": "3"`

4. **`run.conf`** (Child Config)  
   References **`parent.conf`** using `override_base_config: "parent.conf"` and selectively overrides some fields:
   - `"optimistic_loop"`: set to `false`
   - `"loop_iter"`: changed to `"10"`

---

## How It Works

1. **Base Config (`parent.conf`)**  
   Lists the default settings, such as files, the main spec to verify, and global parameters like loop unrolling.

2. **Child Config (`run.conf`)**  
   Declares:
   ```jsonc
   {
     "override_base_config": "parent.conf",
     "optimistic_loop": false,
     "loop_iter": "10"
   }
   ```
   This means the **Prover** merges these overrides with whatever is in `parent.conf`.

3. **Result**  
   - All unspecified attributes in `run.conf` default to those from `parent.conf`.
   - Specified attributes in `run.conf` **override** the parent’s.

---

## Running the Example

Use the `certoraRun` command to reference `run.conf` and explicitly override the base config:

```bash
certoraRun run.conf
```

- The **resulting** configuration is a combination of **`parent.conf`** plus the **overrides** in **`run.conf`**.

---

## Why This Matters

- **Reduced Duplication**: Shared settings (e.g., file names, solver arguments, general flags) go in a single base file, so you don’t repeat them in every `.conf`.
- **Easier Maintenance**: To update a common parameter (e.g., solidity version, environment setup), change it in one place.
- **Selective Overriding**: If you need to tweak certain fields for a particular run (like a different loop bound or turning off `optimistic_loop`), you can do so easily.
