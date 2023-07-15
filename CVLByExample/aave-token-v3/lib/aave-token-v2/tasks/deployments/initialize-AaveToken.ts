import {task} from 'hardhat/config';
import {eContractid} from '../../helpers/types';
import {
  getAaveToken,
  getLendToAaveMigrator,
  getAaveTokenImpl,
  getContract,
} from '../../helpers/contracts-helpers';
import {waitForTx} from '../../helpers/misc-utils';
import {ZERO_ADDRESS} from '../../helpers/constants';
import {InitializableAdminUpgradeabilityProxy} from '../../types/InitializableAdminUpgradeabilityProxy';

const {AaveToken} = eContractid;

task(`initialize-${AaveToken}`, `Initialize the ${AaveToken} proxy contract`)
  .addParam('admin', `The address to be added as an Admin role in ${AaveToken} Transparent Proxy.`)
  .addFlag('onlyProxy', 'Initialize only the proxy contract, not the implementation contract')
  .setAction(async ({admin: aaveAdmin, onlyProxy}, localBRE) => {
    await localBRE.run('set-dre');

    if (!aaveAdmin) {
      throw new Error(
        `Missing --admin parameter to add the Admin Role to ${AaveToken} Transparent Proxy`
      );
    }

    if (!localBRE.network.config.chainId) {
      throw new Error('INVALID_CHAIN_ID');
    }

    console.log(`\n- ${AaveToken} initialization`);

    const aaveTokenImpl = await getAaveTokenImpl();
    const aaveToken = await getAaveToken();
    const lendToAaveMigratorProxy = await getLendToAaveMigrator();

    const aaveTokenProxy = await getContract<InitializableAdminUpgradeabilityProxy>(
      eContractid.InitializableAdminUpgradeabilityProxy,
      aaveToken.address
    );

    if (onlyProxy) {
      console.log(
        `\tWARNING: Not initializing the ${AaveToken} implementation, only set AAVE_ADMIN to Transparent Proxy contract.`
      );
      await waitForTx(await aaveTokenProxy.initialize(aaveTokenImpl.address, aaveAdmin, '0x'));
      console.log(
        `\tFinished ${AaveToken} Proxy initialization, but not ${AaveToken} implementation.`
      );
      return;
    }

    console.log('\tInitializing Aave Token and Transparent Proxy');
    // If any other testnet, initialize for development purposes
    const aaveTokenEncodedInitialize = aaveTokenImpl.interface.encodeFunctionData('initialize', [
      lendToAaveMigratorProxy.address,
      aaveAdmin,
      ZERO_ADDRESS,
    ]);

    await waitForTx(
      await aaveTokenProxy.initialize(aaveTokenImpl.address, aaveAdmin, aaveTokenEncodedInitialize)
    );

    console.log('\tFinished Aave Token and Transparent Proxy initialization');
  });
