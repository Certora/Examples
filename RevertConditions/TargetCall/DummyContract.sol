pragma solidity ^0.8.20;


contract DummyContract{
    // Function to be called
    function execute() external returns (bool, uint) {
        // Dummy implementation, returns true and 123
        return (true, 123);
    }
}