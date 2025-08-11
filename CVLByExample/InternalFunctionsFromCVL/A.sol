// SPDX-License-Identifier: MIT
contract A {
    struct S {
        int i;
    }

    S s;

    function anInternalFunction() internal returns (uint) { return 0; }
    function summarizedInternal() internal returns (uint) { return 0; }

    function internalFunctionWithStorageInput(S storage _s) internal { s = _s; }
    function internalFunctionWithStorageOutput() internal returns (S storage) { return s; }
}
