// SPDX-License-Identifier: AGPL-3.0-or-later
pragma solidity ^0.8.21;

/// @title Intermediate contract that makes low level calls
contract Caller {
    function doCall(
        address target,
        bytes memory data
    ) external returns (bytes memory) {
        (bool success, bytes memory result) = target.call(data);
        require(success);
        return result;
    }
}
