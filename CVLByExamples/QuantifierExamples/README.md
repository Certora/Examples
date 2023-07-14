# QuantifierExamples
This repository contains examples of Certora specs using quantifiers and
quantified invariants.  These examples were presented in the advanced webinar
on quantifiers:

[<img src="./webinar-quantifiers.png" width="50%" />](https://youtu.be/IEB6adfjsA8)

- [Recording on YouTube](https://youtu.be/IEB6adfjsA8)
- [Slides from the Webinar](./webinar-quantifiers.pdf)


The following examples were used in the Webinar.
The first two examples are based on existing code.

- [EnumerableSet](./EnumerableSet) from [OpenZeppelin][1]: We show that the set view and the array view are always consistent and all methods work as expected.
- [DoubleLinkedList](./DoublyLinkedList) from [Morpho][2]: We show the consistency of linkage: The next and prev pointer match for each element.
- [LinkedList](./SinglyLinkedList): For a simple struct-based singly-linked list we show correctness,
including that each element in the list is reachable from the head.

[1]: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/structs/EnumerableSet.sol "EnumerableSet from OpenZeppelin"
[2]: https://github.com/morpho-org/morpho-data-structures/blob/main/src/DoubleLinkedList.sol "DoubleLinkedList from Morpho"
