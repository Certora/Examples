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

By default, the prover overapproximates and assumes that B can be any contract, so the call above is unresolved.
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
The keys to the dictionary are the contracts we want to extend, and their values are lists of extension contracts and lists of functions that should be excluded from the extension (to avoid duplicate functions).

What this does is "transfer" the methods from the extension contracts into the extended one, so analysis could do its thing.

Some more details:
* The implementation of all external methods are removed from the extension contract, so they should never be called. To prevent this there are several guards:
    - Parametric rules will filter out functions from the extension function directly (only as functions of the extended contract).
    - Attempting to alias an Extension function will lead to a typechecker error.
        + One shouldn’t call the functions of the extension contract using that contract as the receiver, only use the extended contract as a receiver.
    - Attempting to add a preserved block on an extension function will lead to a typechecker error.
        + Again, one should be using the extended contract as the receiver.

Run this example using:
```certoraRun ExtensionContracts.conf```

[Report of this run](https://prover.certora.com/output/97560/08306dd220694ca799451e21749d8434?anonymousKey=547879f75744db0c526e690a8b3fad81b4ebcf32)

## Extension Contracts Override

There are implementations of the proxy pattern in which the base contract actually has implementations for all the functions
that are implemented by the extension contracts - all they do is delegatecall the corresponding function in the extension contract. In this case
an extra flag needs to be set in order to "move" the functions from the extension contract into the
base one: `--contract_extensions_override`.

You can see adn run an example of this with
```certoraRun overrideExtended.conf```

[Report of this run](https://prover.certora.com/output/97560/68336a8a71aa42b2a66b512810b05b14?anonymousKey=f171bc0ba2d337fc4879f3165215904e72fb7416)
