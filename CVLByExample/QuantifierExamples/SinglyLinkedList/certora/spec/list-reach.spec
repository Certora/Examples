// Specification for reachability for a linked list implementation.


// Method block: all methods don't need environment

methods {
    function insertAfter(bytes32, bytes32) external envfree;
    function getSucc(bytes32) external returns (bytes32) envfree;
    function contains(bytes32) external returns (bool) envfree;
    function head() external returns (bytes32) envfree;
}

// GHOST

// This is our reachability predicate stating whether there is a path between X and Y using zero or more successor steps.

ghost reach(bytes32, bytes32) returns bool {
    init_state axiom forall bytes32 X. forall bytes32 Y. reach(X, Y) == (X == Y || Y == to_bytes32(0));
}

// Our ghost copy of the valid map.
ghost mapping(bytes32 => bool) ghostValid {
    init_state axiom forall bytes32 X. ghostValid[X] == false;
}

// Our ghost copy of the nextKey map.
ghost mapping(bytes32 => bytes32) ghostSucc {
    init_state axiom forall bytes32 X. ghostSucc[X] == to_bytes32(0);
}

// Our ghost copy of the list head.
ghost bytes32 ghostHead;

definition isSucc(bytes32 a, bytes32 b) returns bool = reach(a, b) && a != b && (forall bytes32 X. reach(a, X) && reach(X, b) => (a == X || b == X));

definition reachSuccInvariant(bytes32 key) returns bool =
    (key == to_bytes32(0) && ghostSucc[key] == to_bytes32(0))
    || (key != to_bytes32(0) && isSucc(key, ghostSucc[key]));

definition updateSucc(bytes32 a, bytes32 b) returns bool = forall bytes32 X. forall bytes32 Y. reach@new(X, Y) == 
            (X == Y ||
            (reach@old(X, Y) && !(reach@old(X, a) && a != Y && reach@old(a, Y))) ||
            (reach@old(X, a) && reach@old(b, Y)));

hook Sstore currentContract.list.elements[KEY bytes32 key].nextKey bytes32 newNextKey {
    bytes32 otherKey;
    
    require reachSuccInvariant(otherKey);
    assert !reach(newNextKey,key), "Setting next introduces cycle";
    
    // update ghost successor
    ghostSucc[key] = newNextKey;
    // update ghost reachability
    havoc reach assuming updateSucc(key, newNextKey);

    assert reachSuccInvariant(otherKey), "Successor invariant not preserved";
}

hook Sstore currentContract.list.elements[KEY bytes32 key].valid uint256 value {
    ghostValid[key] = value != 0;
}

hook Sstore currentContract.list.head bytes32 newHead {
    ghostHead = newHead;
}

hook Sload bytes32 nextKey currentContract.list.elements[KEY bytes32 key].nextKey {
    require ghostSucc[key] == nextKey;
    require reachSuccInvariant(key);
}

hook Sload bytes32 head currentContract.list.head {
    require ghostHead == head;
}

hook Sload uint256 valueValid currentContract.list.elements[KEY bytes32 key].valid {
    require valueValid != 0 <=> ghostValid[key];
}


invariant inListIffValid()
    forall bytes32 key. key != to_bytes32(0) => ghostValid[key] == reach(ghostHead, key)
    {
        preserved {
            requireInvariant reach_invariant();
        }
    }

invariant reach_invariant()
    forall bytes32 X. forall bytes32 Y. forall bytes32 Z. ( 
        reach(X, X)
        && (reach(X,Y) && reach (Y, X) => X == Y)
        && (reach(X,Y) && reach (Y, Z) => reach(X, Z))
        && (reach(X,Y) && reach (X, Z) => (reach(Y,Z) || reach(Z,Y)))
    )
    { 
        preserved {
            requireInvariant inListIffValid();
        }
    }

invariant reach_succ(bytes32 key)
    reachSuccInvariant(key)
    { 
        preserved {
            requireInvariant reach_invariant();
            requireInvariant inListIffValid();
        }
    }

rule checkGetSucc {
    bytes32 key;
    bytes32 afterKey = getSucc(key);
    requireInvariant reach_invariant();
    assert reach(key, afterKey);
}

// Rules for full correctness of API calls.

rule checkInsertHead {
    bytes32 key;
    bytes32 afterKey;
    bytes32 headKey = head();
    requireInvariant inListIffValid();
    requireInvariant reach_invariant();

    // inserts at head
    require afterKey == to_bytes32(0);
    insertAfter(key, afterKey);

    assert reach(key, headKey);
    assert reach(ghostHead, headKey);
}

rule checkInsertSuccessor {
    bytes32 key;
    bytes32 afterKey;
    requireInvariant reach_invariant();
    requireInvariant inListIffValid();
    require !reach(afterKey, key);
    // do not insert at head
    require afterKey != to_bytes32(0);
    insertAfter(key, afterKey);
    assert reach(afterKey, key);
}


rule checkInsert {
    bytes32 key;
    bytes32 afterKey;
    bytes32 randoBoi;
    requireInvariant reach_invariant();
    requireInvariant inListIffValid();

    require reach(ghostHead, randoBoi);
    insertAfter(key, afterKey);
    assert reach(ghostHead, randoBoi), "Element from the list was lost";
    assert reach(ghostHead, key), "Key was not inserted";
}

rule checkInsertRevertsWhenExists {
    bytes32 key;
    bytes32 afterKey;
    requireInvariant reach_invariant();
    requireInvariant inListIffValid();
    require ghostValid[key];

    insertAfter@withrevert(key, afterKey);
    assert lastReverted, "insert should revert";
}

rule checkInsertRevertsWhenAfterKeyNotExists {
    bytes32 key;
    bytes32 afterKey;
    requireInvariant reach_invariant();
    requireInvariant inListIffValid();
    require afterKey != to_bytes32(0);
    require !ghostValid[afterKey];

    insertAfter@withrevert(key, afterKey);
    assert lastReverted, "insert can revert";
}

rule checkInsertSucceedsOtherwise {
    bytes32 key;
    bytes32 afterKey;
    requireInvariant reach_invariant();
    requireInvariant inListIffValid();
    require afterKey == to_bytes32(0) || ghostValid[afterKey];
    require key != to_bytes32(0) && !ghostValid[key];

    insertAfter@withrevert(key, afterKey);
    assert !lastReverted, "insert should not revert";
}