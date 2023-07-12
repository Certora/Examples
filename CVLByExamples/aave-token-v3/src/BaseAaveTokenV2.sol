// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {VersionedInitializable} from './utils/VersionedInitializable.sol';
import {BaseAaveToken} from './BaseAaveToken.sol';

abstract contract BaseAaveTokenV2 is BaseAaveToken, VersionedInitializable {
  /// @dev owner => next valid nonce to submit with permit()
  mapping(address => uint256) public _nonces;

  ///////// @dev DEPRECATED from AaveToken v1  //////////////////////////
  //////// kept for backwards compatibility with old storage layout ////
  uint256[3] private ______DEPRECATED_FROM_AAVE_V1;
  ///////// @dev END OF DEPRECATED from AaveToken v1  //////////////////////////

  bytes32 public DOMAIN_SEPARATOR;

  ///////// @dev DEPRECATED from AaveToken v2  //////////////////////////
  //////// kept for backwards compatibility with old storage layout ////
  uint256[4] private ______DEPRECATED_FROM_AAVE_V2;
  ///////// @dev END OF DEPRECATED from AaveToken v2  //////////////////////////

  bytes public constant EIP712_REVISION = bytes('1');
  bytes32 internal constant EIP712_DOMAIN =
    keccak256('EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)');
  bytes32 public constant PERMIT_TYPEHASH =
    keccak256('Permit(address owner,address spender,uint256 value,uint256 nonce,uint256 deadline)');

  uint256 public constant REVISION = 3;

  /**
   * @dev implements the permit function as for https://github.com/ethereum/EIPs/blob/8a34d644aacf0f9f8f00815307fd7dd5da07655f/EIPS/eip-2612.md
   * @param owner the owner of the funds
   * @param spender the spender
   * @param value the amount
   * @param deadline the deadline timestamp, type(uint256).max for no deadline
   * @param v signature param
   * @param s signature param
   * @param r signature param
   */

  function permit(
    address owner,
    address spender,
    uint256 value,
    uint256 deadline,
    uint8 v,
    bytes32 r,
    bytes32 s
  ) external {
    require(owner != address(0), 'INVALID_OWNER');
    //solium-disable-next-line
    require(block.timestamp <= deadline, 'INVALID_EXPIRATION');
    uint256 currentValidNonce = _nonces[owner];
    bytes32 digest = keccak256(
      abi.encodePacked(
        '\x19\x01',
        DOMAIN_SEPARATOR,
        keccak256(abi.encode(PERMIT_TYPEHASH, owner, spender, value, currentValidNonce, deadline))
      )
    );

    require(owner == ecrecover(digest, v, r, s), 'INVALID_SIGNATURE');
    unchecked {
      // does not make sense to check because it's not realistic to reach uint256.max in nonce
      _nonces[owner] = currentValidNonce + 1;
    }
    _approve(owner, spender, value);
  }

  /**
   * @dev returns the revision of the implementation contract
   */
  function getRevision() internal pure override returns (uint256) {
    return REVISION;
  }
}
