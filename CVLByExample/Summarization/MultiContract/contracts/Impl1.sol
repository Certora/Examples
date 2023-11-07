// pragma solidity ^0.8.19;

import "./SingleContractInterface.sol";

contract Impl1 is SingleContractInterface {

    function summarizedByFunction() public pure override returns(uint256) {
        return 1;
    }

    function summarizedByDispatcher() public pure override returns(uint256) {
        return 11;
    }
    
    function notSummarized() public pure override returns(uint256) {
        return 3;
    }

    function summarizedExternal() public pure override returns(uint256) {
        return 5;
    }

}