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
ghost mapping(address => address) ghostNext {
    init_state axiom forall address x. ghostNext[x] == 0;
}
ghost mapping(address => address) ghostPrev {
    init_state axiom forall address x. ghostPrev[x] == 0;
}
ghost mapping(address => uint256) ghostValue {
    init_state axiom forall address x. ghostValue[x] == 0;
}
ghost address ghostHead;
ghost address ghostTail;
ghost uint256 ghostLength;
ghost nextstar(address, address) returns bool {
    init_state axiom forall address x. forall address y. nextstar(x, y) == (x == y);
}
ghost prevstar(address, address) returns bool {
    init_state axiom forall address x. forall address y. prevstar(x, y) == (x == y);
}

// HOOKS

hook Sstore currentContract.dll.head address newHead STORAGE {
    ghostHead = newHead;
}
hook Sstore currentContract.dll.tail address newTail STORAGE {
    ghostTail = newTail;
}

hook Sstore currentContract.dll.accounts[KEY address key].next address newNext STORAGE {
    ghostNext[key] = newNext;
}

hook Sstore currentContract.dll.accounts[KEY address key].prev address newPrev STORAGE {
    ghostPrev[key] = newPrev;
}
hook Sstore currentContract.dll.accounts[KEY address key].value uint256 newValue STORAGE {
    ghostValue[key] = newValue;
}

hook Sload address head currentContract.dll.head STORAGE {
    require ghostHead == head;
}
hook Sload address tail currentContract.dll.tail STORAGE {
    require ghostTail == tail;
}
hook Sload address next currentContract.dll.accounts[KEY address key].next STORAGE {
    require ghostNext[key] == next;
}
hook Sload address prev currentContract.dll.accounts[KEY address key].prev STORAGE {
    require ghostPrev[key] == prev;
}
hook Sload uint256 value currentContract.dll.accounts[KEY address key].value STORAGE {
    require ghostValue[key] == value;
}

// INVARIANTS

invariant nextPrevMatch()
    ((ghostHead == 0 && ghostTail == 0)
    || (ghostHead != 0 && ghostTail != 0 && ghostNext[ghostTail] == 0 && ghostPrev[ghostHead] == 0
        && ghostValue[ghostHead] != 0 && ghostValue[ghostTail] != 0))
    && (forall address a.  (ghostNext[a] == 0 && ghostPrev[a] == 0 && ghostValue[a] == 0) 
        || (a != 0 && ghostValue[a] != 0
            && ((a == ghostHead && ghostPrev[a] == 0) || ghostNext[ghostPrev[a]] == a)
            && ((a == ghostTail && ghostNext[a] == 0) || ghostPrev[ghostNext[a]] == a)));


invariant inList()
    (ghostHead != 0 => ghostValue[ghostHead] != 0)
    && (ghostTail != 0 => ghostValue[ghostTail] != 0)
    && (forall address a.  ghostNext[a] != 0 => ghostValue[ghostNext[a]] != 0)
    && (forall address a.  ghostPrev[a] != 0 => ghostValue[ghostPrev[a]] != 0)
    {
        preserved {
            requireInvariant nextPrevMatch();
        }
    }
