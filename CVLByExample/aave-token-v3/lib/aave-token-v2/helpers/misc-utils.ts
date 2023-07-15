import BigNumber from 'bignumber.js';
import BN = require('bn.js');
import low from 'lowdb';
import FileSync from 'lowdb/adapters/FileSync';
import {WAD} from './constants';
import {Wallet, ContractTransaction} from 'ethers';
import {HardhatRuntimeEnvironment} from 'hardhat/types';
import {iParamsPerNetwork} from './types';
import {eEthereumNetwork} from './types-common';

export const toWad = (value: string | number) => new BigNumber(value).times(WAD).toFixed();

export const bnToBigNumber = (amount: BN): BigNumber => new BigNumber(<any>amount);
export const stringToBigNumber = (amount: string): BigNumber => new BigNumber(amount);

export const getDb = () => low(new FileSync('./deployed-contracts.json'));

export let DRE: HardhatRuntimeEnvironment = {} as HardhatRuntimeEnvironment;
export const setDRE = (_DRE: HardhatRuntimeEnvironment) => {
  DRE = _DRE;
};

export const getParamPerNetwork = <T>(
  {kovan, ropsten, main, hardhat, coverage}: iParamsPerNetwork<T>,
  network: eEthereumNetwork
) => {
  switch (network) {
    case eEthereumNetwork.coverage:
      return coverage;
    case eEthereumNetwork.hardhat:
      return hardhat;
    case eEthereumNetwork.kovan:
      return kovan;
    case eEthereumNetwork.ropsten:
      return ropsten;
    case eEthereumNetwork.main:
      return main;
    default:
      return main;
  }
};

export const sleep = (milliseconds: number) => {
  return new Promise((resolve) => setTimeout(resolve, milliseconds));
};

export const createRandomAddress = () => Wallet.createRandom().address;

export const waitForTx = async (tx: ContractTransaction) => await tx.wait();

export const evmSnapshot = async () => await DRE.ethers.provider.send('evm_snapshot', []);

export const evmRevert = async (id: string) => DRE.ethers.provider.send('evm_revert', [id]);

export const timeLatest = async () => {
  const block = await DRE.ethers.provider.getBlock('latest');
  return new BigNumber(block.timestamp);
};

export const advanceBlock = async (timestamp: number) =>
  await DRE.ethers.provider.send('evm_mine', [timestamp]);

export const increaseTime = async (secondsToIncrease: number) =>
  await DRE.ethers.provider.send('evm_increaseTime', [secondsToIncrease]);
