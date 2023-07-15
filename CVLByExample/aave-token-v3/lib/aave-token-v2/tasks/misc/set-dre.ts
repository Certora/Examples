import {task} from 'hardhat/config';
import {setDRE} from '../../helpers/misc-utils';

task(`set-dre`, `Inits the DRE, to have access to all the plugins' objects`).setAction(
  async (_, _BRE) => {
    await setDRE(_BRE);
    return _BRE;
  }
);
