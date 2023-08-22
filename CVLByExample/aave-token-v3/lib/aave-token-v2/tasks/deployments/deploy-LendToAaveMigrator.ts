import {task} from 'hardhat/config';
import {eContractid} from '../../helpers/types';
import {
  registerContractInJsonDb,
  deployLendToAaveMigrator,
  deployInitializableAdminUpgradeabilityProxy,
  getAaveToken,
  getLendToken,
  deployMintableErc20,
} from '../../helpers/contracts-helpers';
import {verify} from 'crypto';

const {LendToAaveMigrator, LendToAaveMigratorImpl, MintableErc20} = eContractid;

task(`deploy-${LendToAaveMigrator}`, `Deploys ${LendToAaveMigrator} contract`)
  .addOptionalParam(
    'lendTokenAddress',
    'The address of the LEND token. If not set, a mocked Mintable token will be deployed.'
  )
  .addFlag('verify', 'Proceed with the Etherscan verification')
  .setAction(async ({lendTokenAddress, verify}, localBRE) => {
    await localBRE.run('set-dre');

    if (!localBRE.network.config.chainId) {
      throw new Error('INVALID_CHAIN_ID');
    }

    console.log(`\n- ${LendToAaveMigrator} deployment`);

    if (!lendTokenAddress) {
      console.log(`\tDeploying ${MintableErc20} to mock LEND token...`);
      const mockedLend = await deployMintableErc20(['LEND token', 'LEND', 18]);
      await mockedLend.deployTransaction.wait();
    }

    const aaveTokenProxy = await getAaveToken();
    const lendToken = lendTokenAddress || (await getLendToken()).address;

    console.log(`\tUsing ${lendToken} address for Lend Token input parameter`);

    console.log(`\tDeploying ${LendToAaveMigrator} Implementation...`);

    const constructorParameters: [string, string, string] = [
      aaveTokenProxy.address,
      lendToken,
      '100',
    ];
    const lendToAaveMigratorImpl = await deployLendToAaveMigrator(constructorParameters, verify);
    await registerContractInJsonDb(LendToAaveMigratorImpl, lendToAaveMigratorImpl);

    console.log(`\tDeploying ${LendToAaveMigrator} Transparent Proxy...`);

    const lendToAaveMigratorProxy = await deployInitializableAdminUpgradeabilityProxy(verify);
    await registerContractInJsonDb(LendToAaveMigrator, lendToAaveMigratorProxy);

    console.log(`\tFinished ${LendToAaveMigrator} proxy and implementation deployment`);
  });
