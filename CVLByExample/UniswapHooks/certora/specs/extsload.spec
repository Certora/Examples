methods {
    function PoolManagerHarness.extsload(bytes32 slot) external returns (bytes32) => NONDET DELETE;
    function PoolManagerHarness.extsload(bytes32[] slots) external returns (bytes32[] memory) => ArbBytes32(slots) DELETE;
    function PoolManagerHarness.extsload(bytes32 startSlot, uint256 nSlots) external returns (bytes32[] memory) => ArbNBytes32(startSlot, nSlots) DELETE;
    function PoolManagerHarness.exttload(bytes32 slot) external returns (bytes32) => NONDET DELETE;
    function PoolManagerHarness.exttload(bytes32[] slots) external returns (bytes32[] memory) => ArbBytes32(slots) DELETE;
}

function ArbBytes32(bytes32[] slots) returns bytes32[] {
    bytes32[] data;
    require data.length == slots.length;
    return data;
}

/// Returns an arbitrary bytes32 array of length nSlots.
function ArbNBytes32(bytes32 startSlot, uint256 nSlots) returns bytes32[] {
    bytes32[] data;
    require data.length == nSlots;
    return data;
}
