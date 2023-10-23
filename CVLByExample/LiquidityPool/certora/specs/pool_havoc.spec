/// Without linking, the `integrityOfDeposit` rule will not pass, because the
/// `deposit` and `balanceOf` methods are unresolved and the Certora Prover allows them
/// to return arbitrary values.
///
/// You can verify this spec by running the following from the command line:
///
///      sh certora/scripts/verifyJustPool.sh
///
/// See [the multi-contract section of the user guide](https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html) for a complete
/// discussion of this example.

methods
{
    function balanceOf(address)                      external returns(uint256) envfree;
    function totalSupply()                           external returns(uint256) envfree;
    function transfer(address, uint256)              external returns(bool);
    function transferFrom(address, address, uint256) external returns(bool);

    function deposit(uint256)                        external returns(uint256);
    function withdraw(uint256)                       external returns(uint256);
    function assetBalance()                          external returns(uint256) envfree;

    function flashLoan(address, uint256) external;
}

/// `deposit` must increase the pool's underlying asset balance
rule integrityOfDeposit {

    mathint balance_before = assetBalance();

    env e; uint256 amount;
    require e.msg.sender != currentContract;

    deposit(e, amount);

    mathint balance_after = assetBalance();

    assert balance_after == balance_before + amount,
        "deposit must increase the underlying balance of the pool";
} 

