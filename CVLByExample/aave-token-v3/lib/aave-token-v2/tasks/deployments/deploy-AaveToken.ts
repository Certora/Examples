import {task} from 'hardhat/config';
import {eContractid} from '../../helpers/types';
import {
  registerContractInJsonDb,
  deployAaveToken,
  deployInitializableAdminUpgradeabilityProxy,
} from '../../helpers/contracts-helpers';

const {AaveToken, AaveTokenImpl} = eContractid;

task(`deploy-${AaveToken}`, `Deploys the ${AaveToken} contract`)
  .addFlag('verify', 'Proceed with the Etherscan verification')
  .setAction(async ({verify}, localBRE) => {
    await localBRE.run('set-dre');

    if (!localBRE.network.config.chainId) {
      throw new Error('INVALID_CHAIN_ID');
    }

    console.log(`\n- ${AaveToken} deployment`);

    console.log(`\tDeploying ${AaveToken} implementation ...`);
    const aaveTokenImpl = await deployAaveToken(verify);
    await registerContractInJsonDb(AaveTokenImpl, aaveTokenImpl);

    console.log(`\tDeploying ${AaveToken} Transparent Proxy ...`);
    const aaveTokenProxy = await deployInitializableAdminUpgradeabilityProxy(verify);
    await registerContractInJsonDb(AaveToken, aaveTokenProxy);

    console.log(`\tFinished ${AaveToken} proxy and implementation deployment`);
  });
