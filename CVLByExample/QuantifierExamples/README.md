# QuantifierExamples
This repository contains examples of Certora specs using quantifiers and
quantified invariants.  These examples were presented in the advanced webinar
on quantifiers:

[<img src="./webinar-quantifiers.png" width="50%" />](https://youtu.be/IEB6adfjsA8)

- [Recording on YouTube](https://youtu.be/IEB6adfjsA8)
- [Slides from the Webinar](./webinar-quantifiers.pdf)


The following examples were used in the Webinar.
The first two are based on existing code.

- [EnumerableSet](./EnumerableSet) from [OpenZeppelin][1]: We show that the set view and the array view are always consistent and all methods work as expected.

Run this spec via
```certoraRun set.conf``` from `EnumerableSet`.

[A report of this run](https://prover.certora.com/output/15800/2b7079a4dcc5410cb0f8017dcdd55627?anonymousKey=eff8f0e0c2a5ef20af958194830c42b7c2f3145e)

- [DoubleLinkedList](./DoublyLinkedList) from [Morpho][2]: We show the consistency of linkage: the next and prev pointers match for each element.

Run this spec via
```certoraRun linkedCorrectly.conf``` from `DoublyLinkedList`.

[A report of this run](https://prover.certora.com/output/15800/e68c99b590764792aaee491f6a110963?anonymousKey=090f19d57f649604cf86d600722a1f00043da623)

- [LinkedList](./SinglyLinkedList): For a simple struct-based singly-linked list we show correctness,
including the fact that each element in the list is reachable from the head.

Run this spec via 
```certoraRun list.conf``` from `SinglyLinkedList`.

[A report of this run](https://prover.certora.com/output/15800/ed04ec27f4aa4a91831acece0749b6dc?anonymousKey=a0fcd266019bf068dc9f778843e43a2cd197ff2e)

[1]: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/structs/EnumerableSet.sol "EnumerableSet from OpenZeppelin"
[2]: https://github.com/morpho-org/morpho-data-structures/blob/main/src/DoubleLinkedList.sol "DoubleLinkedList from Morpho"
