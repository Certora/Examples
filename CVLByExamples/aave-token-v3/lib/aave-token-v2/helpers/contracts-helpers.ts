import {Contract, Signer, utils, ethers} from 'ethers';

import {getDb, DRE, waitForTx} from './misc-utils';
import {tEthereumAddress, eContractid, tStringTokenSmallUnits} from './types';
import {Artifact} from 'hardhat/types';
import {MOCK_ETH_ADDRESS, SUPPORTED_ETHERSCAN_NETWORKS} from './constants';
import BigNumber from 'bignumber.js';
import {Ierc20Detailed} from '../types/Ierc20Detailed';
import {InitializableAdminUpgradeabilityProxy} from '../types/InitializableAdminUpgradeabilityProxy';
import {MintableErc20} from '../types/MintableErc20';
import {signTypedData_v4, TypedData} from 'eth-sig-util';
import {fromRpcSig, ECDSASignature} from 'ethereumjs-util';
import {DoubleTransferHelper} from '../types/DoubleTransferHelper';
import {MockTransferHook} from '../types/MockTransferHook';
import {verifyContract} from './etherscan-verification';
import {AaveToken} from '../types/AaveToken';
import {AaveTokenV2} from '../types/AaveTokenV2';
import {LendToAaveMigrator} from '../types/LendToAaveMigrator';

export const registerContractInJsonDb = async (contractId: string, contractInstance: Contract) => {
  const currentNetwork = DRE.network.name;
  if (currentNetwork !== 'hardhat' && currentNetwork !== 'coverage') {
    console.log(`\n\t  *** ${contractId} ***\n`);
    console.log(`\t  Network: ${currentNetwork}`);
    console.log(`\t  tx: ${contractInstance.deployTransaction.hash}`);
    console.log(`\t  contract address: ${contractInstance.address}`);
    console.log(`\t  deployer address: ${contractInstance.deployTransaction.from}`);
    console.log(`\t  gas price: ${contractInstance.deployTransaction.gasPrice}`);
    console.log(`\t  gas used: ${contractInstance.deployTransaction.gasLimit}`);
    console.log(`\t  ******`);
    console.log();
  }

  await getDb()
    .set(`${contractId}.${currentNetwork}`, {
      address: contractInstance.address,
      deployer: contractInstance.deployTransaction.from,
    })
    .write();
};

export const insertContractAddressInDb = async (id: eContractid, address: tEthereumAddress) =>
  await getDb()
    .set(`${id}.${DRE.network.name}`, {
      address,
    })
    .write();

export const getEthersSigners = async (): Promise<Signer[]> =>
  await Promise.all(await DRE.ethers.getSigners());

export const getEthersSignersAddresses = async (): Promise<tEthereumAddress[]> =>
  await Promise.all((await DRE.ethers.getSigners()).map((signer) => signer.getAddress()));

export const getCurrentBlock = async () => {
  return DRE.ethers.provider.getBlockNumber();
};

export const decodeAbiNumber = (data: string): number =>
  parseInt(utils.defaultAbiCoder.decode(['uint256'], data).toString());

const deployContract = async <ContractType extends Contract>(
  contractName: string,
  args: any[]
): Promise<ContractType> => {
  const contract = (await (await DRE.ethers.getContractFactory(contractName)).deploy(
    ...args
  )) as ContractType;
  await waitForTx(contract.deployTransaction);
  await registerContractInJsonDb(<eContractid>contractName, contract);
  return contract;
};

export const getContract = async <ContractType extends Contract>(
  contractName: string,
  address: string
): Promise<ContractType> => (await DRE.ethers.getContractAt(contractName, address)) as ContractType;

export const deployAaveToken = async (verify?: boolean) => {
  const id = eContractid.AaveToken;
  const args: string[] = [];
  const instance = await deployContract<AaveToken>(id, args);
  await instance.deployTransaction.wait();
  if (verify) {
    await verifyContract(id, instance.address, args);
  }
  return instance;
};

export const deployAaveTokenV2 = async (verify?: boolean): Promise<AaveTokenV2> => {
  const id = eContractid.AaveTokenV2;
  const args: string[] = [];
  const instance = await deployContract<AaveTokenV2>(id, args);
  await instance.deployTransaction.wait();
  if (verify) {
    await verifyContract(id, instance.address, args);
  }
  return instance;
};

