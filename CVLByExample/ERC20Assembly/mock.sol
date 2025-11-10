// SPDX-License-Identifier: MIT

pragma solidity 0.8.22;

contract mock {

    address public approveTo;
    uint256 public approveAmount;
    bool public approveSuccess;

    function approve(address to, uint256 amount) external {
        approveTo = to;
        approveAmount = amount;
        assert(approveSuccess || amount == 0);
    }

    address public permitOwner;
    address public permitSpender;
    uint256 public permitValue;
    uint256 public permitDeadline;
    bool public permitAllowed;
    uint8 public permitV;
    bytes32 public permitR;
    bytes32 public permitS;
    bytes32 public permitDatahash;
    bool public permitSuccess;

    function permit(address owner, address spender, 
        uint256 value, uint256 deadline, uint8 v, bytes32 r, bytes32 s) 
    external {
        permitOwner = owner;
        permitSpender = spender;
        permitValue = value;
        permitDeadline = deadline;
        permitV = v;
        permitR = r;
        permitS = s;
        permitDatahash = keccak256(abi.encode(owner,spender,value,deadline,v,r,s));
        assert(permitSuccess);
    }

    function permit(address owner, address spender, 
        uint256 value, uint256 deadline, bool allowed, uint8 v, bytes32 r, bytes32 s) 
    external {
        permitOwner = owner;
        permitSpender = spender;
        permitValue = value;
        permitDeadline = deadline;
        permitAllowed = allowed;
        permitV = v;
        permitR = r;
        permitS = s;
        permitDatahash = keccak256(abi.encode(owner,spender,value,deadline,allowed,v,r,s));
        assert(permitSuccess);
    }

    address public safeTransferRecipient;
    uint256 public safeTransferAmount;
    bool public safeTransferSuccess;

    function transfer(address recipient, uint256 amount) external returns (bool) {
        safeTransferRecipient = recipient;
        safeTransferAmount = amount;
        return safeTransferSuccess;
    }

    address public safeTransferFromSender;
    address public safeTransferFromRecipient;
    uint256 public safeTransferFromAmount;
    bool public safeTransferFromSuccess;

    function transferFrom(address sender, address recipient, uint256 amount)
        external
        returns (bool)
    {
        safeTransferFromSender = sender;
        safeTransferFromRecipient = recipient;
        safeTransferFromAmount = amount;
        return safeTransferFromSuccess;
    }

    address public getBalanceAccount;
    uint256 public balance;

    function balanceOf(address account) external returns (uint256) {
        getBalanceAccount = account;
        return balance;
    }
}