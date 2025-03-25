// SPDX-License-Identifier: AGPL-3.0-or-later
pragma solidity ^0.8.21;

import { Caller } from "Caller.sol";
import { Target } from "Target.sol";


/// @title Main contract for example
contract Main {
    address target;
    Caller caller;
    address public other;

    function main(uint256 x, bool useInternal, address callTarget) external returns (uint256) {
        if (callTarget == address(0)) {
            callTarget = target;
        }

        bytes memory data;
        if (useInternal) {
            data = doCallInternal(
                callTarget,
                abi.encodeCall(Target.calculate, (x))
            );
        } else {
            data = caller.doCall(
                callTarget,
                abi.encodeCall(Target.calculate, (x))
            );
        }
        uint256 result = abi.decode(data, (uint256));
        return result;
    }
    
    function doCallInternal(
        address callTarget,
        bytes memory data
    ) internal returns (bytes memory) {
        (bool success, bytes memory result) = callTarget.call(data);
        require(success);
        return result;
    }

    function catchCall(uint256 x) external returns (uint256) {
        return Target(other).calculate(x);
    }
}
