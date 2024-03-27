// SPDX-License-Identifier: MIT
import {Owner} from './Owner.sol';
pragma solidity >=0.8.0;
contract PrivateImmutable {
    // coding convention to uppercase constant variables
    Owner private immutable OWNER;
    uint public immutable MY_UINT;

    constructor() {
        OWNER = Owner(msg.sender);
        MY_UINT = 2;
    }

    function getMyUint() public view returns (uint) {
        return MY_UINT + 1;
    }

    function getOwner() public view returns (Owner) {
        return OWNER;
    }
}