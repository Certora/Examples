import rawBRE from 'hardhat';
import {expect} from 'chai';
import {TestEnv, makeSuite} from './helpers/make-suite';
import {ProtocolErrors, eContractid} from '../helpers/types';
import {getContract} from '../helpers/contracts-helpers';
import BigNumber from 'bignumber.js';

makeSuite('LEND migrator', (testEnv: TestEnv) => {
  const {} = ProtocolErrors;

  it('Check the constructor is executed properly', async () => {
    const {lendToAaveMigrator, aaveToken, lendToken} = testEnv;

    expect(await lendToAaveMigrator.AAVE()).to.be.equal(aaveToken.address, 'Invalid AAVE Address');

    expect(await lendToAaveMigrator.LEND()).to.be.equal(lendToken.address, 'Invalid LEND address');

    expect(await lendToAaveMigrator.LEND_AAVE_RATIO()).to.be.equal('1000', 'Invalid ratio');
  });

  it("Check migration isn't started", async () => {
    const {lendToAaveMigrator, lendToAaveMigratorImpl} = testEnv;

    const migrationStarted = await lendToAaveMigrator.migrationStarted();

    expect(migrationStarted.toString()).to.be.eq('false');
    await expect(lendToAaveMigrator.migrateFromLEND('1000')).to.be.revertedWith(
      'MIGRATION_NOT_STARTED'
    );
  });

  it('Starts the migration', async () => {
    const {lendToAaveMigrator, lendToAaveMigratorImpl} = testEnv;

    const lendToAaveMigratorInitializeEncoded = lendToAaveMigratorImpl.interface.encodeFunctionData(
      'initialize'
    );

    const migratorAsProxy = await getContract(
      eContractid.InitializableAdminUpgradeabilityProxy,
      lendToAaveMigrator.address
    );

    await migratorAsProxy
      .connect(testEnv.users[0].signer)
      .upgradeToAndCall(lendToAaveMigratorImpl.address, lendToAaveMigratorInitializeEncoded);

    const migrationStarted = await lendToAaveMigrator.migrationStarted();

    expect(migrationStarted.toString()).to.be.eq('true');
  });

  it('Migrates 1000 LEND', async () => {
    const {lendToAaveMigrator, lendToken, aaveToken} = testEnv;
    const user = testEnv.users[2];

    const lendBalance = new BigNumber(1000).times(new BigNumber(10).pow(18)).toFixed(0);
    const expectedAaveBalanceAfterMigration = new BigNumber(10).pow(18);

    await lendToken.connect(user.signer).mint(lendBalance);

    await lendToken.connect(user.signer).approve(lendToAaveMigrator.address, lendBalance);

    await lendToAaveMigrator.connect(user.signer).migrateFromLEND(lendBalance);

    const lendBalanceAfterMigration = await lendToken.balanceOf(user.address);
    const aaveBalanceAfterMigration = await aaveToken.balanceOf(user.address);

    expect(lendBalanceAfterMigration.toString()).to.be.eq('0');
    expect(aaveBalanceAfterMigration.toString()).to.be.eq(
      expectedAaveBalanceAfterMigration.toFixed(0)
    );
  });
});
