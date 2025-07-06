invariant deltaZeroWhenUnlocked(env e)
    getLock(e) == 0 => getDelta(e) == 0;

invariant deltaEqualsStorage(env e)
   getDelta(e) == currentContract.storageValue
{
   preserved onTransactionBoundary with(env e2) {
      require getLock(e2) == 0, "Contract must be unlocked";
      requireInvariant deltaZeroWhenUnlocked(e2);
   }
}