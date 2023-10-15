import "./Impl1.sol";
import "./Impl2.sol";

contract Main {

    Impl1 public calledContract1;
    Impl2 public calledContract2;

    // Call function from calledContract1 summarized by cvl function
    function callByFunctionInCalled1() public view returns(uint256) {
        return calledContract1.summarizedByFunction();
    }

    // Call function from calledContract2 summarized by cvl function
    function callByFunctionInCalled2() public view returns(uint256) {
        return calledContract2.summarizedByFunction();
    }

    // Call function from calledContract1 summarized by DISPATCHER
    function callByDispatcherInCalled1() public view returns(uint256) {
        return calledContract1.summarizedByDispatcher();
    }

    // Call function from calledContract2 summarized by DISPATCHER
    function callByDispatcherInContract2() public view returns(uint256) {
        return calledContract2.summarizedByDispatcher();
    }

    // Call a not-summarized function from CalledContract1
    function callnotSummarizedInCalled1() public view returns(uint256) {
        return calledContract1.notSummarized();
    }

    function callnotSummarizedInCalled2() public view returns(uint256) {
        return calledContract2.notSummarized();
    }

    // Call summarized external function from Impl1. The caller (Main) has a summarized function with the same name.
    function callSummarizedExternalInCalled1() public view returns(uint256) {
        return calledContract1.summarizedExternal();
    }

    function callSummarizedExternalInCalled2() public view returns(uint256) {
        return calledContract2.summarizedExternal();
    }

    function summarizedExternal() public pure returns(uint256) {
        return 13;
    }

    // This calls the internal summarizedInCallerExternalOnly, which is not summarized.
    function callSummarizedExternalInCaller() public pure returns(uint256) {
        return summarizedExternal();
    }

    // a public function with internal summarization in the spec
    function summarizedInternal() public pure returns(uint256) {
        return 131;
    }

    // This function calls the external summarizedInternalInCaller() which calls the internal summarizedInternalInCaller()
    // which is summarized in the spec.
    function callSummarizedInternalInCaller() public pure returns(uint256) {
        return summarizedInternal();
    }


}