export const deployLendToAaveMigrator = async (
  [aaveToken, lendToken, aaveLendRatio]: [tEthereumAddress, tEthereumAddress, string],
  verify?: boolean
) => {
  const id = eContractid.LendToAaveMigrator;
  const args: string[] = [aaveToken, lendToken, aaveLendRatio];
  const instance = await deployContract<any>(id, args);
  await instance.deployTransaction.wait();
  if (verify) {
    await verifyContract(id, instance.address, args);
  }
  return instance;
};

export const deployMintableErc20 = async ([name, symbol, decimals]: [string, string, number]) =>
  await deployContract<MintableErc20>(eContractid.MintableErc20, [name, symbol, decimals]);

export const deployDoubleTransferHelper = async (aaveToken: tEthereumAddress, verify?: boolean) => {
  const id = eContractid.DoubleTransferHelper;
  const args = [aaveToken];
  const instance = await deployContract<DoubleTransferHelper>(id, args);
  await instance.deployTransaction.wait();
  if (verify) {
    await verifyContract(id, instance.address, args);
  }
  return instance;
};

export const deployMockTransferHook = async () =>
  await deployContract<MockTransferHook>(eContractid.MockTransferHook, []);

export const deployInitializableAdminUpgradeabilityProxy = async (verify?: boolean) => {
  const id = eContractid.InitializableAdminUpgradeabilityProxy;
  const args: string[] = [];
  const instance = await deployContract<InitializableAdminUpgradeabilityProxy>(id, args);
  await instance.deployTransaction.wait();
  if (verify) {
    await verifyContract(id, instance.address, args);
  }
  return instance;
};

export const getAaveToken = async (address?: tEthereumAddress) => {
  return await getContract<AaveToken>(
    eContractid.AaveToken,
    address || (await getDb().get(`${eContractid.AaveToken}.${DRE.network.name}`).value()).address
  );
};

export const getAaveTokenImpl = async (address?: tEthereumAddress) => {
  return await getContract<AaveToken>(
    eContractid.AaveToken,
    address ||
      (await getDb().get(`${eContractid.AaveTokenImpl}.${DRE.network.name}`).value()).address
  );
};

export const getLendToken = async (address?: tEthereumAddress) => {
  return await getContract<any>(
    eContractid.MintableErc20,
    address ||
      (await getDb().get(`${eContractid.MintableErc20}.${DRE.network.name}`).value()).address
  );
};

export const getLendToAaveMigratorImpl = async (address?: tEthereumAddress) => {
  return await getContract<LendToAaveMigrator>(
    eContractid.LendToAaveMigrator,
    address ||
      (await getDb().get(`${eContractid.LendToAaveMigratorImpl}.${DRE.network.name}`).value())
        .address
  );
};

export const getLendToAaveMigrator = async (address?: tEthereumAddress) => {
  return await getContract<LendToAaveMigrator>(
    eContractid.LendToAaveMigrator,
    address ||
      (await getDb().get(`${eContractid.LendToAaveMigrator}.${DRE.network.name}`).value()).address
  );
};

export const getMintableErc20 = async (address: tEthereumAddress) => {
  return await getContract<MintableErc20>(
    eContractid.MintableErc20,
    address ||
      (await getDb().get(`${eContractid.MintableErc20}.${DRE.network.name}`).value()).address
  );
};

export const getDoubleTransferHelper = async (address: tEthereumAddress) => {
  return await getContract<DoubleTransferHelper>(
    eContractid.DoubleTransferHelper,
    address ||
      (await getDb().get(`${eContractid.DoubleTransferHelper}.${DRE.network.name}`).value()).address
  );
};

export const getMockTransferHook = async (address?: tEthereumAddress) => {
  return await getContract<MockTransferHook>(
    eContractid.MockTransferHook,
    address ||
      (await getDb().get(`${eContractid.MockTransferHook}.${DRE.network.name}`).value()).address
  );
};

export const getIErc20Detailed = async (address: tEthereumAddress) => {
  return await getContract<Ierc20Detailed>(
    eContractid.IERC20Detailed,
    address ||
      (await getDb().get(`${eContractid.IERC20Detailed}.${DRE.network.name}`).value()).address
  );
};

