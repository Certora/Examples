pragma solidity ^0.8.19;

import "./SingleContractInterface.sol";

contract Impl2 is SingleContractInterface {

    function summarizedByFunction() public pure override returns(uint256) {
        return 2;
    }

    function notSummarized() public pure override returns(uint256) {
        return 3;
    }

    function summarizedInCallerExternalOnly() public pure override returns(uint256) {
        return 5;
    }

    function summarizedByECF() public pure override returns(uint256) {
        return 8;
    }

}