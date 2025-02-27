// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v5.0.0) (token/ERC20/extensions/ERC20Permit.sol)

pragma solidity 0.8.22;

import { IERC20 } from "./IERC20.sol";

contract ERC20PermitMock is IERC20 {

    bytes32 private immutable PERMIT_TYPEHASH;

    uint256 t;
    mapping(address => uint256) b;
    mapping(address => mapping(address => uint256)) a;
    mapping(address => uint256) public nonces;

    string public name;
    string public symbol;
    uint public decimals;

    constructor(bytes32 permit_typehash) {
        PERMIT_TYPEHASH = permit_typehash;
    }

    function myAddress() external view returns (address) {
        return address(this);
    }
    
    function totalSupply() external view returns (uint256) {
        return t;
    }

    function balanceOf(address account) external view returns (uint256) {
        return b[account];
    }

    function transfer(address recipient, uint256 amount) external returns (bool) {
        b[msg.sender] -= amount;
        b[recipient] += amount;

        return true;
    }

    function allowance(address owner, address spender) external view returns (uint256) {
        return a[owner][spender];
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        return _approve(msg.sender, spender, amount);
    }

    function _approve(address owner, address spender, uint256 amount) internal returns (bool) {
        a[owner][spender] = amount;

        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool) {
        b[sender] -= amount;
        b[recipient] += amount;
        a[sender][msg.sender] -= amount;

        return true;
    }

    function permit(bytes calldata data) external {
        (
            address owner,
            address spender,
            uint256 value,
            uint256 deadline,
            uint8 v,
            bytes32 r,
            bytes32 s
        ) = abi.decode(data, (address,address,uint256,uint256,uint8,bytes32,bytes32));
        permit(owner, spender, value, deadline, v, r, s);
    }

    function permit(
        address owner,
        address spender,
        uint256 value,
        uint256 deadline,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) public virtual {
        if (block.timestamp > deadline) revert ("deadline expired");
        nonces[owner]++;
        bytes32 hash = keccak256(abi.encode(PERMIT_TYPEHASH, owner, spender, value, nonces[owner], deadline));

        address signer = ecrecover(hash, v, r, s);
        if (signer != owner) revert ("signer is not owner");

        _approve(owner, spender, value);
    }
}

contract DummyERC20A is ERC20PermitMock {
    constructor(bytes32 permit_typehash) ERC20PermitMock(permit_typehash) {}
}

contract DummyERC20B is ERC20PermitMock {
    constructor(bytes32 permit_typehash) ERC20PermitMock(permit_typehash) {}
}

contract DummyERC20C is ERC20PermitMock {
    constructor(bytes32 permit_typehash) ERC20PermitMock(permit_typehash) {}
}