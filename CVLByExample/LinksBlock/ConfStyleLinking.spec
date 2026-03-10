/// Conf-style linking example: same contract, but linking is done via the
/// `--link` conf flag instead of a `links { }` block.
///
/// Note: The `--link` conf flag can only link scalar and immutable fields.
/// Struct fields (like holder.token) and array elements require either
/// `--struct_link` or the new `links { }` block.

using BasicVault as vault;
using TokenA as tokenA;
using TokenB as tokenB;

methods {
    function getPrimaryValue() external returns (uint) envfree;
    function getImmutableValue() external returns (uint) envfree;
}

/// Scalar field: primaryToken is linked to TokenA (value 1) via conf --link
rule scalarLinked {
    assert getPrimaryValue() == 1;
    assert vault.primaryToken == tokenA;
}

/// Immutable field: immutableToken is linked to TokenB (value 2) via conf --link
rule immutableLinked {
    assert getImmutableValue() == 2;
    assert vault.immutableToken == tokenB;
}
