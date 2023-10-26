pragma solidity ^0.5.0;
import "Impl1.sol";
import "Impl2.sol";

contract Caller1 {

    Impl1 public impl1;
    Impl2 public impl2;

    function callGetSomeUIntInImpl1() public returns(uint256) {
        return impl1.getSomeUInt();
    }

    function callGetSomeUIntInImpl2() public returns(uint256) {
        return impl2.getSomeUInt();
    }

    
}