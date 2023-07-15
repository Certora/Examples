const accounts = require(`./test-wallets.js`).accounts;

module.exports = {
  skipFiles: ["open-zeppelin/"],
  mocha: {
    enableTimeouts: false,
  },
  providerOptions: {
    accounts,
    _chainId: 1337,
    _chainIdRpc: 1337,
    network_id: 1337,
  },
};
