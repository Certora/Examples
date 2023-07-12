This directory contains two versions of the ConstantProductPool contract.

1. ConstantProductPool.sol is a faulty version with the following failing rules:

    integrityOfSwap - there is a switch between the token and the recipient in swap:
            Should be transfer( recipient, tokenOut, amountOut);

    noDecreaseByOther - there is a switch between the token and the recipient in burnSingle.

    balanceGreaterThanReserve - This invariant also catches the bug in which there is a switch between the token and the recipient in burnSingle:
            should be transfer( recipient, tokenOut, amountOut);

    integrityOfTotalSupply - This invariant catches the original bug in Trident where the amount to receive is computed as a function of the balances and not the reserves.

    monotonicityOfMint - there is a bug in mint where the LP tokens of the first depositor are not computed correctly and the less he transfers the more LP-tokens he receives. 

    This version can be verified by running

    certoraRun certora/conf/runFixed.conf

2. ConstantProductPoolFixed.sol - a version in which the bug in swap is fixed and all the rules pass.
    This contract can be verified by running
    certoraRun certora/conf/run.conf









