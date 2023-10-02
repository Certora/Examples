pragma solidity ^0.8.19;

abstract contract SingleContractInterface {

    function summarizedByFunction() public pure virtual  returns(uint256);
    function summarizedByDispatcher() public pure virtual returns(uint256); 
    function notSummarized() public virtual returns(uint256);
    function summarizedInCallerExternalOnly() public virtual returns(uint256);
    function summarizedByECF() public virtual returns(uint256);
}    