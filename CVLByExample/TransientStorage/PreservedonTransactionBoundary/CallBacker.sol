pragma solidity 0.8.24;

import {Vault} from './Vault.sol';

contract CallBacker {
    Vault v;
    constructor(address vault){
        v = Vault(vault);
    }
    function callback() public {
        int256 delta = v.getDelta();
        v.borrow(delta);
        v.repay(delta);
    }
}