export const getInitializableAdminUpgradeabilityProxy = async (address: tEthereumAddress) => {
  return await getContract<InitializableAdminUpgradeabilityProxy>(
    eContractid.InitializableAdminUpgradeabilityProxy,
    address ||
      (
        await getDb()
          .get(`${eContractid.InitializableAdminUpgradeabilityProxy}.${DRE.network.name}`)
          .value()
      ).address
  );
};

export const convertToCurrencyDecimals = async (tokenAddress: tEthereumAddress, amount: string) => {
  const isEth = tokenAddress === MOCK_ETH_ADDRESS;
  let decimals = '18';

  if (!isEth) {
    const token = await getIErc20Detailed(tokenAddress);
    decimals = (await token.decimals()).toString();
  }

  return ethers.utils.parseUnits(amount, decimals);
};

export const convertToCurrencyUnits = async (tokenAddress: string, amount: string) => {
  const isEth = tokenAddress === MOCK_ETH_ADDRESS;

  let decimals = new BigNumber(18);
  if (!isEth) {
    const token = await getIErc20Detailed(tokenAddress);
    decimals = new BigNumber(await token.decimals());
  }
  const currencyUnit = new BigNumber(10).pow(decimals);
  const amountInCurrencyUnits = new BigNumber(amount).div(currencyUnit);
  return amountInCurrencyUnits.toFixed();
};

export const buildPermitParams = (
  chainId: number,
  aaveToken: tEthereumAddress,
  owner: tEthereumAddress,
  spender: tEthereumAddress,
  nonce: number,
  deadline: string,
  value: tStringTokenSmallUnits
) => ({
  types: {
    EIP712Domain: [
      {name: 'name', type: 'string'},
      {name: 'version', type: 'string'},
      {name: 'chainId', type: 'uint256'},
      {name: 'verifyingContract', type: 'address'},
    ],
    Permit: [
      {name: 'owner', type: 'address'},
      {name: 'spender', type: 'address'},
      {name: 'value', type: 'uint256'},
      {name: 'nonce', type: 'uint256'},
      {name: 'deadline', type: 'uint256'},
    ],
  },
  primaryType: 'Permit' as const,
  domain: {
    name: 'Aave Token',
    version: '1',
    chainId: chainId,
    verifyingContract: aaveToken,
  },
  message: {
    owner,
    spender,
    value,
    nonce,
    deadline,
  },
});

export const buildDelegateByTypeParams = (
  chainId: number,
  aaveToken: tEthereumAddress,
  delegatee: tEthereumAddress,
  type: string,
  nonce: string,
  expiry: string
) => ({
  types: {
    EIP712Domain: [
      {name: 'name', type: 'string'},
      {name: 'version', type: 'string'},
      {name: 'chainId', type: 'uint256'},
      {name: 'verifyingContract', type: 'address'},
    ],
    DelegateByType: [
      {name: 'delegatee', type: 'address'},
      {name: 'type', type: 'uint256'},
      {name: 'nonce', type: 'uint256'},
      {name: 'expiry', type: 'uint256'},
    ],
  },
  primaryType: 'DelegateByType' as const,
  domain: {
    name: 'Aave Token',
    version: '1',
    chainId: chainId,
    verifyingContract: aaveToken,
  },
  message: {
    delegatee,
    type,
    nonce,
    expiry,
  },
});

export const buildDelegateParams = (
  chainId: number,
  aaveToken: tEthereumAddress,
  delegatee: tEthereumAddress,
  nonce: string,
  expiry: string
) => ({
  types: {
    EIP712Domain: [
      {name: 'name', type: 'string'},
      {name: 'version', type: 'string'},
      {name: 'chainId', type: 'uint256'},
      {name: 'verifyingContract', type: 'address'},
    ],
    Delegate: [
      {name: 'delegatee', type: 'address'},
      {name: 'nonce', type: 'uint256'},
      {name: 'expiry', type: 'uint256'},
    ],
  },
  primaryType: 'Delegate' as const,
  domain: {
    name: 'Aave Token',
    version: '1',
    chainId: chainId,
    verifyingContract: aaveToken,
  },
  message: {
    delegatee,
    nonce,
    expiry,
  },
});

export const getSignatureFromTypedData = (
  privateKey: string,
  typedData: any // TODO: should be TypedData, from eth-sig-utils, but TS doesn't accept it
): ECDSASignature => {
  const signature = signTypedData_v4(Buffer.from(privateKey.substring(2, 66), 'hex'), {
    data: typedData,
  });
  return fromRpcSig(signature);
};
