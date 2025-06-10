methods {
    function getValueOf(address) external returns (uint256) envfree;
    function getHead() external returns (address) envfree;
    function getTail() external returns (address) envfree;
    function getNext(address) external returns (address) envfree;
    function getPrev(address) external returns (address) envfree;
    function remove(address) external envfree;
    function insertSorted(address, uint256, uint256) external envfree;
}

// GHOST COPIES
ghost mapping (address => address) ghostNext {
    axiom forall address x. ghostNext[x] == 0;
}

ghost mapping (address => address) ghostPrev {
    axiom forall address x. ghostPrev[x] == 0;
}

ghost mapping (address => uint256) ghostValue {
    axiom forall address x. ghostValue[x] == 0;
}

ghost address ghostHead {
    axiom ghostHead == 0;
}

ghost address ghostTail {
    axiom ghostTail == 0;
}

ghost nextstar(address, address) returns bool {
    axiom forall address x. forall address y. nextstar(x, y) == (x == y);
}

ghost prevstar(address, address) returns bool {
    axiom forall address x. forall address y. prevstar(x, y) == (x == y);
}

// HOOKS
hook Sstore currentContract.dll.head address newHead {
    ghostHead = newHead;
}

hook Sstore currentContract.dll.tail address newTail {
    ghostTail = newTail;
}

hook Sstore currentContract.dll.accounts[KEY address key].next address newNext {
    ghostNext[key] = newNext;
}

hook Sstore currentContract.dll.accounts[KEY address key].prev address newPrev {
    ghostPrev[key] = newPrev;
}

hook Sstore currentContract.dll.accounts[KEY address key].value uint256 newValue {
    ghostValue[key] = newValue;
}

hook Sload address head currentContract.dll.head {
    require ghostHead == head;
}

hook Sload address tail currentContract.dll.tail {
    require ghostTail == tail;
}

hook Sload address next currentContract.dll.accounts[KEY address key].next {
    require ghostNext[key] == next;
}

hook Sload address prev currentContract.dll.accounts[KEY address key].prev {
    require ghostPrev[key] == prev;
}

hook Sload uint256 value currentContract.dll.accounts[KEY address key].value {
    require ghostValue[key] == value;
}

// INVARIANTS
invariant nextPrevMatch()
// either list is empty, and both head and tail are 0,
// for all addresses:
// or both head and tail are set and their prev resp. next points to 0.
((ghostHead == 0 && ghostTail == 0) || (ghostHead != 0 && ghostTail != 0 && ghostNext[ghostTail] == 0 && ghostPrev[ghostHead] == 0 && ghostValue[ghostHead] != 0 && ghostValue[ghostTail] != 0)) && (forall address a.
// either the address is not part of the list and every field is 0.
// or the address is part of the list, address is non-zero, value is non-zero,
// and prev and next pointer are linked correctly.
(ghostNext[a] == 0 && ghostPrev[a] == 0 && ghostValue[a] == 0) || (a != 0 && ghostValue[a] != 0 && ((a == ghostHead && ghostPrev[a] == 0) || ghostNext[ghostPrev[a]] == a) && ((a == ghostTail && ghostNext[a] == 0) || ghostPrev[ghostNext[a]] == a))) ;

invariant inList() (ghostHead != 0 => ghostValue[ghostHead] != 0) && (ghostTail != 0 => ghostValue[ghostTail] != 0) && (forall address a. ghostNext[a] != 0 => ghostValue[ghostNext[a]] != 0) && (forall address a. ghostPrev[a] != 0 => ghostValue[ghostPrev[a]] != 0) {
    preserved {
        requireInvariant nextPrevMatch();
 }

rule insert_preserves_old {
    address newElem;
    address oldElem;
    uint256 newValue;
    uint256 maxIter;
    bool oldInList = ghostValue[oldElem] != 0;
    require oldElem != newElem;
    insertSorted(newElem, newValue, maxIter);
    assert oldInList == (ghostValue[oldElem] != 0);
}

rule insert_adds_new {
    address newElem;
    uint256 newValue;
    uint256 maxIter;
    insertSorted(newElem, newValue, maxIter);
    assert ghostValue[newElem] != 0;
    assert ghostValue[newElem] == newValue;
}

rule insert_does_not_revert {
    address newElem;
    uint256 newValue;
    uint256 maxIter;
    require newElem != 0;
    require ghostValue[newElem] == 0;
    require newValue != 0;
    insertSorted@withrevert(newElem, newValue, maxIter);
    assert !lastReverted;
}

rule remove_preserves_old {
    address elem;
    address oldElem;
    bool oldInList = ghostValue[oldElem] != 0;
    require oldElem != elem;
    remove(elem);
    assert oldInList == (ghostValue[oldElem] != 0);
}

rule remove_deletes {
    address elem;
    remove(elem);
    assert ghostValue[elem] == 0;
}

rule remove_does_not_revert {
    address elem;
    require elem != 0;
    require ghostValue[elem] != 0;
    remove@withrevert(elem);
    assert !lastReverted;
}