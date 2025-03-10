# Using `calledContract` and `executingContract` in Summaries

This directory demonstrates how to use two CVL keywords—`calledContract` and `executingContract`—to track function call details within a summary context. The repository contains:

1. A Solidity file, **`CalledContractAndExecutingContract.sol`**, which defines contracts **`Primary`**, **`Secondary`**, and **`Tertiary`**, as well as a **`Library`**.  
2. A CVL spec file, **`CalledContractAndExecutingContract.spec`**, which verifies rules about contract function calls and how the two new keywords behave under different call types.

## 1. Solidity File Overview

The file **`CalledContractAndExecutingContract.sol`** declares three contracts (`Primary`, `Secondary`, `Tertiary`) and one library (`Library`). Each contract has two “callee” functions:

- `calleeInternal()` – an internal function  
- `calleeExternal()` – an external function  

In addition, `Primary` and `Secondary` implement various "call" functions that invoke these callee functions in different ways:

1. **Calls within the same contract** (e.g., `Primary` calling its own internal method).  
2. **Calls to another contract** (e.g., `Primary` calling an external method on `Secondary`).  
3. **Calls from one contract to another that in turn calls back** (e.g., `Secondary` calling `Primary` again).  
4. **Library calls**, both internal and external (e.g., `Library.calleeInternal()` from within `Primary` or `Secondary`).  
5. **Delegate calls**, where `Primary` uses `delegatecall` to call `Secondary`'s external function, ensuring the code runs in `Secondary` but uses `Primary`'s storage context.  

These different invocation patterns let us test when and how `calledContract` and `executingContract` diverge.

## 2. CVL Specification Overview

The **`CalledContractAndExecutingContract.spec`** file does two key things:

1. **Summaries**: Inside the `methods` block, it summarizes every `calleeInternal` and `calleeExternal` function (for all contracts and the library) by calling a helper function, `saveContracts`, which writes into ghost variables `called`, `executing`, and `sender`.
2. **Rules**: A series of rules each perform a high-level call (e.g., `callPrimaryInternal`, `callSecondaryExternal`, etc.) from the `Primary` contract, and then assert that the ghost variables hold the correct addresses for the **called contract**, the **executing contract**, and the **sender**.  

### 2.1 Summaries (Using `calledContract` and `executingContract`)

In the `methods` block, the specification shows how to attach a summary to an internal or external function:

```solidity
methods {
    function _.calleeInternal() internal with (env e)
        => saveContracts(calledContract, executingContract, e.msg.sender)
        expect void;

    function _.calleeExternal() external with (env e)
        => saveContracts(calledContract, executingContract, e.msg.sender)
        expect void ALL;
}
```

Here:
- **`calledContract`** is the address of the contract on which the summarized function was called.
- **`executingContract`** is the address of the contract that is actually running the function code.  
- **`e.msg.sender`** is the caller’s address as specified in the test environment.

These three values are passed to `saveContracts`, which stores them in ghost variables `called`, `executing`, and `sender`:

```solidity
ghost address called;
ghost address executing;
ghost address sender;

function saveContracts(address _called, address _executing, address _sender) {
    called = _called;
    executing = _executing;
    sender = _sender;
}
```

By capturing these addresses as ghost variables, we can write rules that check whether the correct caller/callee relationship is preserved.

### 2.2 Rules

Each rule (e.g., `rule primaryInternal(env e)`) performs a specific contract call (like `callPrimaryInternal`) and then checks the ghost variables. For instance:

```solidity
rule primaryInternal(env e) {
    callPrimaryInternal(e);
    assert called == primary;
    assert executing == primary;
    assert sender == e.msg.sender;
}
```

- We make a call to `callPrimaryInternal`.
- Internally, this triggers `calleeInternal` on the same contract (`Primary`), setting `called = primary`, `executing = primary`, and `sender = e.msg.sender`.
- The rule then **asserts** that these ghost variables match the expected values.

By comparing `called`, `executing`, and `sender` in each rule, we ensure that **internal calls**, **external calls**, **delegate calls**, and **library calls** update the ghosts consistently with how the EVM actually routes the call.

## 3. Behavior of `calledContract` and `executingContract`

### `calledContract`
- Represents the address of the contract on which the summarized method was called.
- For **internal calls**, `calledContract` is the same as the contract containing the function (i.e., “this”).
- For **library calls** and **delegate calls**, `calledContract` can be the contract *initiating* the code execution (since libraries and delegate calls run in the caller’s context).

### `executingContract`
- Represents the address of the contract that *initiated the call*.
- For **internal** and **delegate** calls, this will be the same as `calledContract`.
- For **external** calls, it will be the address of the caller, while `calledContract` is the address of the receiver.

### Additional Notes on the Keywords

- **`calledContract`** is only valid within the `methods` block (i.e., inside function summaries). It is essentially `address(this)` in the context of the original call you are summarizing.  
- **`executingContract`** is also only valid within the `methods` block (and in certain hook bodies) and distinguishes the actual execution context when calls involve libraries or delegate calls.  
- They are not arbitrary variables that can be combined or manipulated further. You can only pass them into your summary function (e.g., `saveContracts`) or reference them directly in your specification.  

## 4. Run the Example
To run the example use:
```
certoraRun CalledContractAndExecutingContract.conf
```

[The report of this run](https://prover.certora.com/output/15800/9e05615085b445f98e4cc26a06dd15c7?anonymousKey=a858189c9d763bcc29bad9941fa8543d3eba89b8)
