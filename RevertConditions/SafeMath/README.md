# SafeMath Reverts
SafeMath is a Solidity library developed by OpenZeppelin that wraps over Solidity math operation to prevent undefined behaviors.
Instead, when such a state is reached (for example division by 0) the SafeMath will be responsible to revert the transaction.
From Solidity 8.0 onward, SafeMath is integrated be default into the language and you don't need any special imports to use it.

The simple contract and spec in this example demonstrate 3 different reverts on 3 undefined states that SafeMath catches for us.
In `SafeMathReverts.sol` we have a contract that has a uint256 value which can be manipulated in different ways, it can be increased, decreased and divided. The spec we wrote checks that no matter the amounts we want to manipulate value with, we will always revert when reaching an undefined state.

The 3 undefined states are:
* Overflow - Value can be represented by a maximum of 256 bits of memory. An overflow is a state in which a value gets bigger than the maximum number that can be represented by 256 bits.
* Underflow - Value is an unsigned integer, that means he cannot be negative (cannot have a minus sign). An underflow is a state in which value becomes negative when he cannot.
* Division by zero - This is a very big math no no, you simply cannot divide by zero in math!

You can run this spec using:
```certoraRun SafeMathReverts.conf```

[A report of this run](https://prover.certora.com/output/15800/a94f75ebce7640df84fa2bc126374686?anonymousKey=6254f7dfd4c4006c726d88fe28f63e303542d3ed)