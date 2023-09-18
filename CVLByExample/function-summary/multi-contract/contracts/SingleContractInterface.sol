pragma solidity ^0.8.19;

abstract contract SingleContractInterface {

    function summarizedByFunction() public virtual  returns(uint256);

    function notSummarized() public virtual returns(uint256);
    function summarizedInCallerExternalOnly() public virtual returns(uint256);

}