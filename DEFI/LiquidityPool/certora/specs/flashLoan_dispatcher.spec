/***
 * With the `DISPATCHER` summary, the Certora Prover will assume that the recipient
 * of the `executeOperation` method could be any contract in the scene that
 * implements `executeOperation`.  The outcome of verification therefore
 * depends on the set of contracts provided on the scene.
 *
 * You can verify this spec by running any of the following scripts:
 *
 *  - `certoraRun certora/scripts/runFlashLoanNoDispatchers.conf` will verify the spec
 *    with no valid dispatchers on the scene; this will treat the method as a
 *    `HAVOC_ALL` summary.
 *
 *  - `certoraRun certora/scripts/verifyFlashLoanTrivial.conf` will verify the spec with
 *    only a trivial `FlashLoanReceiver` implementation.
 *
 *
 * See [the multi-contract section of the user guide][guide] for a complete
 * discussion of this example.
 *
 * [guide]: https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html#working-with-unknown-contracts
 */

using Asset as underlying;

methods {
    function balanceOf(address)                        external returns(uint256) envfree;
    function underlying.balanceOf(address)             external returns(uint256) envfree;
    function _.executeOperation(uint256,uint256,address) external => DISPATCHER(true);
}

/// flash loans must increase the pool's underlying asset balance, assuming the
/// receiver has no pool balance.
rule flashLoanIncreasesBalance {
    address receiver; uint256 amount; env e;

    require e.msg.sender != currentContract;

    mathint balance_before = underlying.balanceOf(currentContract);

    flashLoan(e, receiver, amount);

    mathint balance_after = underlying.balanceOf(currentContract);

    assert balance_after >= balance_before,
        "flash loans must not decrease the contract's underlying balance";
}

