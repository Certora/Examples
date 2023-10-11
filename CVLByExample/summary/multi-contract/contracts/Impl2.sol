// pragma solidity ^0.8.19;

import "./SingleContractInterface.sol";

contract Impl2 is SingleContractInterface {

    function summarizedByFunction() public pure override returns(uint256) {
        return 2;
    }

    function summarizedByDispatcher() public pure override returns(uint256) {
        return 22;
    }

    function notSummarized() public pure override returns(uint256) {
        return 3;
    }

    function summarizedExternal() public pure override returns(uint256) {
        return 5;
    }

}