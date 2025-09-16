// SPDX-License-Identifier: MIT 
contract A {
    bool public a_field;
    function execute(address x, bytes calldata data) external {
        (bool success, ) = x.call(data);
   }
}