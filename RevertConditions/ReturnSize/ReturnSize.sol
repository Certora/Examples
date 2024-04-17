pragma solidity ^0.8.20;

interface ILib {
    function calledFunction(uint) external returns (bool, uint);
}

contract ReturnSize {
    
    function callerFunction(address lib, uint y) public returns (uint) {
        ILib libContract = ILib(lib);
        (bool status, uint x) = libContract.calledFunction(y);
        if (status){
            return x;
        }
        return y;
    }
}
