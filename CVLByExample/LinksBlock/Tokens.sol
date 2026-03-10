// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IToken {
    function getValue() external view returns (uint);
}

contract TokenA is IToken {
    function getValue() external pure returns (uint) {
        return 1;
    }
}

contract TokenB is IToken {
    function getValue() external pure returns (uint) {
        return 2;
    }
}

contract TokenC is IToken {
    function getValue() external pure returns (uint) {
        return 3;
    }
}

contract TokenD is IToken {
    function getValue() external pure returns (uint) {
        return 4;
    }
}
