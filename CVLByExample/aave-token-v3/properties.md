# AAVE token V3. Specs

## Summary of v2 → v3

AAVE is an ERC20 token deployed on Ethereum, which main utility is participating in the Aave governance system via voting on proposals or creating them.

AAVE is a transparent proxy contract, and its current implementation ([here](https://etherscan.io/address/0xc13eac3b4f9eed480045113b7af00f7b5655ece8#code)) is version 2.

Together will all the standard ERC20 functionalities, the current implementation includes extra logic mainly for the management and accounting of voting and proposition power. Due to the design/architecture of the Aave governance v2 system, of which AAVE is the main voting asset, the current AAVE implementation makes the token transfers quite gas-consuming, as multiple snapshots of data (voting and proposition power) need to be stored all the time.

With a new iteration of the Aave governance in the Aave/BGD roadmap down the line, snapshots on the token will not be required anymore for its integration with the governance system. So this new version 3 of AAVE consists mainly of removing the snapshotting, together with adding extra minor meta-transactions capabilities.

## Glossary

$t_0$ → the state of the system before a transaction.

$t_1$ → the state of the system after a transaction.

**account** → Ethereum address involved in a transaction on the system.

**power** → any and only one between proposition or voting powers. It can be delegated from one account to another.

**proposition power** → measures the influence an account has regarding creating proposals on the Aave governance.

**voting power** → measures the influence an account has regarding voting on proposals on the Aave governance.

**delegation** → power that an account can use, not generate from his own AAVE balance.

**balance** → the amount of AAVE tokens belonging to an account `balanceOf(account)` at any time $t$.

## General rules

- The total power (of one type) of all users in the system is less or equal than the sum of balances of all AAVE holders (totalSupply of AAVE token): $$\sum powerOfAccount_i <= \sum balanceOf(account_i)$$
- If an account is delegating a power to itself or to `address(0)`, that means that account is not delegating that power to anybody:

  $$powerOfAccountX = (accountXDelegatingPower \ ? \ 0 : balanceOf(accountX)) +
  \sum (balanceOf(accountDelegatingPowerToAccountX_i) \ / \ 10^{10} * 10^{10})$$

- If an account is not receiving delegation of power (one type) from anybody, and that account is not delegating that power to anybody, the power of that account must be equal to its AAVE balance.
- The power of all other accounts not described in cases should stay constant.
- Account1 ≠ account2 on the following cases.

## Account1 and account2 are not delegating power

- On transfer of $\forall z >= 0$ of AAVE tokens from **account1** to **account2**

  $$account1Power_{t1} = account1Power_{t0} - z$$

  $$account2Power_{t1} = account2Power_{t0} + z$$

- After **account1** will delegate his **power** to **account2**

  $$account1Power_{t1} = account1Power_{t0} - account1Balance$$

  $$account2Power_{t1} = account2Power_{t0} + account1Balance / 10^{10} * 10^{10}$$

  $$account1PowerDelegatee_{t1} = account2$$


## Account1 is delegating power to delegatee1, account2 is not delegating power to anybody

- On transfer of $\forall z >= 0$ of AAVE tokens from **account1** to **account2**

  $$account1Power_{t1} = account1Power_{t0} = 0$$

  $$delegatee1Power_{t1} = delegatee1Power_{t0} - account1Balance_{t0} / 10^{10} * 10^{10} + account1Balance_{t1} / 10^{10} * 10^{10}$$

  $$account2Power_{t1} = account2Power_{t0} + z$$

- After **account1** will stop delegating his **power** to **delegatee1**

  $$account1Power_{t1} = account1Power_{t0} + account1Balance$$

  $$delegatee1Power_{t1} = delegatee1Power_{t0} - account1Balance / 10^{10} * 10^{10}$$$$

- After **account1** will delegate **power** to **delegatee2**

  $$account1Power_{t1} = account1Power_{t0} = 0$$

  $$delegatee1Power_{t1} = delegatee1Power_{t0} - account1Balance / 10^{10} * 10^{10}$$

  $$delegatee2Power_{t1} = delegatee2Power_{t0} + account1Balance / 10^{10} * 10^{10}$$

  $$account1PowerDelegatee_{t1} = delegatee2$$


## Account1 not delegating power to anybody, **account2** is delegating power to delegatee2

- On transfer of $\forall z >= 0$ of AAVE tokens from **account1** to **account2**

  $$account1Power_{t1} = account1Power_{t0} - z$$

  $$account2Power_{t1} = account2Power_{t0} = 0$$

  $$delegatee2Power_{t1}=delegatee2Power_{t0} - account2Balance_{t0} / 10^{10} * 10^{10} + account2Balance_{t1} / 10^{10} * 10^{10}$$


## Account1 is delegating power to delegatee1, **account2** is delegating power to delegatee2

- On transfer of $\forall z >= 0$ of AAVE tokens from **account1** to **account2**

  $$account1Power_{t1} = account1Power_{t0} = 0$$

  $$delegatee1Power_{t1} = delegatee1Power_{t0} - account1Balance_{t0} / 10^{10} * 10^{10} + account1Balance_{t1} / 10^{10} * 10^{10}$$

  $$account2Power_{t1} = account2Power_{t0} = 0$$

  $$delegatee2Power_{t1}=delegatee2Power_{t0} - account2Balance_{t0} / 10^{10} * 10^{10} + account2Balance_{t1} / 10^{10} * 10^{10}$$
