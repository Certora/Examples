pragma solidity ^0.8.19;

import "./SingleContractInterface.sol";

abstract contract Impl2 is SingleContractInterface {

    function summarizedByFunction() public pure override returns(uint256) {
        return 2;
    }

    // function notSummarized() public returns(uint256) {
    //     return 3;
    // }

    function summarizedInCallerExternalOnly() public pure override returns(uint256) {
        return 5;
    }


}