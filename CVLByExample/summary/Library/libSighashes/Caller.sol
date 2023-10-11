// SPDX-License-Identifier: agpl-3.0
pragma solidity >=0.8.10;

library CalledLibrary {
    struct S {
        uint256 x;
        bool b;
        E loc;
    }

    enum E {
        FIRST,
        SECOND
    }

    function funcWithStruct(CalledLibrary.S memory s) external view returns (uint) {
        return 0;
    }
    function funcWithEnum(CalledLibrary.E e) external view returns (uint) {
        return 0;
    }
    function funcWithStorage(uint[] storage s) external view returns (uint) {
        return 0;
    }

    function getLoc(CalledLibrary.S memory record) internal returns (CalledLibrary.E) {
        return record.loc;
    }

    function toStruct(uint256 _x, bool _b, E _loc) internal returns (CalledLibrary.S memory out) {
        return S(_x, _b, _loc);
    }

    function idArray(uint256 min, uint256 max) internal returns (uint256[] memory out) {
        for (uint256 i = 0; i < max; i++) {
            out[i] = i;
        }
    }
}

contract Caller {
    uint[] uarr;

    function funcWithStruct(CalledLibrary.S memory s) external view returns (uint) {
        return 0;
    }

    function funcWithEnum(CalledLibrary.E e) external view returns (uint) {
        return 0;
    }

    function funcWithStorage(uint[] memory s) external view returns (uint) {
        return 0;
    }

    function callLibFuncWithStruct(CalledLibrary.S memory s) external view returns (uint) {
        return CalledLibrary.funcWithStruct(s);
    }
    function callContractFuncWithStruct(CalledLibrary.S memory s) external view returns (uint) {
        return this.funcWithStruct(s);
    }

    function callLibFuncWithEnum(CalledLibrary.E e) external view returns (uint) {
        return CalledLibrary.funcWithEnum(e);
    }
    function callContractFuncWithEnum(CalledLibrary.E e) external view returns (uint) {
        return this.funcWithEnum(e);
    }

    function callLibFuncWithStorage() external view returns (uint) {
        return CalledLibrary.funcWithStorage(uarr);
    }
    function callContractFuncWithStorage() external view returns (uint) {
        return this.funcWithStorage(uarr);
    }

    function callGetLoc(CalledLibrary.S memory record) external returns (CalledLibrary.E) {
        return CalledLibrary.getLoc(record);
    }

    function callToStruct(uint256 _x, bool _b, CalledLibrary.E _loc) external returns (CalledLibrary.S memory) {
        return CalledLibrary.toStruct(_x, _b, _loc);
    }

    function callIdArray(uint256 min, uint256 max) external returns (uint256[] memory out) {
        return CalledLibrary.idArray(min, max);
    }
}
