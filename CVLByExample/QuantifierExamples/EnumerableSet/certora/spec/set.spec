// METHOD specification
// all methods never access environment (msg.sender, block number, etc.)
methods {
    function add(bytes32) external returns (bool) envfree;
    function remove(bytes32) external returns (bool) envfree;
    function contains(bytes32) external returns (bool) envfree;
    function length() external returns (uint256) envfree;
    function elemAt(uint256) external returns (bytes32) envfree;
}

// GHOST COPIES:
// For every storage variable we add a ghost field that is kept synchronized by hooks.
// The ghost fields can be accessed by the spec, even inside quantifiers.

// ghost field for the values array
ghost mapping(mathint => bytes32) ghostValues {
    init_state axiom forall mathint x. ghostValues[x] == to_bytes32(0);
}

// ghost field for the indexes map
ghost mapping(bytes32 => uint256) ghostIndexes {
    init_state axiom forall bytes32 x. ghostIndexes[x] == 0;
}

// ghost field for the length of the values array (stored in offset 0)
ghost uint256 ghostLength {
    init_state axiom ghostLength == 0;
    // assumption: it's infeasible to grow the list to these many elements.
    axiom ghostLength < max_uint256;
}

// HOOKS
// Store hook to synchronize ghostLength with the length of the set._inner._values array.
hook Sstore currentContract.set._inner._values.length uint256 newLength {
    ghostLength = newLength;
}

// Store hook to synchronize ghostValues array with set._inner._values.
hook Sstore currentContract.set._inner._values[INDEX uint256 index] bytes32 newValue {
    ghostValues[index] = newValue;
}

// Store hook to synchronize ghostIndexes array with set._inner._indexes.
hook Sstore currentContract.set._inner._indexes[KEY bytes32 value] uint256 newIndex {
    ghostIndexes[value] = newIndex;
}

// The load hooks can use require to ensure that the ghost field has the same information as the storage.
// The require is sound, since the store hooks ensure the contents are always the same.  However we cannot
// prove that with invariants, since this would require the invariant to read the storage for all elements
// and neither storage access nor function calls are allowed in quantifiers.
//
// By following this simple pattern it is ensured that the ghost state and the storage are always the same
// and that the solver can use this knowledge in the proofs.

// Load hook to synchronize ghostLength with the length of the set._inner._values array.
hook Sload uint256 length currentContract.set._inner._values.length {
    require ghostLength == length;
}

hook Sload bytes32 value currentContract.set._inner._values[INDEX uint256 index] {
    require ghostValues[index] == value;
}

hook Sload uint256 index currentContract.set._inner._indexes[KEY bytes32 value] {
    require ghostIndexes[value] == index;
}

// INVARIANTS

//  This is the main invariant stating that the indexes and values always match:
//        values[indexes[v] - 1] = v for all values v in the set
//    and indexes[values[i]] = i+1 for all valid indexes i.

invariant setInvariant()
    (forall uint256 index. 0 <= index && index < ghostLength => to_mathint(ghostIndexes[ghostValues[index]]) == index + 1) && (forall bytes32 value. ghostIndexes[value] == 0 || (ghostValues[ghostIndexes[value] - 1] == value && ghostIndexes[value] >= 1 && ghostIndexes[value] <= ghostLength));

// DEFINITION

// Returns, whether a value is in the set.
definition inSet(bytes32 value) returns bool = (ghostIndexes[value] != 0);

// RULES

rule containsEqualsInSet() {
    bytes32 value;
    bool result = contains@withrevert(value);
    assert !lastReverted, "contains should never revert";
    assert result == inSet(value), "result should indicate whether value is in set";
}

rule lengthEqualsGhost() {
    uint256 len = length@withrevert();
    assert !lastReverted, "length() should never revert";
    assert len == ghostLength, "length() should return the length of the values list";
}

rule addFresh() {
    bytes32 value;
    bytes32 other;
    require other != value;
    require !inSet(value);
    bool otherInSet = inSet(other);
    bool result = add@withrevert(value);
    assert !lastReverted, "addFresh() should never revert";
    assert result && inSet(value), "value should have been added to list";
    assert otherInSet == inSet(other), "no other value should be added or removed";
}

rule addAlreadyIn() {
    bytes32 value;
    bytes32 other;
    require other != value;
    require inSet(value);
    bool otherInSet = inSet(other);
    bool result = add@withrevert(value);
    assert !lastReverted, "addFresh() should never revert";
    assert !result && inSet(value), "addFresh should return false if element in list";
    assert otherInSet == inSet(other), "no other value should be added or removed";
}

rule removeSuccess() {
    bytes32 value;
    bytes32 other;
    requireInvariant setInvariant();
    require other != value;
    require inSet(value);
    bool otherInSet = inSet(other);
    bool result = remove@withrevert(value);
    assert !lastReverted, "remove() should never revert";
    assert result && !inSet(value), "remove should remove element from list";
    assert otherInSet == inSet(other), "no other value should be added or removed";
}

rule removeFail() {
    bytes32 value;
    bytes32 other;
    require other != value;
    require !inSet(value);
    bool otherInSet = inSet(other);
    bool result = remove@withrevert(value);
    assert !lastReverted, "remove() should never revert";
    assert !result && !inSet(value), "remove should return false if element was not in list";
    assert otherInSet == inSet(other), "no other value should be added or removed";
}

rule elemAtSuccess() {
    bytes32 value;
    uint256 index;
    requireInvariant setInvariant();
    require index < ghostLength;
    value = elemAt@withrevert(index);
    assert !lastReverted, "elemAt() should not revert for valid index";
    assert inSet(value), "elemAt() should return a value from the set";
}

rule elemAtFail() {
    bytes32 value;
    uint256 index;
    require index >= ghostLength;
    value = elemAt@withrevert(index);
    assert lastReverted, "elemAt() should revert for invalid index";
}

rule elementsUnique() {
    bytes32 value1;
    bytes32 value2;
    uint256 index1;
    uint256 index2;
    requireInvariant setInvariant();
    require index1 != index2;
    value1 = elemAt(index1);
    value2 = elemAt(index2);
    assert value1 != value2, "all elements in the list should be different";
}

rule everyElementReachable() {
    bytes32 value;
    bytes32 result;
    uint256 index;
    requireInvariant setInvariant();
    require inSet(value);
    index = assert_uint256(ghostIndexes[value] - 1);
    result = elemAt@withrevert(index);
    assert !lastReverted, "elemAt should not revert for valid index";
    assert result == value, "every value should be at its corresponding index";
}
