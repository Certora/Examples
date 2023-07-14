pragma solidity ^0.8.1;

contract LinkedList {
  struct Element {
    bytes32 nextKey;
    uint256 valid;
  }

  struct List {
    bytes32 head;
    mapping(bytes32 => Element) elements;
  }

  List list;

  /**
   * @notice Inserts an element into a doubly linked list.
   * @param key The key of the element to insert.
   * @param afterKey The key of the element that comes before the element to insert. Or 0 to insert at the head.
   */
  function insertAfter(bytes32 key, bytes32 afterKey) public {
    require(key != bytes32(0), "Key must be defined");
    require(!contains(key), "Can't insert an existing element");
    require(afterKey != key, "Key cannot be the same as afterKey");

    Element storage element = list.elements[key];
    element.valid = 1;

    if (afterKey == 0) {
        element.nextKey = list.head;
        list.head = key;
    } else {
        require(contains(afterKey), "If afterKey is defined, it must exist in the list");
        bytes32 tmp = list.elements[afterKey].nextKey;
        element.nextKey = tmp; 
        list.elements[afterKey].nextKey = key; 
    }
  }

  function getSucc(bytes32 key) public view returns (bytes32) {
    return list.elements[key].nextKey;
  }

  function head() public view returns (bytes32) {
    return list.head;
  }

  /**
   * @notice Returns whether or not a particular key is present in the sorted list.
   * @param key The element key.
   * @return Whether or not the key is in the sorted list.
   */
  function contains(bytes32 key) public view returns (bool) {
    return list.elements[key].valid != 0;
  }
}
