pragma solidity ^0.8.0;

/**
 * 
 */
contract DataInvariant {

    mapping(address => int256) public balance;
    mapping(address => bool) public accessInvariant;

    constructor() {
    }

    function increase(address a, int256 value) external {
        require(value >= 0);
        balance[a] += value;
    }

    function temporarilyMakeNegative(address a, int256 value) external returns (bool accessInv) {
        require(value >= 0);
        balance[a] -= value;
        accessInv = accessInvariant[a];
        balance[a] += value;
    }

    function breakInvariant(address a, int256 value) external returns (bool accessInv) {
        require(value >= 0);
        balance[a] -= 2*value;
        accessInv = accessInvariant[a];
        balance[a] += value;
    }

    function temporarilyAdd(address a, int256 value) external returns (bool accessInv) {
        require(value >= 0);
        balance[a] += value;
        accessInv = accessInvariant[a];
        balance[a] -= value;
    }

    function addTogether(address a, address b, address c, int256 value) external returns (bool accessInv) {
        balance[a] += balance[b];
        balance[a] += balance[c];

        accessInv = (accessInvariant[b] == accessInvariant[c]);
    }

    function addTogetherAndIncrease(address a, address b, address c, int256 value) external returns (bool accessInv) {
        require(value >= 0);
        balance[a] += balance[b];
        balance[a] += balance[c];

        balance[b] += value;
        balance[c] += value;
        
        accessInv = (accessInvariant[b] == accessInvariant[c]);
    }
}
