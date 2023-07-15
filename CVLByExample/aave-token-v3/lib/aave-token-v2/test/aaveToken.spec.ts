import {fail} from 'assert';
import {ethers} from 'ethers';
import BigNumber from 'bignumber.js';
import {TestEnv, makeSuite} from './helpers/make-suite';
import {ProtocolErrors} from '../helpers/types';
import {eEthereumNetwork} from '../helpers/types-common';
import {waitForTx, DRE} from '../helpers/misc-utils';
import {
  getInitializableAdminUpgradeabilityProxy,
  buildPermitParams,
  getSignatureFromTypedData,
  deployDoubleTransferHelper,
} from '../helpers/contracts-helpers';
import {
  getAaveTokenDomainSeparatorPerNetwork,
  BUIDLEREVM_CHAINID,
  ZERO_ADDRESS,
  MAX_UINT_AMOUNT,
} from '../helpers/constants';

const {expect} = require('chai');

makeSuite('AAVE token', (testEnv: TestEnv) => {
  const {} = ProtocolErrors;

  it('Checks initial configuration', async () => {
    const {aaveToken} = testEnv;

    expect(await aaveToken.name()).to.be.equal('Aave Token', 'Invalid token name');

    expect(await aaveToken.symbol()).to.be.equal('AAVE', 'Invalid token symbol');

    expect((await aaveToken.decimals()).toString()).to.be.equal('18', 'Invalid token decimals');
  });

  it('Checks the domain separator', async () => {
    const network = DRE.network.name;
    const DOMAIN_SEPARATOR_ENCODED = getAaveTokenDomainSeparatorPerNetwork(
      network as eEthereumNetwork
    );
    const {aaveToken} = testEnv;

    const separator = await aaveToken.DOMAIN_SEPARATOR();
    expect(separator).to.be.equal(DOMAIN_SEPARATOR_ENCODED, 'Invalid domain separator');
  });

  it('Checks the revision', async () => {
    const {aaveToken} = testEnv;

    const revision = await aaveToken.REVISION();

    expect(revision.toString()).to.be.equal('1', 'Invalid revision');
  });

  it('Checks the allocation of the initial AAVE supply', async () => {
    const expectedMigratorBalance = new BigNumber(13000000).times(new BigNumber(10).pow(18));
    const expectedlDistributorBalance = new BigNumber(3000000).times(new BigNumber(10).pow(18));
    const {aaveToken, lendToAaveMigrator} = testEnv;
    const migratorBalance = await aaveToken.balanceOf(lendToAaveMigrator.address);
    const distributorBalance = await aaveToken.balanceOf(testEnv.users[0].address);

    expect(migratorBalance.toString()).to.be.equal(
      expectedMigratorBalance.toFixed(0),
      'Invalid migrator balance'
    );
    expect(distributorBalance.toString()).to.be.equal(
      expectedlDistributorBalance.toFixed(0),
      'Invalid migrator balance'
    );
  });

  it('Starts the migration', async () => {
    const {lendToAaveMigrator, lendToAaveMigratorImpl, users} = testEnv;

    const lendToAaveMigratorInitializeEncoded = lendToAaveMigratorImpl.interface.encodeFunctionData(
      'initialize'
    );

    const migratorAsProxy = await getInitializableAdminUpgradeabilityProxy(
      lendToAaveMigrator.address
    );

    await migratorAsProxy
      .connect(users[0].signer)
      .upgradeToAndCall(lendToAaveMigratorImpl.address, lendToAaveMigratorInitializeEncoded);
  });

  it('Checks the snapshots emitted after the initial allocation', async () => {
    const {aaveToken, users} = testEnv;

    const userCountOfSnapshots = await aaveToken._countsSnapshots(users[0].address);
    const snapshot = await aaveToken._snapshots(users[0].address, userCountOfSnapshots.sub(1));
    expect(userCountOfSnapshots.toString()).to.be.equal('1', 'INVALID_SNAPSHOT_COUNT');
    expect(snapshot.value.toString()).to.be.equal(
      ethers.utils.parseEther('3000000'),
      'INVALID_SNAPSHOT_VALUE'
    );
  });

  it('Record correctly snapshot on migration', async () => {
    const {aaveToken, lendToAaveMigrator, deployer, lendToken} = testEnv;

    await waitForTx(await lendToken.mint(ethers.utils.parseEther('2000')));
    await waitForTx(
      await lendToken.approve(lendToAaveMigrator.address, ethers.utils.parseEther('2000'))
    );
    await waitForTx(await lendToAaveMigrator.migrateFromLEND(ethers.utils.parseEther('2000')));

    expect((await aaveToken.balanceOf(deployer.address)).toString()).to.be.equal(
      ethers.utils.parseEther('2'),
      'INVALID_BALANCE_AFTER_MIGRATION'
    );

    const userCountOfSnapshots = await aaveToken._countsSnapshots(deployer.address);
    const snapshot = await aaveToken._snapshots(deployer.address, userCountOfSnapshots.sub(1));
    expect(userCountOfSnapshots.toString()).to.be.equal('1', 'INVALID_SNAPSHOT_COUNT');
    expect(snapshot.value.toString()).to.be.equal(
      ethers.utils.parseEther('2'),
      'INVALID_SNAPSHOT_VALUE'
    );
  });

  it('Record correctly snapshot on transfer', async () => {
    const {aaveToken, deployer, users} = testEnv;
    const from = deployer.address;
    const to = users[1].address;
    await waitForTx(await aaveToken.transfer(to, ethers.utils.parseEther('1')));
    const fromCountOfSnapshots = await aaveToken._countsSnapshots(from);
    const fromLastSnapshot = await aaveToken._snapshots(from, fromCountOfSnapshots.sub(1));
    const fromPreviousSnapshot = await aaveToken._snapshots(from, fromCountOfSnapshots.sub(2));

    const toCountOfSnapshots = await aaveToken._countsSnapshots(to);
    const toSnapshot = await aaveToken._snapshots(to, toCountOfSnapshots.sub(1));

    expect(fromCountOfSnapshots.toString()).to.be.equal('2', 'INVALID_SNAPSHOT_COUNT');
    expect(fromLastSnapshot.value.toString()).to.be.equal(
      ethers.utils.parseEther('1'),
      'INVALID_SNAPSHOT_VALUE'
    );
    expect(fromPreviousSnapshot.value.toString()).to.be.equal(
      ethers.utils.parseEther('2'),
      'INVALID_SNAPSHOT_VALUE'
    );

    expect(toCountOfSnapshots.toString()).to.be.equal('1', 'INVALID_SNAPSHOT_COUNT');
    expect(toSnapshot.value.toString()).to.be.equal(
      ethers.utils.parseEther('1'),
      'INVALID_SNAPSHOT_VALUE'
    );
  });

  it('Reverts submitting a permit with 0 expiration', async () => {
    const {aaveToken, deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const expiration = 0;
    const nonce = (await aaveToken._nonces(owner)).toNumber();
    const permitAmount = ethers.utils.parseEther('2').toString();
    const msgParams = buildPermitParams(
      chainId,
      aaveToken.address,
      owner,
      spender,
      nonce,
      permitAmount,
      expiration.toFixed()
    );

    const ownerPrivateKey = require('../test-wallets.js').accounts[0].secretKey;
    if (!ownerPrivateKey) {
      throw new Error('INVALID_OWNER_PK');
    }

    expect((await aaveToken.allowance(owner, spender)).toString()).to.be.equal(
      '0',
      'INVALID_ALLOWANCE_BEFORE_PERMIT'
    );

    const {v, r, s} = getSignatureFromTypedData(ownerPrivateKey, msgParams);

    await expect(
      aaveToken.connect(users[1].signer).permit(owner, spender, permitAmount, expiration, v, r, s)
    ).to.be.revertedWith('INVALID_EXPIRATION');

    expect((await aaveToken.allowance(owner, spender)).toString()).to.be.equal(
      '0',
      'INVALID_ALLOWANCE_AFTER_PERMIT'
    );
  });

  it('Submits a permit with maximum expiration length', async () => {
    const {aaveToken, deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    const configChainId = DRE.network.config.chainId;
    expect(configChainId).to.be.equal(chainId);
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const deadline = MAX_UINT_AMOUNT;
    const nonce = (await aaveToken._nonces(owner)).toNumber();
    const permitAmount = ethers.utils.parseEther('2').toString();
    const msgParams = buildPermitParams(
      chainId,
      aaveToken.address,
      owner,
      spender,
      nonce,
      deadline,
      permitAmount
    );

    const ownerPrivateKey = require('../test-wallets.js').accounts[0].secretKey;
    if (!ownerPrivateKey) {
      throw new Error('INVALID_OWNER_PK');
    }

    expect((await aaveToken.allowance(owner, spender)).toString()).to.be.equal(
      '0',
      'INVALID_ALLOWANCE_BEFORE_PERMIT'
    );

    const {v, r, s} = getSignatureFromTypedData(ownerPrivateKey, msgParams);

    await waitForTx(
      await aaveToken
        .connect(users[1].signer)
        .permit(owner, spender, permitAmount, deadline, v, r, s)
    );

    expect((await aaveToken._nonces(owner)).toNumber()).to.be.equal(1);
  });

  it('Cancels the previous permit', async () => {
    const {aaveToken, deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const deadline = MAX_UINT_AMOUNT;
    const nonce = (await aaveToken._nonces(owner)).toNumber();
    const permitAmount = '0';
    const msgParams = buildPermitParams(
      chainId,
      aaveToken.address,
      owner,
      spender,
      nonce,
      deadline,
      permitAmount
    );

    const ownerPrivateKey = require('../test-wallets.js').accounts[0].secretKey;
    if (!ownerPrivateKey) {
      throw new Error('INVALID_OWNER_PK');
    }

    const {v, r, s} = getSignatureFromTypedData(ownerPrivateKey, msgParams);

    expect((await aaveToken.allowance(owner, spender)).toString()).to.be.equal(
      ethers.utils.parseEther('2'),
      'INVALID_ALLOWANCE_BEFORE_PERMIT'
    );

    await waitForTx(
      await aaveToken
        .connect(users[1].signer)
        .permit(owner, spender, permitAmount, deadline, v, r, s)
    );
    expect((await aaveToken.allowance(owner, spender)).toString()).to.be.equal(
      permitAmount,
      'INVALID_ALLOWANCE_AFTER_PERMIT'
    );

    expect((await aaveToken._nonces(owner)).toNumber()).to.be.equal(2);
  });

  it('Tries to submit a permit with invalid nonce', async () => {
    const {aaveToken, deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const deadline = MAX_UINT_AMOUNT;
    const nonce = 1000;
    const permitAmount = '0';
    const msgParams = buildPermitParams(
      chainId,
      aaveToken.address,
      owner,
      spender,
      nonce,
      deadline,
      permitAmount
    );

    const ownerPrivateKey = require('../test-wallets.js').accounts[0].secretKey;
    if (!ownerPrivateKey) {
      throw new Error('INVALID_OWNER_PK');
    }

    const {v, r, s} = getSignatureFromTypedData(ownerPrivateKey, msgParams);

    await expect(
      aaveToken.connect(users[1].signer).permit(owner, spender, permitAmount, deadline, v, r, s)
    ).to.be.revertedWith('INVALID_SIGNATURE');
  });

  it('Tries to submit a permit with invalid expiration (previous to the current block)', async () => {
    const {aaveToken, deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const expiration = '1';
    const nonce = (await aaveToken._nonces(owner)).toNumber();
    const permitAmount = '0';
    const msgParams = buildPermitParams(
      chainId,
      aaveToken.address,
      owner,
      spender,
      nonce,
      expiration,
      permitAmount
    );

    const ownerPrivateKey = require('../test-wallets.js').accounts[0].secretKey;
    if (!ownerPrivateKey) {
      throw new Error('INVALID_OWNER_PK');
    }

    const {v, r, s} = getSignatureFromTypedData(ownerPrivateKey, msgParams);

    await expect(
      aaveToken.connect(users[1].signer).permit(owner, spender, expiration, permitAmount, v, r, s)
    ).to.be.revertedWith('INVALID_EXPIRATION');
  });

  it('Tries to submit a permit with invalid signature', async () => {
    const {aaveToken, deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const deadline = MAX_UINT_AMOUNT;
    const nonce = (await aaveToken._nonces(owner)).toNumber();
    const permitAmount = '0';
    const msgParams = buildPermitParams(
      chainId,
      aaveToken.address,
      owner,
      spender,
      nonce,
      deadline,
      permitAmount
    );

    const ownerPrivateKey = require('../test-wallets.js').accounts[0].secretKey;
    if (!ownerPrivateKey) {
      throw new Error('INVALID_OWNER_PK');
    }

    const {v, r, s} = getSignatureFromTypedData(ownerPrivateKey, msgParams);

    await expect(
      aaveToken
        .connect(users[1].signer)
        .permit(owner, ZERO_ADDRESS, permitAmount, deadline, v, r, s)
    ).to.be.revertedWith('INVALID_SIGNATURE');
  });

  it('Tries to submit a permit with invalid owner', async () => {
    const {aaveToken, deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const expiration = MAX_UINT_AMOUNT;
    const nonce = (await aaveToken._nonces(owner)).toNumber();
    const permitAmount = '0';
    const msgParams = buildPermitParams(
      chainId,
      aaveToken.address,
      owner,
      spender,
      nonce,
      expiration,
      permitAmount
    );

    const ownerPrivateKey = require('../test-wallets.js').accounts[0].secretKey;
    if (!ownerPrivateKey) {
      throw new Error('INVALID_OWNER_PK');
    }

    const {v, r, s} = getSignatureFromTypedData(ownerPrivateKey, msgParams);

    await expect(
      aaveToken
        .connect(users[1].signer)
        .permit(ZERO_ADDRESS, spender, expiration, permitAmount, v, r, s)
    ).to.be.revertedWith('INVALID_OWNER');
  });

  it('Correct snapshotting on double action in the same block', async () => {
    const {aaveToken, deployer, users} = testEnv;

    const doubleTransferHelper = await deployDoubleTransferHelper(aaveToken.address);

    const receiver = users[2].address;

    await waitForTx(
      await aaveToken.transfer(
        doubleTransferHelper.address,
        (await aaveToken.balanceOf(deployer.address)).toString()
      )
    );

    await waitForTx(
      await doubleTransferHelper.doubleSend(
        receiver,
        ethers.utils.parseEther('0.2'),
        ethers.utils.parseEther('0.8')
      )
    );

    const countSnapshotsReceiver = (await aaveToken._countsSnapshots(receiver)).toString();

    const snapshotReceiver = await aaveToken._snapshots(doubleTransferHelper.address, 0);

    const countSnapshotsSender = (
      await aaveToken._countsSnapshots(doubleTransferHelper.address)
    ).toString();

    expect(countSnapshotsSender).to.be.equal('2', 'INVALID_COUNT_SNAPSHOTS_SENDER');
    const snapshotsSender = [
      await aaveToken._snapshots(doubleTransferHelper.address, 0),
      await aaveToken._snapshots(doubleTransferHelper.address, 1),
    ];

    expect(snapshotsSender[0].value.toString()).to.be.equal(
      ethers.utils.parseEther('1'),
      'INVALID_SENDER_SNAPSHOT'
    );
    expect(snapshotsSender[1].value.toString()).to.be.equal(
      ethers.utils.parseEther('0'),
      'INVALID_SENDER_SNAPSHOT'
    );

    expect(countSnapshotsReceiver).to.be.equal('1', 'INVALID_COUNT_SNAPSHOTS_RECEIVER');
    expect(snapshotReceiver.value.toString()).to.be.equal(ethers.utils.parseEther('1'));
  });

  it('Emits correctly mock event of the _beforeTokenTransfer hook', async () => {
    const {aaveToken, mockTransferHook, users} = testEnv;

    const recipient = users[2].address;

    await expect(aaveToken.connect(users[1].signer).transfer(recipient, 1)).to.emit(
      mockTransferHook,
      'MockHookEvent'
    );
  });

  it("Don't record snapshot when sending funds to itself", async () => {
    const {aaveToken, deployer, users} = testEnv;
    const from = users[2].address;
    const to = from;
    await waitForTx(
      await aaveToken.connect(users[2].signer).transfer(to, ethers.utils.parseEther('1'))
    );
    const fromCountOfSnapshots = await aaveToken._countsSnapshots(from);
    const fromLastSnapshot = await aaveToken._snapshots(from, fromCountOfSnapshots.sub(1));
    const fromPreviousSnapshot = await aaveToken._snapshots(from, fromCountOfSnapshots.sub(2));

    const toCountOfSnapshots = await aaveToken._countsSnapshots(to);
    const toSnapshot = await aaveToken._snapshots(to, toCountOfSnapshots.sub(1));

    expect(fromCountOfSnapshots.toString()).to.be.equal('2', 'INVALID_SNAPSHOT_COUNT');
    expect(fromLastSnapshot.value.toString()).to.be.equal(
      '1000000000000000001',
      'INVALID_SNAPSHOT_VALUE'
    );
    expect(fromPreviousSnapshot.value.toString()).to.be.equal(
      ethers.utils.parseEther('1'),
      'INVALID_SNAPSHOT_VALUE'
    );

    expect(toCountOfSnapshots.toString()).to.be.equal('2', 'INVALID_SNAPSHOT_COUNT');
    expect(toSnapshot.value.toString()).to.be.equal(
      '1000000000000000001',
      'INVALID_SNAPSHOT_VALUE'
    );
  });
});
