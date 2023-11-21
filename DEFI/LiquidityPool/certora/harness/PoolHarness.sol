pragma solidity >= 0.8.0;

import "../../contracts/Pool.sol";

contract PoolHarness is Pool {
    function underlyingBalance() public returns(uint256) {
        return asset.balanceOf(address(this));
    }

    function underlyingAllowance(address a) public returns(uint256) {
        return asset.allowance(address(this), a);
    }
}
