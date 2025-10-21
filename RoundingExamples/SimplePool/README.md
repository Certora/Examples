# Simple Pool Implementation with Rounding Bug Fixes

This directory contains a simple liquidity pool implementation that demonstrates common rounding issues in DeFi protocols and their fixes. The pool allows users to deposit assets, withdraw assets, and provides flash loan functionality.

## Pool.sol - Original Implementation

### Overview
The `Pool.sol` contract is an ERC20-based liquidity pool that:
- Allows users to deposit assets and receive shares
- Allows users to withdraw assets by burning shares
- Provides flash loan functionality with fees
- Distributes fees between the owner and liquidity providers


## Bugs in Pool.sol

### 1. **Incorrect Rounding Strategy in `withdraw()`**

**Problem**: The `withdraw()` function uses rounding down, which is incorrect for burning shares.

```solidity
function withdraw(uint256 amount) public returns (uint256 shares) {
    shares = amountToShares(amount);  // Rounds DOWN - WRONG for burning
    _burn(msg.sender, shares);
    asset.transfer(msg.sender, amount);
    depositedAmount = depositedAmount - amount;
}
```

**Impact**:
- Users can withdraw more assets than their shares represent
- This creates a vulnerability where users can drain the pool
- The pool's asset-to-share ratio becomes incorrect
- **Existing liquidity providers lose value** because users get more assets than they should


### 2. **Flash Loan Fee Distribution Bug**

**Problem**: The flash loan function has incorrect fee distribution logic that can cause transactions to revert.

```solidity
function flashLoan(address receiverAddress, uint256 amount) public {
    uint256 totalPremium = calcPremium(amount);
    uint256 splitPremium = totalPremium / 2;  // Rounds DOWN
    
    // ... flash loan logic ...
    
    asset.transferFrom(msg.sender, address(this), amount + splitPremium);
    asset.transferFrom(msg.sender, owner, splitPremium);  // Should be totalPremium - splitPremium
    depositedAmount = depositedAmount + amount + splitPremium;
}
```

**Issues**:

- **Transaction may revert**: User might need to pay `calcPremium(amount) + 1` due to rounding up in `calcPremium()`

## PoolFixed.sol - Fixed Implementation

### Key Fixes

#### 1. **Added Round-Up Function for Withdrawals**

```solidity
function amountToSharesRoundUp(uint256 amount) public view virtual returns (uint256) { 
    return (amount * totalSupply() + depositedAmount - 1) / depositedAmount;   
}
```

**Fix**: Uses ceiling division to ensure users burn at least the expected shares when withdrawing.

#### 2. **Fixed Withdraw Function**

```solidity
function withdraw(uint256 amount) public returns (uint256 shares) {
    shares = amountToSharesRoundUp(amount);  // Now rounds UP when burning
    _burn(msg.sender, shares);
    asset.transfer(msg.sender, amount);
    depositedAmount = depositedAmount - amount;
}
```

**Fix**: Uses round-up calculation when burning shares to protect existing liquidity providers from being drained.

#### 3. **Fixed Flash Loan Fee Distribution**

```solidity
function flashLoan(address receiverAddress, uint256 amount) public {
    uint256 totalPremium = calcPremium(amount);
    uint256 poolPremium = totalPremium / 2;  // Rounds DOWN (acceptable for pool)
    
    // ... flash loan logic ...
    
    asset.transferFrom(msg.sender, address(this), amount + poolPremium);
    asset.transferFrom(msg.sender, owner, totalPremium - poolPremium);  // FIXED
    depositedAmount = depositedAmount + amount + poolPremium;
}
```

**Fix**: 
- Owner now receives the correct amount (`totalPremium - poolPremium`)
- **Prevents reverts**: User only needs to pay exactly `calcPremium(amount)`, no extra tokens required
- Fee distribution is now mathematically correct

## CVL Specification Analysis

The `Pool.spec` file contains formal verification that are common properties of liquidity pools:

### 1. **Flash Loan Integrity Rule**
```cvl
rule flashLoanIntegrity(env e){
    require e.msg.sender != currentContract && e.msg.sender != currentContract.owner;
    address receiver;
    uint256 amount;

    uint256 userUnderlyingBalanceBefore = underlying.balanceOf(e.msg.sender);
    flashLoan(e, receiver, amount);
    uint256 userUnderlyingBalanceAfter = underlying.balanceOf(e.msg.sender);
    
    assert userUnderlyingBalanceAfter == userUnderlyingBalanceBefore - calcPremium(amount);
}
```

**Purpose**: Ensures users pay exactly the calculated premium for flash loans.

### 2. **Assets More Than Supply Invariant**
```cvl
invariant assetsMoreThanSupply()
    depositedAmount() >= totalSupply();
```

**Purpose**: Ensures the pool always has enough assets to cover all shares.

### 3. **Monotonic Supply Rate Rule**
```cvl
rule monotonicSupplyRate(method f) {
    // ... setup ...
    assert totalSupplyBefore != 0 => 
        balanceAfter * totalSupplyBefore >= balanceBefore * totalSupplyAfter;
}
```

**Purpose**: Ensures the exchange rate between assets and shares is monotonic (never decreases).

## Impact of the Bugs

### Without Fixes (Pool.sol):
- **LP Loss**: Existing liquidity providers lose value when users withdraw
- **Pool Drain**: Users can withdraw more assets than their shares represent
- **Fee Loss**: Incorrect fee distribution loses revenue
- **Invariant Violations**: Pool can become undercollateralized

### With Fixes (PoolFixed.sol):
- **LP Protection**: Existing liquidity providers are protected from rounding attacks
- **Security**: Withdrawals are properly bounded to prevent draining
- **Correct Fees**: Fee distribution works as intended
- **Invariant Preservation**: Pool maintains proper collateralization

## Lessons Learned

1. **Rounding Strategy Matters**: 
   - **Minting shares**: Round DOWN to favor existing LPs (users may lose up to 1 share worth)
   - **Burning shares**: Round UP to protect existing LPs (users burn at least expected shares)
2. **LP Protection is Priority**: Always favor existing liquidity providers in rounding decisions
3. **Test Edge Cases**: Small amounts and edge cases often reveal rounding bugs
4. **Formal Verification**: CVL specifications can catch subtle mathematical errors
5. **Fee Distribution**: Double-check fee distribution logic to ensure correct amounts

## Running the Verification

To run the CVL verification:

```bash
# For the original (buggy) implementation
certoraRun Pool.conf

# For the fixed implementation  
certoraRun PoolFixed.conf
```

### Verification Results

- **Pool.sol (Original)**: [Verification Report](https://prover.certora.com/output/40726/f9f39b92acf3413e92160aea1cf85cf9/?anonymousKey=9c216ec2800cdec0e7434bd581c73b1d9230873c) - Shows rule failures due to rounding bugs
- **PoolFixed.sol (Fixed)**: [Verification Report](https://prover.certora.com/output/40726/0049b352b63843fa9941ee85b429558a/?anonymousKey=aec58e56d26a7b0e68fc3aa64612463275f30739) - Shows all rules passing

The verification will show that the original implementation fails certain rules, while the fixed implementation passes all checks.
