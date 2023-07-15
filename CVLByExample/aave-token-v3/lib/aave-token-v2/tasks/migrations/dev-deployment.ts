import {task} from 'hardhat/config';
import {HardhatRuntimeEnvironment} from 'hardhat/types';

import {eContractid} from '../../helpers/types';
import {getEthersSigners} from '../../helpers/contracts-helpers';
import {checkVerification} from '../../helpers/etherscan-verification';

task('dev-deployment', 'Deployment in hardhat')
  .addOptionalParam(
    'admin',
    `The address to be added as an Admin role in Aave Token and LendToAaveMigrator Transparent Proxies.`
  )
  .addOptionalParam('lendTokenAddress', 'The address of the LEND token smart contract.')
  .addFlag(
    'verify',
    'Verify AaveToken, LendToAaveMigrator, and InitializableAdminUpgradeabilityProxy contract.'
  )
  .setAction(async ({admin, lendTokenAddress, verify}, localBRE) => {
    const DRE: HardhatRuntimeEnvironment = await localBRE.run('set-dre');

    // If admin parameter is NOT set, the Aave Admin will be the
    // second account provided via buidler config.
    const [, secondaryWallet] = await getEthersSigners();
    const aaveAdmin = admin || (await secondaryWallet.getAddress());

    console.log('AAVE ADMIN', aaveAdmin);

    // If Etherscan verification is enabled, check needed enviroments to prevent loss of gas in failed deployments.
    if (verify) {
      checkVerification();
    }

    await DRE.run(`deploy-${eContractid.AaveToken}`, {verify});

    await DRE.run(`deploy-${eContractid.LendToAaveMigrator}`, {
      lendTokenAddress,
      verify,
    });

    await DRE.run(`initialize-${eContractid.AaveToken}`, {
      admin: aaveAdmin,
    });

    await DRE.run(`initialize-${eContractid.LendToAaveMigrator}`, {
      admin: aaveAdmin,
    });

    await DRE.run(`Lend-Migration`, {});

    console.log('\n👷 Finished the deployment of the Aave Token Development Enviroment. 👷');
  });
