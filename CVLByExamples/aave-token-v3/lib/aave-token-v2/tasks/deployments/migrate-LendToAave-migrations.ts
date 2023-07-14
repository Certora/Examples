import {task} from 'hardhat/config';
import BigNumber from 'bignumber.js';
import {
  getLendToAaveMigrator,
  getLendToken,
  getEthersSigners,
} from '../../helpers/contracts-helpers';

task(`Lend-Migration`, `Create migration to test the contracts`).setAction(async (_, localBRE) => {
  console.log(`\n- Lend Migration started`);
  await localBRE.run('set-dre');

  if (!localBRE.network.config.chainId) {
    throw new Error('INVALID_CHAIN_ID');
  }

  const [, , user1, user2] = await getEthersSigners();

  const mockLend = await getLendToken();
  const lendToAaveMigrator = await getLendToAaveMigrator();

  const lendAmount = 1000;
  const lendTokenAmount = new BigNumber(lendAmount).times(new BigNumber(10).pow(18)).toFixed(0);
  const halfLendTokenAmount = new BigNumber(lendAmount / 2)
    .times(new BigNumber(10).pow(18))
    .toFixed(0);

  await mockLend.connect(user1).mint(lendTokenAmount);
  await mockLend.connect(user2).mint(lendTokenAmount);

  await mockLend.connect(user1).approve(lendToAaveMigrator.address, lendTokenAmount);
  await mockLend.connect(user2).approve(lendToAaveMigrator.address, lendTokenAmount);

  await lendToAaveMigrator.connect(user1).migrateFromLEND(halfLendTokenAmount);
  await lendToAaveMigrator.connect(user1).migrateFromLEND(halfLendTokenAmount);
  await lendToAaveMigrator.connect(user2).migrateFromLEND(lendTokenAmount);

  console.log(`\n- Finished migrating lend balances`);
});
