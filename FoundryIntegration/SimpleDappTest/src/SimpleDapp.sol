//SPDX-License-Identifier: MIT

pragma solidity ^0.8.23;

/// @title SimpleDapp
/// @notice This contract allows for deposits and withdrawals of ETH by users
contract SimpleDapp {
    mapping(address => uint256) public balances;

    /// @notice Deposit ETH into the contract
    /// @dev This function will deposit ETH into the contract and update the mapping balances.abi
    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    /// @notice Withdraw ETH from the contract
    /// @dev This function will withdraw ETH from the contract and update the mapping balances.
    /// @param _amount The amount of ETH to withdraw
    function withdraw(uint256 _amount) external {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] -= _amount;
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Withdraw failed");
    }
}
