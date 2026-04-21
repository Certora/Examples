# Links Block Example

## Overview

The `links { }` block is a CVL feature for declaring contract linking directly in the spec file, replacing the `link` and `struct_link` conf flags. Linking tells the Prover which concrete contract an address field points to, enabling precise verification of multi-contract interactions.

With the `links { }` block, linking declarations live alongside the rules that depend on them, and support advanced features like struct field linking, array/mapping indexing, wildcards, and multi-target dispatch.

## Syntax Quick Reference

| Pattern | Description |
| ------- | ----------- |
| `main.field => target` | Scalar or immutable field |
| `main.holder.token => target` | Struct field (dot notation) |
| `main.arr[0] => target` | Array element (concrete index) |
| `main.arr[_] => target` | Wildcard (all indices) |
| `main.arr[0] => targetA; main.arr[_] => targetB` | Concrete precedence (index 0 -> targetA, rest -> targetB) |
| `main.field => [targetA, targetB]` | Multi-target dispatch |
| `main.map[0] => target` | Mapping (concrete key) |
| `main.map[_] => target` | Mapping (wildcard key) |
| `main.map[to_bytes4(0x1234)] => target` | Typed key cast |
| `main.map[contractAlias] => target` | Contract alias as key |
| `main.map[0][0] => target` | Nested mapping/array |
| `main.arr[_].field => target` | Struct field in array |

## Examples

### 1. BasicLinking — Scalar, immutable, struct, static array

Demonstrates the most common linking patterns using the new `links { }` syntax.

**Command:**
```bash
certoraRun BasicLinking.conf
```

### 2. ConfStyleLinking — Comparison with old `link` conf flag

Same contract, but linking is done via the `link` conf flag. Only scalar and immutable fields can be linked this way — precise struct fields and arrays require the `links { }` block. This way of linking is not recommended for new specifications, linking via CVL should be used as default.
**Command:**
```bash
certoraRun ConfStyleLinking.conf
```

### 3. AdvancedLinking — Wildcards, multi-target, mappings, nesting

Demonstrates advanced capabilities:
- **Multi-target dispatch**: `field => [tokenA, tokenB]` — the Prover considers both targets
- **Wildcard arrays**: `arr[_] => target` — all indices resolve to the target
- **Wildcard precedence**: concrete entries override wildcards at the same path
- **Address-keyed mappings**: contract aliases used as mapping keys
- **bytes4-keyed mappings**: `to_bytes4(...)` casts as keys
- **Nested mappings**: `map[i][j] => target`
- **Struct arrays**: `arr[_].field => target`

**Command:**
```bash
certoraRun AdvancedLinking.conf
```

## Important Notes

- The `links { }` block and `link`/`struct_link` conf flags are **mutually exclusive** per verification run. You cannot use both in the same conf.
- For dynamic arrays with concrete element links, the compiler adds an assumption of the form `assume arr.length <= index || contract.arr[index] == target` for each linked index.
- When both concrete and wildcard entries exist at the same path, concrete entries take precedence.
- Wildcard indices cannot be mixed with concrete indices in the same entry (e.g., `arr[0][_]` is not allowed — use all concrete or all wildcards).
