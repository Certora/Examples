// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title C
 * @dev A simple contract demonstrating functions that can revert
 */
contract C {
    bool public fooWasCalled;

    /**
     * @notice Sets fooWasCalled and reverts if the input b is false
     */
    function foo(bool b) external {
        fooWasCalled = true;
        if (!b) {
            revert("foo reverted");
        }
    }

    /**
     * @notice Calls foo and can therefore revert if foo reverts
     */
    function callFooFromContract(bool b) external {
        this.foo(b);
    }

    /**
     * @notice Dummy function that can be used to demonstrate "summary" usage
     */
    function summarizeMe(bool b) external {}

    /**
     * @notice Returns b or reverts if b is false
     */
    function canRevert(bool b) external returns (bool) {
        if (!b) {
            revert("canRevert reverted");
        }
        return b;
    }

    /**
     * @notice Calls summarizeMe and can be used for demonstration of deeper calls
     */
    function callSummarizeMe(bool b) external {
        this.summarizeMe(b);
    }
}
