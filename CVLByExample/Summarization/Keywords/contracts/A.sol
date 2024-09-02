// SPDX-License-Identifier: MIT 
contract A {
    function execute(address x, bytes calldata data) external {
        (bool success, ) = x.call(data);
   }
}