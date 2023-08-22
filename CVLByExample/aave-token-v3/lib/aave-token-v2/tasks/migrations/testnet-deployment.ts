import {task} from 'hardhat/config';
import {HardhatRuntimeEnvironment} from 'hardhat/types';

import {eContractid} from '../../helpers/types';
import {eEthereumNetwork} from '../../helpers/types-common';
import {getAaveAdminPerNetwork, getLendTokenPerNetwork} from '../../helpers/constants';
import {checkVerification} from '../../helpers/etherscan-verification';

task('testnet-deployment', 'Deployment in mainnet network')
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

    await DRE.run(`initialize-${eContractid.AaveToken}`, {
      admin: aaveAdmin,
      onlyProxy: true,
    });

    await DRE.run(`initialize-${eContractid.LendToAaveMigrator}`, {
      admin: aaveAdmin,
      onlyProxy: true,
    });

    console.log('\n✔️  Finished the deployment of the Aave Token Testnet Enviroment. ✔️');
  });
