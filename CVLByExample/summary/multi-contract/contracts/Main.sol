pragma solidity ^0.8.19;
import "./Impl1.sol";
import "./Impl2.sol";

contract Main {

    Impl1 public calledContract1;
    Impl2 public calledContract2;

    function callSummarizedByFunctionInCalledContract1() public view returns(uint256) {
        return calledContract1.summarizedByFunction();
    }

    function callSummarizedByFunctionInCalledContract2() public view returns(uint256) {
        return calledContract2.summarizedByFunction();
    }

    function callSummarizedByDispatcherInCalledContract1() public view returns(uint256) {
        return calledContract1.summarizedByDispatcher();
    }

    function callSummarizedByDispatcherInCalledContract2() public view returns(uint256) {
        return calledContract2.summarizedByDispatcher();
    }


    function callnotSummarizedInCalledContract1() public view returns(uint256) {
        return calledContract1.notSummarized();
    }

    function callnotSummarizedInCalledContract2() public view returns(uint256) {
        return calledContract2.notSummarized();
    }

    function callSummarizedInCallerExternalOnlyInCalledContract1() public view returns(uint256) {
        return calledContract1.summarizedInCallerExternalOnly();
    }

    function callSummarizedInCallerExternalOnlyInCalledContract2() public view returns(uint256) {
        return calledContract2.summarizedInCallerExternalOnly();
    }

    function summarizedInCallerExternalOnly() public pure returns(uint256) {
        return 13;
    }

    // This calls the internal summarizedInCallerExternalOnly which is not summarized.
    function callSummarizedInCallerExternalOnly() public pure returns(uint256) {
        return summarizedInCallerExternalOnly();
    }

    function summarizedInternalInCaller() public pure returns(uint256) {
        return 131;
    }

    function callSummarizedInternalInCaller() public pure returns(uint256) {
        return summarizedInternalInCaller();
    }


}