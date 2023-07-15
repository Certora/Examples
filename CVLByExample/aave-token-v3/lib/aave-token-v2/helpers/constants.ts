import {tEthereumAddress} from './types';
import {getParamPerNetwork} from './misc-utils';
import {eEthereumNetwork} from './types-common';

export const BUIDLEREVM_CHAINID = 31337;
export const COVERAGE_CHAINID = 1337;

export const ZERO_ADDRESS: tEthereumAddress = '0x0000000000000000000000000000000000000000';
export const ONE_ADDRESS = '0x0000000000000000000000000000000000000001';
export const MAX_UINT_AMOUNT =
  '115792089237316195423570985008687907853269984665640564039457584007913129639935';
export const MOCK_ETH_ADDRESS = '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE';
export const WAD = Math.pow(10, 18).toString();

export const SUPPORTED_ETHERSCAN_NETWORKS = ['main', 'ropsten', 'kovan'];

export const getAaveTokenDomainSeparatorPerNetwork = (
  network: eEthereumNetwork
): tEthereumAddress =>
  getParamPerNetwork<tEthereumAddress>(
    {
      [eEthereumNetwork.coverage]:
        '0x6334ce07fc771d21f0634439a587b364f00756c209bb425d2c4873b672e6d265',
      [eEthereumNetwork.hardhat]:
        '0xd76d40d21133f42fdacea0d02807309902f26a87ff5b55bb55ac77f881143cc4',
      [eEthereumNetwork.kovan]: '',
      [eEthereumNetwork.ropsten]: '',
      [eEthereumNetwork.main]: '',
    },
    network
  );

// AaveProtoGovernance address as admin of AaveToken and Migrator
export const getAaveAdminPerNetwork = (network: eEthereumNetwork): tEthereumAddress =>
  getParamPerNetwork<tEthereumAddress>(
    {
      [eEthereumNetwork.coverage]: ZERO_ADDRESS,
      [eEthereumNetwork.hardhat]: ZERO_ADDRESS,
      [eEthereumNetwork.kovan]: '0x8134929c3dcb1b8b82f27f53424b959fb82182f2',
      [eEthereumNetwork.ropsten]: '0xEd93e49A2d75beA505fD4D1A0Dff745f69F2E997',
      [eEthereumNetwork.main]: '0x8a2Efd9A790199F4c94c6effE210fce0B4724f52',
    },
    network
  );

export const getLendTokenPerNetwork = (network: eEthereumNetwork): tEthereumAddress =>
  getParamPerNetwork<tEthereumAddress>(
    {
      [eEthereumNetwork.coverage]: ZERO_ADDRESS,
      [eEthereumNetwork.hardhat]: ZERO_ADDRESS,
      [eEthereumNetwork.kovan]: '0x690eaca024935aaff9b14b9ff9e9c8757a281f3c',
      [eEthereumNetwork.ropsten]: '0xb47f338ec1e3857bb188e63569aebab036ee67c6',
      [eEthereumNetwork.main]: '0x80fB784B7eD66730e8b1DBd9820aFD29931aab03',
    },
    network
  );
