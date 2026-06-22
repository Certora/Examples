## Mini Constant Product Pool

The following system is based on a simplified version of the Trident bug that was found by the Certora Prover.
You can find a brief explanation about the original system and bug here:
https://medium.com/certora/exploiting-an-invariant-break-how-we-found-a-pool-draining-bug-in-sushiswaps-trident-585bd98a4d4f 
 

In constant-product pools, liquidity providers (LPs) deposit two types of underlying tokens (Token0 and Token1) in exchange for LP tokens. 
They can later burn LP tokens to reclaim a proportional amount of Token0 and Token1.
Trident users can swap one underlying token for the other by transferring some tokens of one type to the pool and receiving some number of the other token.
To determine the exchange rate, the pool returns enough tokens to ensure that
(reserves0 ⋅ reserves1)ᵖʳᵉ =(reserves0 ⋅ reserves1)ᵖᵒˢᵗ
where reserves0 and reserves1 are the amount of token0 and token1 the system holds. 

On first liquidity deposit, the system transfers 1000 LP tokens to address 0 to ensure the pool cannot be emptied.  

An important property is that if there are liquidity providers (totalSupply >0) than there must be assets in both tokens. 
This property is written in CVL and in foundry as invariant. 
### Fuzz test

To run the fuzz test from the CPP_mini folder:
```
forge coverage --report lcov --report-file fuzz --match-contract CPPMini
genhtml fuzz -o fuzzcov
open fuzzcov/index.html
```
Coverage is very good - 96.3%, however the bug is missed.

The bug is demonstrated in a manual crafted test `test_manual()` and shows how it can cause a complete drain of the protocol.


### Formal verification 
To run the verification:
```certoraRun certora/conf/runBroken.conf```

As seen in the report, the property is violated: https://prover.certora.com/output/40726/4ba34bd0d7d54c279c7cb261d1616fef/?anonymousKey=626461dda2213599b57007646d3198b21c249908


Once the bug is fixed the property is verified:
```certoraRun certora/conf/runFixed.conf```

https://prover.certora.com/output/40726/a90ecf39cd7a44d59b30ff8a6172e8ff/?anonymousKey=cac7192076ce98c8465b939d2ac2001385a484ff
