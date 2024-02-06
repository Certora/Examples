// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// game developer depoloys contract
contract Verify {

    function isSigned(address _addr, bytes32 msgHash, uint8 v, bytes32 r, bytes32 s) external  returns (bool) {
        return ecrecover(msgHash, v, r, s) == _addr;
    }


mapping (address => uint256) private nonces; 

function executeMyFunctionFromSignature(
    uint8 v,
    bytes32 r,
    bytes32 s,
    address owner,
    uint256 myParam,
    uint256 deadline
) external {

    bytes32 hash = getHash(/*owner*/ msg.sender, myParam, deadline); // computing the has on the wrong address

    
    address signer = ecrecover(hash, v, r, s);
    require(signer == owner, "MyFunction: invalid signature");
    require(signer != address(0), "ECDSA: invalid signature");

    require(block.timestamp < deadline, "MyFunction: signed transaction expired");
    nonces[owner]++; 

    _myFunction(owner, myParam);
}

function _myFunction(address owner, uint256 myParam) internal {

}

function getHash(
    address owner,
    uint256 myParam,
    uint256 deadline
) public returns(bytes32) {
    bytes32 eip712DomainHash = keccak256(
        abi.encode(
            keccak256(
                "EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)"
            ),
            keccak256(bytes("MyContractName")),
            keccak256(bytes("1")),
            address(this)
        )
    );

    bytes32 hashStruct = keccak256(
        abi.encode(
            keccak256("MyFunction(address owner,uint256 myParam,uint256 nonce,uint256 deadline)"),
            owner,
            myParam,
            nonces[owner],
            deadline
        )
    );

    return keccak256(abi.encodePacked("\x19\x01", eip712DomainHash, hashStruct));
}
}