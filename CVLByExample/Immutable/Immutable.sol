// SPDX-License-Identifier: MIT
import {Owner} from './Owner.sol';
pragma solidity >=0.8.0;
contract Immutable {
    // coding convention to uppercase constant variables
    Owner public immutable OWNER;
    uint private immutable MY_UINT;

    constructor() {
        OWNER = Owner(msg.sender);
        MY_UINT = 2;
    }

    function getMyUint() public view returns (uint) {
        return MY_UINT + 1;
    }
}