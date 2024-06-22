// SPDX-License-Identifier: LGPL-3.0-only
pragma solidity >=0.8.0;

contract Proxy {
    address internal _implementation;
    constructor(address implementation) {
        _implementation = implementation;
    }

    fallback() external {
        // This code is for "illustration" purposes. To implement this functionality in production it
        // is recommended to use the `Proxy` contract from the `@openzeppelin/contracts` library.
        // https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.2/contracts/proxy/Proxy.sol
        
        address implementation = _implementation;
        assembly {
            // (1) copy incoming call data
            calldatacopy(0, 0, calldatasize())

            // (2) forward call to logic contract
            let result := delegatecall(gas(), implementation, 0, calldatasize(), 0, 0)

            // (3) retrieve return data
            returndatacopy(0, 0, returndatasize())

            // (4) forward return data back to caller
            switch result
            case 0 {
                revert(0, returndatasize())
            }
            default {
                return(0, returndatasize())
            }
        }
    }
}