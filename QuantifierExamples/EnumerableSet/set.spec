methods {
    function add(bytes32) external returns (bool) envfree;
    function remove(bytes32) external returns (bool) envfree;
    function contains(bytes32) external returns (bool) envfree;
    function length() external returns (uint256) envfree;
    function elemAt(uint256) external returns (bytes32) envfree;
}

// GHOST COPIES
ghost mapping(mathint => bytes32) ghostValues {
    init_state axiom forall mathint x. ghostValues[x] == to_bytes32(0);
}
ghost mapping(bytes32 => uint256) ghostIndexes {
    init_state axiom forall bytes32 x. ghostIndexes[x] == 0;
}
ghost uint256 ghostLength {
    // assumption: it's infeasible to grow the list to these many elements.
    axiom ghostLength < 0xffffffffffffffffffffffffffffffff;
}

// HOOKS

hook Sstore currentContract.set.(offset 0) uint256 newLength STORAGE {
    ghostLength = newLength;
}
hook Sstore currentContract.set._inner._values[INDEX uint256 index] bytes32 newValue STORAGE {
    ghostValues[index] = newValue;
}
hook Sstore currentContract.set._inner._indexes[KEY bytes32 value] uint256 newIndex STORAGE {
    ghostIndexes[value] = newIndex;
}

hook Sload uint256 length currentContract.set.(offset 0) STORAGE {
    require ghostLength == length;
}
hook Sload bytes32 value currentContract.set._inner._values[INDEX uint256 index] STORAGE {
    require ghostValues[index] == value;
}
hook Sload uint256 index currentContract.set._inner._indexes[KEY bytes32 value] STORAGE {
    require ghostIndexes[value] == index;
}

// INVARIANTS

invariant setInvariant()
    (forall uint256 index. 0 <= index && index < ghostLength => to_mathint(ghostIndexes[ghostValues[index]]) == index + 1)
    && (forall bytes32 value. ghostIndexes[value] == 0 || 
         (ghostValues[ghostIndexes[value] - 1] == value && ghostIndexes[value] >= 1 && ghostIndexes[value] <= ghostLength));

// DEFINITION

definition inSet(bytes32 value) returns bool = (ghostIndexes[value] != 0);

rule containsEqualsInSet()
{
    bytes32 value;
    bool result = contains@withrevert(value);

    assert !lastReverted;
    assert result == inSet(value);
}

rule lengthEqualsGhost()
{
    uint256 len = length();
    assert !lastReverted;
    assert len == ghostLength;
}

rule addFresh()
{
    bytes32 value;
    bytes32 other;

    require other != value;

    require !inSet(value);
    bool otherInSet = inSet(other);
    bool result = add@withrevert(value);

    assert !lastReverted;
    assert result && inSet(value);
    assert otherInSet == inSet(other);
}

rule addAlreadyIn()
{
    bytes32 value;
    bytes32 other;

    require other != value;

    require inSet(value);
    bool otherInSet = inSet(other);
    bool result = add@withrevert(value);

    assert !lastReverted;
    assert !result && inSet(value);
    assert otherInSet == inSet(other);
}

rule removeSuccess()
{
    bytes32 value;
    bytes32 other;

    requireInvariant setInvariant();
    require other != value;

    require inSet(value);
    bool otherInSet = inSet(other);
    bool result = remove@withrevert(value);

    assert !lastReverted;
    assert result && !inSet(value);
    assert otherInSet == inSet(other);
}

rule removeFail()
{
    bytes32 value;
    bytes32 other;

    require other != value;

    require !inSet(value);
    bool otherInSet = inSet(other);
    bool result = remove@withrevert(value);

    assert !lastReverted;
    assert !result && !inSet(value);
    assert otherInSet == inSet(other);
}

rule elemAtSuccess()
{
    bytes32 value;
    uint256 index;

    requireInvariant setInvariant();
    require index < ghostLength;

    value = elemAt@withrevert(index);

    assert !lastReverted;
    assert inSet(value);
}

rule elemAtFail()
{
    bytes32 value;
    uint256 index;

    require index >= ghostLength;

    value = elemAt@withrevert(index);

    assert lastReverted;
}

rule elementsUnique()
{
    bytes32 value1;
    bytes32 value2;
    uint256 index1;
    uint256 index2;

    requireInvariant setInvariant();
    require index1 != index2;

    value1 = elemAt(index1);
    value2 = elemAt(index2);

    assert value1 != value2;
}

rule everyElementReachable()
{
    bytes32 value;
    bytes32 result;
    uint256 index;

    requireInvariant setInvariant();
    require inSet(value);
    index = assert_uint256(ghostIndexes[value] - 1);

    result = elemAt@withrevert(index);
    assert !lastReverted;
    assert result == value;
}
