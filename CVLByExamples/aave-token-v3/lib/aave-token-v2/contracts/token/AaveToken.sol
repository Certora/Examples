// SPDX-License-Identifier: agpl-3.0
pragma solidity 0.7.5;

import {ERC20} from '../open-zeppelin/ERC20.sol';
import {ITransferHook} from '../interfaces/ITransferHook.sol';
import {VersionedInitializable} from '../utils/VersionedInitializable.sol';
import {SafeMath} from '../open-zeppelin/SafeMath.sol';

/**
 * @notice implementation of the AAVE token contract
 * @author Aave
 */
contract AaveToken is ERC20, VersionedInitializable {
  using SafeMath for uint256;

  /// @dev snapshot of a value on a specific block, used for balances
  struct Snapshot {
    uint128 blockNumber;
    uint128 value;
  }

  string internal constant NAME = 'Aave Token';
  string internal constant SYMBOL = 'AAVE';
  uint8 internal constant DECIMALS = 18;

  /// @dev the amount being distributed for the LEND -> AAVE migration
  uint256 internal constant MIGRATION_AMOUNT = 13000000 ether;

  /// @dev the amount being distributed for the PSI and PEI
  uint256 internal constant DISTRIBUTION_AMOUNT = 3000000 ether;

  uint256 public constant REVISION = 1;

  /// @dev owner => next valid nonce to submit with permit()
  mapping(address => uint256) public _nonces;

  mapping(address => mapping(uint256 => Snapshot)) public _snapshots;

  mapping(address => uint256) public _countsSnapshots;

  /// @dev reference to the Aave governance contract to call (if initialized) on _beforeTokenTransfer
  /// !!! IMPORTANT The Aave governance is considered a trustable contract, being its responsibility
  /// to control all potential reentrancies by calling back the AaveToken
  ITransferHook public _aaveGovernance;

  bytes32 public DOMAIN_SEPARATOR;
  bytes public constant EIP712_REVISION = bytes('1');
  bytes32 internal constant EIP712_DOMAIN = keccak256(
    'EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)'
  );
  bytes32 public constant PERMIT_TYPEHASH = keccak256(
    'Permit(address owner,address spender,uint256 value,uint256 nonce,uint256 deadline)'
  );

  event SnapshotDone(address owner, uint128 oldValue, uint128 newValue);

  constructor() public ERC20(NAME, SYMBOL) {}

  /**
   * @dev initializes the contract upon assignment to the InitializableAdminUpgradeabilityProxy
   * @param migrator the address of the LEND -> AAVE migration contract
   * @param distributor the address of the AAVE distribution contract
   */
  function initialize(
    address migrator,
    address distributor,
    ITransferHook aaveGovernance
  ) external initializer {
    uint256 chainId;

    //solium-disable-next-line
    assembly {
      chainId := chainid()
    }

    DOMAIN_SEPARATOR = keccak256(
      abi.encode(
        EIP712_DOMAIN,
        keccak256(bytes(NAME)),
        keccak256(EIP712_REVISION),
        chainId,
        address(this)
      )
    );
    _name = NAME;
    _symbol = SYMBOL;
    _setupDecimals(DECIMALS);
    _aaveGovernance = aaveGovernance;
    _mint(migrator, MIGRATION_AMOUNT);
    _mint(distributor, DISTRIBUTION_AMOUNT);
  }

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
    _nonces[owner] = currentValidNonce.add(1);
    _approve(owner, spender, value);
  }

  /**
   * @dev returns the revision of the implementation contract
   */
  function getRevision() internal override pure returns (uint256) {
    return REVISION;
  }

  /**
   * @dev Writes a snapshot for an owner of tokens
   * @param owner The owner of the tokens
   * @param oldValue The value before the operation that is gonna be executed after the snapshot
   * @param newValue The value after the operation
   */
  function _writeSnapshot(
    address owner,
    uint128 oldValue,
    uint128 newValue
  ) internal {
    uint128 currentBlock = uint128(block.number);

    uint256 ownerCountOfSnapshots = _countsSnapshots[owner];
    mapping(uint256 => Snapshot) storage snapshotsOwner = _snapshots[owner];

    // Doing multiple operations in the same block
    if (
      ownerCountOfSnapshots != 0 &&
      snapshotsOwner[ownerCountOfSnapshots - 1].blockNumber == currentBlock
    ) {
      snapshotsOwner[ownerCountOfSnapshots - 1].value = newValue;
    } else {
      snapshotsOwner[ownerCountOfSnapshots] = Snapshot(currentBlock, newValue);
      _countsSnapshots[owner] = ownerCountOfSnapshots + 1;
    }

    emit SnapshotDone(owner, oldValue, newValue);
  }

  /**
   * @dev Writes a snapshot before any operation involving transfer of value: _transfer, _mint and _burn
   * - On _transfer, it writes snapshots for both "from" and "to"
   * - On _mint, only for _to
   * - On _burn, only for _from
   * @param from the from address
   * @param to the to address
   * @param amount the amount to transfer
   */
  function _beforeTokenTransfer(
    address from,
    address to,
    uint256 amount
  ) internal override {
    if (from == to) {
      return;
    }

    if (from != address(0)) {
      uint256 fromBalance = balanceOf(from);
      _writeSnapshot(from, uint128(fromBalance), uint128(fromBalance.sub(amount)));
    }
    if (to != address(0)) {
      uint256 toBalance = balanceOf(to);
      _writeSnapshot(to, uint128(toBalance), uint128(toBalance.add(amount)));
    }

    // caching the aave governance address to avoid multiple state loads
    ITransferHook aaveGovernance = _aaveGovernance;
    if (aaveGovernance != ITransferHook(0)) {
      aaveGovernance.onTransfer(from, to, amount);
    }
  }
}
