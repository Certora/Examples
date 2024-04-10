pragma solidity 0.8.10;
pragma experimental ABIEncoderV2;

/*
A wrapper contract for calling functions from the library UserConfiguration.
*/
contract PerciseBitwiseOps{
    uint16 public constant MAX_RESERVES_COUNT = 128;
    string public constant INVALID_RESERVE_INDEX = '74'; // 'Invalid reserve index'
    uint256 public data;

    constructor(){
        data = 0;
    }

    function setBorrowing(
    uint256 reserveIndex,
    bool borrowing
  ) public {
    unchecked {
      require(reserveIndex < MAX_RESERVES_COUNT, INVALID_RESERVE_INDEX);
      uint256 bit = 1 << (reserveIndex << 1);
      if (borrowing) {
        data |= bit;
      } else {
        data &= ~bit;
      }
    }
  }

  function isBorrowing(
    uint256 reserveIndex
  ) public view returns (bool) {
    unchecked {
      require(reserveIndex < MAX_RESERVES_COUNT, INVALID_RESERVE_INDEX);
      return (data >> (reserveIndex << 1)) & 1 != 0;
    }
  }
}
