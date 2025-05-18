# Configuration File Inheritance Example

This folder demonstrates how to use the **`override_base_config`** feature to inherit and selectively modify Certora Prover configuration files. By defining **common** settings in a **base** config (`base.conf`) and referencing it from different child configs, you can avoid duplication and streamline maintenance.

---

## Files

1. **`MainContract.sol`**  
   A minimal Solidity contract to be verified.

2. **`base.conf`**  
   **Base** configuration with shared defaults:
   ```jsonc
   {
     "files": ["MainContract.sol"],
     "verify": "MainContract:MainContract.spec",
     "msg": "Main contract",
     "optimistic_loop": true,
     "loop_iter": "3",
     "rule_sanity": "basic"
   }
   ```
   - Defines the source files, contract–spec pairing, default loop settings, etc.

3. **`new_fields.conf`**  
   Child config **adding** a new field (`optimistic_hashing`) not present in `base.conf`:
   ```jsonc
   {
     "override_base_config": "base.conf",
     "optimistic_hashing": true
   }
   ```

4. **`override_fields.conf`**  
   Child config **overriding** certain fields from `base.conf`:
   ```jsonc
   {
     "override_base_config": "base.conf",
     "loop_iter": "10",
     "optimistic_loop": false
   }
   ```

5. **`invalid_base.conf`**  
   A config that **incorrectly** attempts to act as a base while also referencing **another** base:
   ```jsonc
   {
     "files": ["MainContract.sol"],
     "verify": "MainContract:MainContract.spec",
     "msg": "Main contract",
     "optimistic_loop": true,
     "loop_iter": "3",
     "rule_sanity": "basic",
     "override_base_config": "base.conf"
   }
   ```
   - **This is invalid** because a base config must **not** itself contain `override_base_config`.
   - The feature currently supports **only one** level of inheritance (no nested base configs).

---

## Usage Examples

### Merging **`base.conf`** + **`new_fields.conf`**
```bash
certoraRun new_fields.conf
```
- Inherits `base.conf` and **adds** `"optimistic_hashing": true`.

### Merging **`base.conf`** + **`override_fields.conf`**
```bash
certoraRun override_fields.conf
```
- Changes `loop_iter` from `"3"` to `"10"` and sets `optimistic_loop` to `false`.

---

## Invalid Base Example
### Attempting to Use **`invalid_base.conf`**
```bash
certoraRun invalid_base.conf
```
Error:
```
certoraRun invalid_base.conf

Cannot load base config: override_fields.conf
base config cannot include 'override_base_config'

Error when reading invalid_base.conf: Cannot load base config: override_fields.conf
base config cannot include 'override_base_config'
```

- **`invalid_base.conf`** tries to reference `override_fields.conf` as a base config.
- **This is disallowed** because the feature only supports **single-level inheritance**: a base config **cannot** itself specify an `override_base_config` field.

---

## Why Use `override_base_config`?

1. **Reduce Duplication**  
   Common fields (e.g., file lists, compiler version, environment arguments) live in **one** place.

2. **Clear Overrides**  
   Child configs only show what differs from the parent.

3. **Easier Maintenance**  
   Updating a shared parameter (e.g., loop iterations) means editing just one file.
