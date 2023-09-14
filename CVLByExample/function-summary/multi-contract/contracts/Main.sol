pragma solidity ^0.8.19;
import "./Impl1.sol";
import "./Impl2.sol";

contract Main {

    Impl1 public calledContract1;
    Impl2 public calledContract2;

    function callSummarizedByFunctionInCalledContract1() public returns(uint256) {
        return calledContract1.summarizedByFunction();
    }

    function callSummarizedByFunctionInCalledContract2() public returns(uint256) {
        return calledContract2.summarizedByFunction();
    }

    function callnotSummarizedInCalledContract1() public returns(uint256) {
        return calledContract1.notSummarized();
    }

    function callnotSummarizedInCalledContract2() public returns(uint256) {
        return calledContract2.notSummarized();
    }

    function callSummarizedInCallerExternalOnlyInCalledContract1() public returns(uint256) {
        return calledContract1.summarizedInCallerExternalOnly();
    }

    function callSummarizedInCallerExternalOnlyInCalledContract2() public returns(uint256) {
        return calledContract2.summarizedInCallerExternalOnly();
    }

    function summarizedInCallerExternalOnly() public returns(uint256) {
        return 13;
    }

    // This calls the internal summarizedInCallerExternalOnly which is not summarized.
    function callSummarizedInCallerExternalOnly() public returns(uint256) {
        return summarizedInCallerExternalOnly();
    }

    function summarizedInternalInCaller() public returns(uint256) {
        return 131;
    }

    function callSummarizedInternalInCaller() public returns(uint256) {
        return summarizedInternalInCaller();
    }

}