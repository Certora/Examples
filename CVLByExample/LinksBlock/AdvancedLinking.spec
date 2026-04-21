/// Advanced `links { }` block example: wildcards, multi-target dispatch,
/// mappings, nested containers, and struct arrays.
///
/// Demonstrates capabilities that go beyond what the `--link` conf flag can do.

using AdvancedRegistry as registry;
using TokenA as tokenA;
using TokenB as tokenB;
using TokenC as tokenC;
using TokenD as tokenD;

links {
    // Multi-target dispatch: the address resolves to one of the listed contracts
    registry.multiTarget => [tokenA, tokenB];

    // Wildcard dynamic array: all elements resolve to tokenA or tokenB
    registry.dynamicTokens[_] => [tokenA, tokenB];

    // Mapping with concrete key + wildcard precedence:
    // Key 0 always resolves to tokenA; all other keys resolve to tokenB
    registry.tokenMap[0] => tokenA;
    registry.tokenMap[_] => tokenB;

    // Address-keyed mapping: contract alias used as the key
    registry.addrMap[tokenA] => tokenC;
    registry.addrMap[tokenB] => tokenD;

    // Wildcard + concrete precedence on array:
    // Index 0 is always tokenC; all other indices are tokenA
    registry.precedenceTokens[0] => tokenC;
    registry.precedenceTokens[_] => tokenA;

    // bytes4-keyed mapping: to_bytes4(...) cast as the key
    registry.bytes4Map[to_bytes4(0x12345678)] => tokenA;
    registry.bytes4Map[to_bytes4(0xdeadbeef)] => tokenB;

    // Nested mapping: two-level indexing
    registry.mapMap[0][0] => tokenC;
    registry.mapMap[_][_] => [tokenA, tokenD];

    // Struct in array: wildcard access to a struct field
    registry.holderArray[_].token => [tokenA, tokenC];
}

methods {
    function getMultiTargetValue() external returns (uint) envfree;
    function getDynamicTokenValue(uint) external returns (uint) envfree;
    function dynamicTokensLength() external returns (uint) envfree;
    function getTokenMapValue(uint) external returns (uint) envfree;
    function getAddrMapValue(address) external returns (uint) envfree;
    function getPrecedenceValue(uint) external returns (uint) envfree;
    function precedenceTokensLength() external returns (uint) envfree;
    function getBytes4MapValue(bytes4) external returns (uint) envfree;
    function getMapMapValue(uint, uint) external returns (uint) envfree;
    function getHolderArrayValue(uint) external returns (uint) envfree;
    function holderArrayLength() external returns (uint) envfree;
}

/// Multi-target: value must be TokenA (1) or TokenB (2)
rule multiTargetDispatch {
    uint val = getMultiTargetValue();
    assert val == 1 || val == 2;
    assert registry.multiTarget == tokenA || registry.multiTarget == tokenB;
}

/// Wildcard dynamic array: every element is TokenA or TokenB
rule wildcardDynamicArray {
    uint i;
    require dynamicTokensLength() > i;
    uint val = getDynamicTokenValue(i);
    assert val == 1 || val == 2;
    assert registry.dynamicTokens[i] == tokenA || registry.dynamicTokens[i] == tokenB;
}

/// Mapping with wildcard precedence: key 0 -> TokenA (1), all others -> TokenB (2)
rule mappingWithPrecedence {
    // Concrete key takes priority
    assert getTokenMapValue(0) == 1;
    assert registry.tokenMap[0] == tokenA;

    // Wildcard applies to all other keys
    uint key;
    require key != 0;
    assert getTokenMapValue(key) == 2;
    assert registry.tokenMap[key] == tokenB;
}

/// Address-keyed mapping: contract aliases as keys
rule addressKeyedMapping {
    assert getAddrMapValue(tokenA) == 3;  // tokenA -> tokenC (value 3)
    assert getAddrMapValue(tokenB) == 4;  // tokenB -> tokenD (value 4)
    assert registry.addrMap[tokenA] == tokenC;
    assert registry.addrMap[tokenB] == tokenD;
}

/// Wildcard + concrete precedence on array:
/// Index 0 is tokenC (3), all others are tokenA (1)
rule arrayPrecedence {
    require precedenceTokensLength() >= 2;

    assert getPrecedenceValue(0) == 3;
    assert registry.precedenceTokens[0] == tokenC;

    assert getPrecedenceValue(1) == 1;
    assert registry.precedenceTokens[1] == tokenA;
}

/// bytes4-keyed mapping: to_bytes4 casts as keys
rule bytes4Mapping {
    assert getBytes4MapValue(to_bytes4(0x12345678)) == 1;  // tokenA
    assert getBytes4MapValue(to_bytes4(0xdeadbeef)) == 2;  // tokenB
    assert registry.bytes4Map[to_bytes4(0x12345678)] == tokenA;
    assert registry.bytes4Map[to_bytes4(0xdeadbeef)] == tokenB;
}

/// Nested mapping: concrete [0][0] -> tokenC (3),
/// wildcard [_][_] -> tokenA (1) or tokenD (4)
rule nestedMapping {
    // Concrete entry
    assert getMapMapValue(0, 0) == 3;

    // Wildcard entries
    uint i; uint j;
    require i != 0 || j != 0;
    uint val = getMapMapValue(i, j);
    assert val == 1 || val == 4;
}

/// Struct in array: wildcard links holderArray[_].token to tokenA or tokenC
rule structInArray {
    uint i;
    require holderArrayLength() > i;
    uint val = getHolderArrayValue(i);
    assert val == 1 || val == 3;
    assert registry.holderArray[i].token == tokenA || registry.holderArray[i].token == tokenC;
}
