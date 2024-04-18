pragma solidity ^0.8.20;

interface SomeCaller {
    function execute(uint) external returns (bool, uint);
}

contract ReturnSize {
    
    function callerFunction(address con, uint y) public returns (uint) {
        SomeCaller caller = SomeCaller(con);
        (bool status, uint x) = caller.execute(y);
        if (status){
            return x;
        }
        return y;
    }
}
