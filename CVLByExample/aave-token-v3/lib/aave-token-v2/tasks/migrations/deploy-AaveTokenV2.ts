import {task} from 'hardhat/config';
import {HardhatRuntimeEnvironment} from 'hardhat/types';

import {eEthereumNetwork} from '../../helpers/types-common';
import {eContractid} from '../../helpers/types';
import {checkVerification} from '../../helpers/etherscan-verification';
import {getAaveAdminPerNetwork, getLendTokenPerNetwork} from '../../helpers/constants';

task('deploy-v2', 'Deployment of the Aave token V2')
  .addFlag(
    'verify',
    'Verify AaveTokenV2 contract.'
  )
  .setAction(async ({verify}, localBRE) => {
    const DRE: HardhatRuntimeEnvironment = await localBRE.run('set-dre');
    const network = DRE.network.name as eEthereumNetwork;
    const aaveAdmin = getAaveAdminPerNetwork(network);

    if (!aaveAdmin) {
      throw Error(
        'The --admin parameter must be set for mainnet network. Set an Ethereum address as --admin parameter input.'
      );
    }

    // If Etherscan verification is enabled, check needed environments to prevent loss of gas in failed deployments.
    if (verify) {
      checkVerification();
    }

    await DRE.run(`deploy-${eContractid.AaveTokenV2}`, {verify});

    console.log('\n✔️ Finished the deployment of the Aave Token V2 Mainnet Environment. ✔️');
  });
