import {task} from 'hardhat/config';
import {eContractid} from '../../helpers/types';
import {
  registerContractInJsonDb,
  deployAaveToken,
  deployInitializableAdminUpgradeabilityProxy,
  deployAaveTokenV2,
} from '../../helpers/contracts-helpers';

const {AaveTokenV2, AaveTokenImpl} = eContractid;

task(`deploy-${AaveTokenV2}`, `Deploys the ${AaveTokenV2} contract`)
  .addFlag('verify', 'Proceed with the Etherscan verification')
  .setAction(async ({verify}, localBRE) => {
    await localBRE.run('set-dre');

    if (!localBRE.network.config.chainId) {
      throw new Error('INVALID_CHAIN_ID');
    }

    console.log(`\n- ${AaveTokenV2} deployment`);

    console.log(`\tDeploying ${AaveTokenV2} implementation ...`);
    const aaveTokenImpl = await deployAaveTokenV2(verify);
    await registerContractInJsonDb(AaveTokenImpl, aaveTokenImpl);

    console.log(`\tFinished ${AaveTokenV2} proxy and implementation deployment`);
  });
