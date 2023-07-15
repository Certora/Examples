import {task} from 'hardhat/config';
import {eContractid} from '../../helpers/types';
import {
  getLendToAaveMigratorImpl,
  getContract,
  getLendToAaveMigrator,
} from '../../helpers/contracts-helpers';
import {waitForTx} from '../../helpers/misc-utils';

const {LendToAaveMigrator} = eContractid;

task(`initialize-${LendToAaveMigrator}`, `Initialize the ${LendToAaveMigrator} proxy contract`)
  .addParam('admin', 'The address to be added as an Admin role in Aave Token Transparent Proxy.')
  .addFlag('onlyProxy', 'Initialize only the proxy contract, not the implementation contract')
  .setAction(async ({admin: aaveAdmin, onlyProxy}, localBRE) => {
    await localBRE.run('set-dre');

    if (!aaveAdmin) {
      throw new Error(
        `Missing --admin parameter to add the Admin Role to ${LendToAaveMigrator} Transparent Proxy`
      );
    }

    if (!localBRE.network.config.chainId) {
      throw new Error('INVALID_CHAIN_ID');
    }

    console.log(`\n- ${LendToAaveMigrator} initialization`);

    const lendToAaveMigratorImpl = await getLendToAaveMigratorImpl();
    const lendToAaveMigrator = await getLendToAaveMigrator();

    const lendToAaveMigratorProxy = await getContract(
      eContractid.InitializableAdminUpgradeabilityProxy,
      lendToAaveMigrator.address
    );

    const lendToAaveMigratorInitializeEncoded = lendToAaveMigratorImpl.interface.encodeFunctionData(
      'initialize'
    );

    if (onlyProxy) {
      console.log(
        `\tWARNING: Not initializing the ${LendToAaveMigrator} implementation, only set AAVE_ADMIN to Transparent Proxy contract.`
      );
      await waitForTx(
        await lendToAaveMigratorProxy.initialize(lendToAaveMigratorImpl.address, aaveAdmin, '0x')
      );
      console.log(
        `\tFinished ${LendToAaveMigrator} Proxy initialization, but not ${LendToAaveMigrator} implementation.`
      );
      return;
    }

    console.log('\tInitializing LendToAaveMigrator Proxy and Implementation ');

    await waitForTx(
      await lendToAaveMigratorProxy.initialize(
        lendToAaveMigratorImpl.address,
        aaveAdmin,
        lendToAaveMigratorInitializeEncoded
      )
    );

    console.log('\tFinished LendToAaveMigrator Proxy and Implementation initialization.');
  });
