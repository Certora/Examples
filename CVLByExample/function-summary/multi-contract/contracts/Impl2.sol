pragma solidity ^0.5.0;

import "./SingleContractInterface.sol";

contract Impl2 is SingleContractInterface {

    function summarizedByFunction() public returns(uint256) {
        return 2;
    }

    // function notSummarized() public returns(uint256) {
    //     return 3;
    // }

    function summarizedInCallerExternalOnly() public returns(uint256) {
        return 5;
    }


}