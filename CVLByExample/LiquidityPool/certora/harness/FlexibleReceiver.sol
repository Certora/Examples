pragma solidity >= 0.8.0;

import "../../contracts/IFlashLoanReceiver.sol";
import "../../contracts/IPool.sol";
import "../helpers/ArbitraryValues.sol";

/**
 * A flexible implementation of the FlashLoanReceiver callback that
 * nondeterministically makes calls back to the token.
 */
contract FlexibleReceiver is IFlashLoanReceiver, ArbitraryValues {
    IPool   token;

    /**
     * Nondeterministically call {deposit}, {transferFrom}, {withdraw},
     * {transfer}, or {approve} on the {token}.
     *
     * @return true
     */
    function executeOperation(
        uint256 amount,
        uint256 premium,
        address initiator
    ) external override(IFlashLoanReceiver) returns (bool) {

        uint    callbackChoice    = arbitraryUint();

        if (callbackChoice == 0)
            token.deposit(arbitraryUint());
        else if (callbackChoice == 1)
            token.transferFrom(arbitraryAddress(),arbitraryAddress(),arbitraryUint());
        else if (callbackChoice == 2)
            token.withdraw(arbitraryUint());
        else if (callbackChoice == 3)
            token.transfer(arbitraryAddress(),arbitraryUint());
        else if (callbackChoice == 4)
            token.approve(arbitraryAddress(),arbitraryUint());

        return true;
    }
}

