// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {IERC20Metadata} from '../../lib/openzeppelin-contracts/contracts/token/ERC20/extensions/IERC20Metadata.sol';
import {AaveTokenV3} from '../AaveTokenV3.sol';

import {AaveUtils, console} from './utils/AaveUtils.sol';

contract StorageTest is AaveUtils {
  function setUp() public {
    revertAaveImplementationUpdate();
  }

  function testForBaseMetadata() public {
    string memory nameBefore = AAVE_TOKEN.name();
    string memory symbolBefore = AAVE_TOKEN.symbol();
    uint256 decimalsBefore = AAVE_TOKEN.decimals();

    updateAaveImplementation(AAVE_IMPLEMENTATION_V3);

    assertEq(AAVE_TOKEN.name(), nameBefore);
    assertEq(AAVE_TOKEN.symbol(), symbolBefore);
    assertEq(AAVE_TOKEN.decimals(), decimalsBefore);
  }

  function testForTotalSupply() public {
    uint256 totalSupplyBefore = AAVE_TOKEN.totalSupply();

    updateAaveImplementation(AAVE_IMPLEMENTATION_V3);

    assertEq(AAVE_TOKEN.totalSupply(), totalSupplyBefore);
  }

  function testForBalances() public {
    uint256[] memory balancesBefore = new uint256[](AAVE_HOLDERS.length);
    for (uint256 i = 0; i < AAVE_HOLDERS.length; i += 1) {
      balancesBefore[i] = AAVE_TOKEN.balanceOf(AAVE_HOLDERS[i]);
    }
    updateAaveImplementation(AAVE_IMPLEMENTATION_V3);
    for (uint256 i = 0; i < AAVE_HOLDERS.length; i += 1) {
      assertEq(AAVE_TOKEN.balanceOf(AAVE_HOLDERS[i]), balancesBefore[i]);
    }
  }
}
