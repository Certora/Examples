# Configuration File Inheritance Example

This folder demonstrates how to use the **`override_base_config`** feature to inherit and selectively modify Certora Prover configuration files. By defining **common** settings in a **base** config (`base.conf`), you can then:

1. **Add** new settings in a child config (`new_fields.conf`).
2. **Override** existing settings in a different child config (`override_fields.conf`).

This helps avoid duplication, simplifies maintenance, and keeps your configuration consistent.

---

## Files

1. **`MainContract.sol`**  
   An example Solidity contract (kept minimal for demonstration).
2. **`base.conf`**  
   The **base configuration** providing shared defaults:
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
   - Defines common fields like files, which contract and spec to verify, default loops, etc.
3. **`new_fields.conf`**  
   A child config **adding** an attribute that did not exist in `base.conf`:
   ```jsonc
   {
     "override_base_config": "base.conf",
     "optimistic_hashing": true
   }
   ```
   - Inherits everything from `base.conf` and adds `"optimistic_hashing": true`.
   - All original base fields remain unchanged unless redefined here.
4. **`override_fields.conf`**  
   Another child config **overriding** certain fields from `base.conf`:
   ```jsonc
   {
     "override_base_config": "base.conf",
     "loop_iter": "10",
     "optimistic_loop": false
   }
   ```
   - Changes `loop_iter` from `"3"` to `"10"`.
   - Changes `optimistic_loop` from `true` to `false`.

---

## Usage

Run the Certora Prover by pointing to either `new_fields.conf` or `override_fields.conf`, 
```bash
# Example 1: Inherit base.conf and add the 'optimistic_hashing' field
certoraRun new_fields.conf

# Example 2: Inherit base.conf but override loop_iter and optimistic_loop
certoraRun override_fields.conf
```

### What Happens Under the Hood?
- The Prover sees `"override_base_config": "base.conf"` in the child `.conf`.
- It **merges** the child’s fields with the base config:
  - **New fields** in the child (e.g. `optimistic_hashing`) are appended.
  - **Existing fields** in the child (e.g. `loop_iter`) override those in `base.conf`.
  - **Unmentioned fields** remain as specified in `base.conf`.

---

## Why Use This Feature?

- **Reduce Duplication**: Shared configuration (e.g. file lists, solver arguments) is defined once in `base.conf`.
- **Focus on Differences**: Child configs highlight only what is unique to each run, making them shorter and clearer.
- **Easier Maintenance**: Updating a common field (e.g. compiler version) means editing only the base config.
- **Flexible Overrides**: If you need different loop bounds or flags for a particular test, simply override them in a child config.
