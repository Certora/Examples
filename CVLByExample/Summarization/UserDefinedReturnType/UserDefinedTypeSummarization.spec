methods {
    
    // Summarized functions from library
    function CalledLibrary.getLoc(CalledLibrary.S memory record) internal returns (CalledLibrary.E) => getOppositeLoc(record);
    // A struct return type summarization
    function CalledLibrary.toStruct(uint256 _x, bool _b, CalledLibrary.E _loc) internal returns (CalledLibrary.S memory) => getDoubledStruct(_x, _b, _loc);
    // An array return type summarization.
    function CalledLibrary.idArray(uint256 min, uint256 max) internal returns (uint256[] memory) => doubledArray(min, max);
    function callGetLoc(CalledLibrary.S record) external returns (CalledLibrary.E) envfree;
    function callToStruct(uint256 _x, bool _b, CalledLibrary.E _loc) external returns (CalledLibrary.S memory) envfree;
    function callIdArray(uint256 min, uint256 max) external returns (uint256[] memory) envfree;
}

function getOppositeLoc(CalledLibrary.S s) returns CalledLibrary.E {
    if (s.loc == CalledLibrary.E.FIRST) {
        return CalledLibrary.E.SECOND;
    }
    return CalledLibrary.E.FIRST;
}

function getDoubledStruct(uint256 _x, bool _b, CalledLibrary.E _loc) returns CalledLibrary.S {
    CalledLibrary.S out;
    require out.x == _x * 2;
    require out.b == _b;
    require out.loc == _loc;
    return out;
}

function doubledArray(uint256 min, uint256 max) returns uint256[] {
    return [0, 2];
}

rule checkLoc(CalledLibrary.S record) {
    assert callGetLoc(record) != record.loc, "enum function not summarized";
}

rule checkStructField(uint256 _x, bool _b, CalledLibrary.E _loc) {
    CalledLibrary.S newStruct = callToStruct(_x, _b, _loc);
    assert newStruct.x % 2 == 0, "Summary for struct return type function is not applied";
}

rule checkArray() {
    uint256 min;
    uint256 max;
    require max > min;
    uint256[] arr = callIdArray(min, max);
    assert arr.length > 0, "Summary for array return type function is not applied";
}
