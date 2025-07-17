invariant isUnlocked(env e)
   getLock(e) == 0 
   filtered {
       // The functions repay and borrow use the modifier onlyLocked therefore excluding them here, as it causes vacuity with the invariant expression.
       f -> f.selector != sig:repay(int256).selector 
         && f.selector != sig:borrow(int256).selector
         // The function callback calls repay and borrow, thus same applied as above. 
         && f.selector != sig:CallBacker.callback().selector 
         }

invariant deltaZeroWhenUnlocked(env e)
    getLock(e) == 0 => getDelta(e) == 0;

invariant deltaEqualsStorage(env e)
   getDelta(e) == currentContract.storageValue
{
   preserved onTransactionBoundary with(env e2) {
      requireInvariant isUnlocked(e2);
      requireInvariant deltaZeroWhenUnlocked(e2);
   }
}