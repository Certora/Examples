import {evmRevert, evmSnapshot, DRE} from '../../helpers/misc-utils';
import {Signer} from 'ethers';
import {
  getEthersSigners,
  getAaveToken,
  getLendToken,
  getLendToAaveMigrator,
  getLendToAaveMigratorImpl,
  getMockTransferHook,
} from '../../helpers/contracts-helpers';
import {tEthereumAddress} from '../../helpers/types';

import chai from 'chai';
// @ts-ignore
import bignumberChai from 'chai-bignumber';
import {AaveToken} from '../../types/AaveToken';
import {LendToAaveMigrator} from '../../types/LendToAaveMigrator';
import {MintableErc20} from '../../types/MintableErc20';
import {MockTransferHook} from '../../types/MockTransferHook';

chai.use(bignumberChai());

export interface SignerWithAddress {
  signer: Signer;
  address: tEthereumAddress;
}
export interface TestEnv {
  deployer: SignerWithAddress;
  users: SignerWithAddress[];
  aaveToken: AaveToken;
  lendToken: MintableErc20;
  lendToAaveMigrator: LendToAaveMigrator;
  lendToAaveMigratorImpl: LendToAaveMigrator;
  mockTransferHook: MockTransferHook;
}

let buidlerevmSnapshotId: string = '0x1';
const setBuidlerevmSnapshotId = (id: string) => {
  if (DRE.network.name === 'hardhat') {
    buidlerevmSnapshotId = id;
  }
};

const testEnv: TestEnv = {
  deployer: {} as SignerWithAddress,
  users: [] as SignerWithAddress[],
  aaveToken: {} as AaveToken,
  lendToken: {} as MintableErc20,
  lendToAaveMigrator: {} as LendToAaveMigrator,
  lendToAaveMigratorImpl: {} as LendToAaveMigrator,
  mockTransferHook: {} as MockTransferHook,
} as TestEnv;

export async function initializeMakeSuite() {
  const [_deployer, ...restSigners] = await getEthersSigners();
  const deployer: SignerWithAddress = {
    address: await _deployer.getAddress(),
    signer: _deployer,
  };

  for (const signer of restSigners) {
    testEnv.users.push({
      signer,
      address: await signer.getAddress(),
    });
  }
  testEnv.deployer = deployer;
  testEnv.aaveToken = await getAaveToken();
  testEnv.lendToAaveMigrator = await getLendToAaveMigrator();
  testEnv.lendToken = await getLendToken();
  testEnv.lendToAaveMigratorImpl = await getLendToAaveMigratorImpl();
  testEnv.mockTransferHook = await getMockTransferHook();
}

export function makeSuite(name: string, tests: (testEnv: TestEnv) => void) {
  describe(name, () => {
    before(async () => {
      setBuidlerevmSnapshotId(await evmSnapshot());
    });
    tests(testEnv);
    after(async () => {
      await evmRevert(buidlerevmSnapshotId);
    });
  });
}
