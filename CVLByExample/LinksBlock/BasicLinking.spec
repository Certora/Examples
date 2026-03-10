/// Basic `links { }` block example: scalar, immutable, struct, and static array linking.
///
/// This spec demonstrates the new spec-based linking syntax, replacing the
/// `--link` and `--struct_link` conf flags. All linking is declared in the spec
/// alongside the rules that depend on it.

using BasicVault as vault;
using TokenA as tokenA;
using TokenB as tokenB;
using TokenC as tokenC;

links {
    vault.primaryToken => tokenA;       // scalar field
    vault.immutableToken => tokenB;     // immutable field
    vault.holder.token => tokenC;       // struct field (not possible with --link conf flag)
    vault.fixedTokens[0] => tokenA;    // static array element
    vault.fixedTokens[1] => tokenB;
}

methods {
    function getPrimaryValue() external returns (uint) envfree;
    function getImmutableValue() external returns (uint) envfree;
    function getHolderValue() external returns (uint) envfree;
    function getFixedTokenValue(uint) external returns (uint) envfree;
}

/// Scalar field: primaryToken is linked to TokenA (value 1)
rule scalarLinked {
    assert getPrimaryValue() == 1;
    assert vault.primaryToken == tokenA;
}

/// Immutable field: immutableToken is linked to TokenB (value 2)
rule immutableLinked {
    assert getImmutableValue() == 2;
    assert vault.immutableToken == tokenB;
}

/// Struct field: holder.token is linked to TokenC (value 3)
rule structFieldLinked {
    assert getHolderValue() == 3;
    assert vault.holder.token == tokenC;
}

/// Static array: fixedTokens[0] = TokenA (1), fixedTokens[1] = TokenB (2)
rule staticArrayLinked {
    assert getFixedTokenValue(0) == 1;
    assert getFixedTokenValue(1) == 2;
    assert vault.fixedTokens[0] == tokenA;
    assert vault.fixedTokens[1] == tokenB;
}
