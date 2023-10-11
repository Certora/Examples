abstract contract SingleContractInterface {

    function summarizedByFunction() public pure virtual  returns(uint256);
    function summarizedByDispatcher() public pure virtual returns(uint256); 
    function notSummarized() public virtual returns(uint256);
    function summarizedExternal() public virtual returns(uint256);
}    