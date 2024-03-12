// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity >=0.8.0;

import "./B.sol";

contract A {

    B public other;

    function callAFunc() external returns (uint256) {
        return other.toBeSummarized();
    }
}
