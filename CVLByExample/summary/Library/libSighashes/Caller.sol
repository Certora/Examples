// SPDX-License-Identifier: agpl-3.0
pragma solidity >=0.8.10;

library CalledLibrary {
    struct S {
        int64 x;
        bool b;
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
}
