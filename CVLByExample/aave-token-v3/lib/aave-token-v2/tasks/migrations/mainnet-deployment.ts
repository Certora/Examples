import {task} from 'hardhat/config';
import {HardhatRuntimeEnvironment} from 'hardhat/types';

import {eEthereumNetwork} from '../../helpers/types-common';
import {eContractid} from '../../helpers/types';
import {checkVerification} from '../../helpers/etherscan-verification';
import {getAaveAdminPerNetwork, getLendTokenPerNetwork} from '../../helpers/constants';

task('main-deployment', 'Deployment in mainnet network')
  .addFlag(
    'verify',
    'Verify AaveToken, LendToAaveMigrator, and InitializableAdminUpgradeabilityProxy contract.'
  )
  .setAction(async ({verify}, localBRE) => {
    const DRE: HardhatRuntimeEnvironment = await localBRE.run('set-dre');
    const network = DRE.network.name as eEthereumNetwork;
    const aaveAdmin = getAaveAdminPerNetwork(network);
    const lendTokenAddress = getLendTokenPerNetwork(network);

    if (!aaveAdmin) {
      throw Error(
        'The --admin parameter must be set for mainnet network. Set an Ethereum address as --admin parameter input.'
      );
    }

    // If Etherscan verification is enabled, check needed enviroments to prevent loss of gas in failed deployments.
    if (verify) {
      checkVerification();
    }

    console.log('AAVE ADMIN', aaveAdmin);
    await DRE.run(`deploy-${eContractid.AaveToken}`, {verify});

    await DRE.run(`deploy-${eContractid.LendToAaveMigrator}`, {
      lendTokenAddress,
      verify,
    });

    // The task will only initialize the proxy contract, not implementation
    await DRE.run(`initialize-${eContractid.AaveToken}`, {
      admin: aaveAdmin,
      onlyProxy: true,
    });

    // The task will only initialize the proxy contract, not implementation
    await DRE.run(`initialize-${eContractid.LendToAaveMigrator}`, {
      admin: aaveAdmin,
      onlyProxy: true,
    });

    console.log('\n✔️ Finished the deployment of the Aave Token Mainnet Enviroment. ✔️');
  });
