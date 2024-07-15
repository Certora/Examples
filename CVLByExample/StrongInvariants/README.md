# Strong Invariant Feature Demonstration

The Strong Invariant feature ensures that certain invariants hold whenever control is yielded to an external function, providing enhanced security, especially for contracts without global locks.

## Running the Example

To run the example and verify the invariants, use the following command:

```
certoraRun StrongInvariants.conf
```

## Results

You can view the results of running the invariants verification at the following link:

[Certora Output Results](https://prover.certora.com/output/1512/2c471bfb42464bf5849afce75a950052?anonymousKey=2fb8a42e6fc6c250215ffacaa42e7f67cd91d22b)

## Results Explanation

### Contract Functions

- **modifyAndExternalCall:** Modifies `storageValue` before and after making an external call. This tests if the strong invariant can catch the change during the external call while the weak invariant misses it, exactly as expected.

### Key Differences

- **Strong Invariant:** Checked continuously, including during external calls. Ensures contract state consistency across all execution paths. In the `modifyAndExternalCall` function, the strong invariant detects the change in `storageValue` and fails the check, showcasing its strict enforcement of contract state.
- **Weak Invariant:** Only checked at the boundaries of top-level calls. Allows temporary state changes during internal execution, focusing on the final state after all operations. In the `modifyAndExternalCall` function, the weak invariant misses the intermediate change in `storageValue`, demonstrating its leniency compared to the strong invariant.

## Conclusion

The new Strong Invariant feature provides an essential tool for ensuring the integrity of smart contracts, particularly in scenarios involving external callbacks. By using strong invariants, developers can guarantee that certain conditions hold throughout the execution of their contracts, enhancing security and reliability.