# Extension Contracts

A contract extension is about splitting the functionality of a single contract into several ones and using delegatecalls between them.

For example:
```
contract Extended {
    address public extensionAddress; // Address of contract Extension

    // Fallback function will handle all calls that don't match a function signature
    fallback() external payable {
        // Delegate the call to contract Extension
        (bool success, ) = bAddress.delegatecall(msg.data);
        require(success, "Delegatecall failed");
    }
}

Contract B {
	function foo() external { ... }
}
```
Then when someone calls B(aAddress).foo() the call is delegated to B via A's fallback function.

Usually the prover doesn't "understand" that B is in an extension of A, so the call above is unresolved.
To support this pattern a new option `contract_extensions` was added which accepts a dictionary of the form:
```
"contract_extensions": {
    "A": [
        {
            "extension": "B",
            "exclude": ["value", "sender", "num"],
        },
        {
            "extension": "C",
            "exclude": ["value", "sender", "num"],
        },
    ],
	"D": [
		...
	],
    ...
}
```
The keys to the dictionary are the contracts we want to extend, and their values are lists of extension (extension) contracts and lists of functions that should be excluded from the extension (to avoid duplicate functions).

What this does is "transfer" the methods from the extension contracts into the extended one, so analysis could do its thing.

Some more details:
* The implementation of all external methods are removed from the extension contract, so they should never be called. To prevent this there are several guards:
    - Parametric rules will filter out functions from the extension function directly (only as functions of the extended contract).
    - Attempting to alias an Extension function will lead to a typechecker error.
        + One shouldn’t call the functions of the extension contract using that contract as the receiver, only use the extended contract as a receiver.
    - Attempting to add a preserved block on an extension function will lead to a typechecker error.
        + Again, one should be using the extended contract as the receiver.
