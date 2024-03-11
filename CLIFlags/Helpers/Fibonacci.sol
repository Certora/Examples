// SPDX-License-Identifier: AGPL-3.0-only

pragma solidity >=0.8.0;


contract Fibonacci {
    function fibonacci(uint32 i) external returns (uint32) {
        if(i == 1 || i == 2) {
            return 1;
        }
        return this.fibonacci(i- 1) + this.fibonacci(i - 2);
    }
}