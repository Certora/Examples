import {eEthereumNetwork} from './helpers/types-common';
// @ts-ignore
import {accounts} from './test-wallets.js';
import {BUIDLEREVM_CHAINID, COVERAGE_CHAINID} from './helpers/constants';
import {HardhatUserConfig} from 'hardhat/config';

import 'hardhat-typechain';
import 'solidity-coverage';
import '@nomiclabs/hardhat-waffle';
import '@nomiclabs/hardhat-etherscan';
import path from 'path';
import fs from 'fs';

const SKIP_LOAD = process.env.SKIP_LOAD === 'true';

// Prevent to load scripts before compilation and typechain
if (!SKIP_LOAD) {
  ['misc', 'migrations', 'deployments'].forEach((folder) => {
    const tasksPath = path.join(__dirname, 'tasks', folder);
    fs.readdirSync(tasksPath)
      .filter((pth) => pth.includes('.ts'))
      .forEach((task) => {
        require(`${tasksPath}/${task}`);
      });
  });
}

const DEFAULT_BLOCK_GAS_LIMIT = 12500000;
const DEFAULT_GAS_PRICE = 50000000000; // 50 gwei
const HARDFORK = 'istanbul';
const INFURA_KEY = process.env.INFURA_KEY || '';
const ALCHEMY_KEY = process.env.ALCHEMY_KEY || '';
const ETHERSCAN_KEY = process.env.ETHERSCAN_KEY || '';
const MNEMONIC_PATH = "m/44'/60'/0'/0";
const MNEMONIC = process.env.MNEMONIC || '';
const MAINNET_FORK = process.env.MAINNET_FORK === 'true';

const mainnetFork = MAINNET_FORK
  ? {
      blockNumber: 11366117,
      url: ALCHEMY_KEY
        ? `https://eth-mainnet.alchemyapi.io/v2/${ALCHEMY_KEY}`
        : `https://main.infura.io/v3/${INFURA_KEY}`,
    }
  : undefined;

const getCommonNetworkConfig = (networkName: eEthereumNetwork, networkId: number) => {
  return {
    url: ALCHEMY_KEY
      ? `https://eth-${
          networkName === 'main' ? 'mainnet' : networkName
        }.alchemyapi.io/v2/${ALCHEMY_KEY}`
      : `https://${networkName}.infura.io/v3/${INFURA_KEY}`,
    hardfork: HARDFORK,
    blockGasLimit: DEFAULT_BLOCK_GAS_LIMIT,
    gasMultiplier: DEFAULT_GAS_PRICE,
    chainId: networkId,
    accounts: {
      mnemonic: MNEMONIC,
      path: MNEMONIC_PATH,
      initialIndex: 0,
      count: 20,
    },
  };
};

const config: HardhatUserConfig = {
  solidity: {
    version: '0.7.5',
    settings: {
      optimizer: {enabled: true, runs: 200},
      evmVersion: 'istanbul',
    },
  },
  typechain: {
    outDir: 'types',
  },
  etherscan: {
    apiKey: ETHERSCAN_KEY,
  },
  mocha: {
    timeout: 0,
  },
  networks: {
    kovan: getCommonNetworkConfig(eEthereumNetwork.kovan, 42),
    ropsten: getCommonNetworkConfig(eEthereumNetwork.ropsten, 3),
    main: getCommonNetworkConfig(eEthereumNetwork.main, 1),
    hardhat: {
      hardfork: 'istanbul',
      blockGasLimit: DEFAULT_BLOCK_GAS_LIMIT,
      gas: DEFAULT_BLOCK_GAS_LIMIT,
      gasPrice: DEFAULT_GAS_PRICE,
      chainId: BUIDLEREVM_CHAINID,
      throwOnTransactionFailures: true,
      throwOnCallFailures: true,
      accounts: accounts.map(({secretKey, balance}: {secretKey: string; balance: string}) => ({
        privateKey: secretKey,
        balance,
      })),
      forking: mainnetFork,
    },
    buidlerevm_docker: {
      hardfork: 'istanbul',
      blockGasLimit: 9500000,
      gas: 9500000,
      gasPrice: 8000000000,
      chainId: BUIDLEREVM_CHAINID,
      throwOnTransactionFailures: true,
      throwOnCallFailures: true,
      url: 'http://localhost:8545',
    },
    ganache: {
      url: 'http://ganache:8545',
      accounts: {
        mnemonic: 'fox sight canyon orphan hotel grow hedgehog build bless august weather swarm',
        path: "m/44'/60'/0'/0",
        initialIndex: 0,
        count: 20,
      },
    },
    coverage: {
      url: 'http://localhost:8555',
      chainId: COVERAGE_CHAINID,
    },
  },
};

export default config;
