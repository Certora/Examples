# PointsHook rules.

We have two specific rules for the PointsHook that check that the right
amount of tokens are minted:

```sh
certoraRun certora/conf/PointsHook.conf
```

The generic rules to check that the hook permissions are corresponding
to the implemented hook and to check that the hook prevents calls from
other contracts than the PoolManager are here:

```sh
certoraRun certora/conf/HookRules.conf
```

A very simple rule for the Uniswap v4 PoolManager is here:

```sh
certoraRun certora/conf/UniswapTake.conf
```
