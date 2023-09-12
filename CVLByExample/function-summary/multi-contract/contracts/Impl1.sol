pragma solidity ^0.5.0;

contract Impl1 {

    function summarizedByFunction() public returns(uint256) {
        return 1;
    }

    function notSummarized() public returns(uint256) {
        return 3;
    }

    function summarizedInCallerExternalOnly() public returns(uint256) {
        return 5;
    }

}