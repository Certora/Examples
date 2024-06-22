// SPDX-License-Identifier: LGPL-3.0-only
pragma solidity >=0.8.0;

contract ProxySimulator {
    function callAddition(address proxy, uint32 methodsig, uint256 x, uint256 y) external view returns (uint256) {
        (bool success, bytes memory data) = proxy.staticcall(abi.encodePacked(methodsig, x, y));
        
        require(success);

        return abi.decode(data, (uint256));
    }
}