import {fail} from 'assert';
import {ethers} from 'ethers';
import BigNumber from 'bignumber.js';
import {TestEnv, makeSuite} from './helpers/make-suite';
import {eContractid, ProtocolErrors} from '../helpers/types';
import {eEthereumNetwork} from '../helpers/types-common';
import {waitForTx, DRE} from '../helpers/misc-utils';
import {
  getInitializableAdminUpgradeabilityProxy,
  buildPermitParams,
  getSignatureFromTypedData,
  deployDoubleTransferHelper,
  deployAaveTokenV2,
  getContract,
} from '../helpers/contracts-helpers';
import {
  ZERO_ADDRESS,
  MAX_UINT_AMOUNT,
  getAaveTokenDomainSeparatorPerNetwork,
} from '../helpers/constants';
import {AaveTokenV2} from '../types/AaveTokenV2';
import {parseEther} from 'ethers/lib/utils';

const {expect} = require('chai');

makeSuite('AAVE token V2', (testEnv: TestEnv) => {
  let aaveTokenV2: AaveTokenV2;

  it('Updates the implementation of the AAVE token to V2', async () => {
    const {aaveToken, users} = testEnv;

    //getting the proxy contract from the aave token address
    const aaveTokenProxy = await getContract(
      eContractid.InitializableAdminUpgradeabilityProxy,
      aaveToken.address
    );

    const AAVEv2 = await deployAaveTokenV2();

    const encodedIntialize = AAVEv2.interface.encodeFunctionData('initialize');

    await aaveTokenProxy
      .connect(users[0].signer)
      .upgradeToAndCall(AAVEv2.address, encodedIntialize);

    aaveTokenV2 = await getContract(eContractid.AaveTokenV2, aaveTokenProxy.address);
  });

  it('Checks initial configuration', async () => {
    expect(await aaveTokenV2.name()).to.be.equal('Aave Token', 'Invalid token name');

    expect(await aaveTokenV2.symbol()).to.be.equal('AAVE', 'Invalid token symbol');

    expect((await aaveTokenV2.decimals()).toString()).to.be.equal('18', 'Invalid token decimals');
  });

  it('Checks the domain separator', async () => {
    const network = DRE.network.name;
    const DOMAIN_SEPARATOR_ENCODED = getAaveTokenDomainSeparatorPerNetwork(
      network as eEthereumNetwork
    );

    const separator = await aaveTokenV2.DOMAIN_SEPARATOR();
    expect(separator).to.be.equal(DOMAIN_SEPARATOR_ENCODED, 'Invalid domain separator');
  });

  it('Checks the revision', async () => {
    const revision = await aaveTokenV2.REVISION();

    expect(revision.toString()).to.be.equal('2', 'Invalid revision');
  });

  it('Checks the allocation of the initial AAVE supply', async () => {
    const expectedMigratorBalance = new BigNumber(13000000).times(new BigNumber(10).pow(18));
    const expectedlDistributorBalance = new BigNumber(3000000).times(new BigNumber(10).pow(18));
    const {lendToAaveMigrator} = testEnv;
    const migratorBalance = await aaveTokenV2.balanceOf(lendToAaveMigrator.address);
    const distributorBalance = await aaveTokenV2.balanceOf(testEnv.users[0].address);

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

  it('Reverts submitting a permit with 0 expiration', async () => {
    const {deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const expiration = 0;
    const nonce = (await aaveTokenV2._nonces(owner)).toNumber();
    const permitAmount = ethers.utils.parseEther('2').toString();
    const msgParams = buildPermitParams(
      chainId,
      aaveTokenV2.address,
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

    expect((await aaveTokenV2.allowance(owner, spender)).toString()).to.be.equal(
      '0',
      'INVALID_ALLOWANCE_BEFORE_PERMIT'
    );

    const {v, r, s} = getSignatureFromTypedData(ownerPrivateKey, msgParams);

    await expect(
      aaveTokenV2.connect(users[1].signer).permit(owner, spender, permitAmount, expiration, v, r, s)
    ).to.be.revertedWith('INVALID_EXPIRATION');

    expect((await aaveTokenV2.allowance(owner, spender)).toString()).to.be.equal(
      '0',
      'INVALID_ALLOWANCE_AFTER_PERMIT'
    );
  });

  it('Submits a permit with maximum expiration length', async () => {
    const {deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    const configChainId = DRE.network.config.chainId;
    expect(configChainId).to.be.equal(chainId);
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const deadline = MAX_UINT_AMOUNT;
    const nonce = (await aaveTokenV2._nonces(owner)).toNumber();
    const permitAmount = ethers.utils.parseEther('2').toString();
    const msgParams = buildPermitParams(
      chainId,
      aaveTokenV2.address,
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

    expect((await aaveTokenV2.allowance(owner, spender)).toString()).to.be.equal(
      '0',
      'INVALID_ALLOWANCE_BEFORE_PERMIT'
    );

    const {v, r, s} = getSignatureFromTypedData(ownerPrivateKey, msgParams);

    await waitForTx(
      await aaveTokenV2
        .connect(users[1].signer)
        .permit(owner, spender, permitAmount, deadline, v, r, s)
    );

    expect((await aaveTokenV2._nonces(owner)).toNumber()).to.be.equal(1);
  });

  it('Cancels the previous permit', async () => {
    const {deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const deadline = MAX_UINT_AMOUNT;
    const nonce = (await aaveTokenV2._nonces(owner)).toNumber();
    const permitAmount = '0';
    const msgParams = buildPermitParams(
      chainId,
      aaveTokenV2.address,
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

    expect((await aaveTokenV2.allowance(owner, spender)).toString()).to.be.equal(
      ethers.utils.parseEther('2'),
      'INVALID_ALLOWANCE_BEFORE_PERMIT'
    );

    await waitForTx(
      await aaveTokenV2
        .connect(users[1].signer)
        .permit(owner, spender, permitAmount, deadline, v, r, s)
    );
    expect((await aaveTokenV2.allowance(owner, spender)).toString()).to.be.equal(
      permitAmount,
      'INVALID_ALLOWANCE_AFTER_PERMIT'
    );

    expect((await aaveTokenV2._nonces(owner)).toNumber()).to.be.equal(2);
  });

  it('Tries to submit a permit with invalid nonce', async () => {
    const {deployer, users} = testEnv;
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
      aaveTokenV2.address,
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
      aaveTokenV2.connect(users[1].signer).permit(owner, spender, permitAmount, deadline, v, r, s)
    ).to.be.revertedWith('INVALID_SIGNATURE');
  });

  it('Tries to submit a permit with invalid expiration (previous to the current block)', async () => {
    const {deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const expiration = '1';
    const nonce = (await aaveTokenV2._nonces(owner)).toNumber();
    const permitAmount = '0';
    const msgParams = buildPermitParams(
      chainId,
      aaveTokenV2.address,
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
      aaveTokenV2.connect(users[1].signer).permit(owner, spender, expiration, permitAmount, v, r, s)
    ).to.be.revertedWith('INVALID_EXPIRATION');
  });

  it('Tries to submit a permit with invalid signature', async () => {
    const {deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const deadline = MAX_UINT_AMOUNT;
    const nonce = (await aaveTokenV2._nonces(owner)).toNumber();
    const permitAmount = '0';
    const msgParams = buildPermitParams(
      chainId,
      aaveTokenV2.address,
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
      aaveTokenV2
        .connect(users[1].signer)
        .permit(owner, ZERO_ADDRESS, permitAmount, deadline, v, r, s)
    ).to.be.revertedWith('INVALID_SIGNATURE');
  });

  it('Tries to submit a permit with invalid owner', async () => {
    const {deployer, users} = testEnv;
    const owner = deployer.address;
    const spender = users[1].address;

    const {chainId} = await DRE.ethers.provider.getNetwork();
    if (!chainId) {
      fail("Current network doesn't have CHAIN ID");
    }
    const expiration = MAX_UINT_AMOUNT;
    const nonce = (await aaveTokenV2._nonces(owner)).toNumber();
    const permitAmount = '0';
    const msgParams = buildPermitParams(
      chainId,
      aaveTokenV2.address,
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
      aaveTokenV2
        .connect(users[1].signer)
        .permit(ZERO_ADDRESS, spender, expiration, permitAmount, v, r, s)
    ).to.be.revertedWith('INVALID_OWNER');
  });

  it('Checks the total supply', async () => {
    const totalSupply = await aaveTokenV2.totalSupplyAt('0'); // Supply remains constant due no more mints
    expect(totalSupply).equal(parseEther('16000000'));
  });
});
