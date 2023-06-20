methods {
    function insertAfter(bytes32, bytes32) external envfree;
    function getSucc(bytes32) external returns (bytes32) envfree;
    function contains(bytes32) external returns (bool) envfree;
    function head() external returns (bytes32) envfree;
}

ghost reach(bytes32, bytes32) returns bool {
    init_state axiom forall bytes32 X. forall bytes32 Y. reach(X, Y) == (X == Y || Y == to_bytes32(0));
}

ghost mapping(bytes32 => bool) ghostExists {
    init_state axiom forall bytes32 X. ghostExists[X] == false;
}

ghost mapping(bytes32 => bytes32) ghostSucc {
    init_state axiom forall bytes32 X. ghostSucc[X] == to_bytes32(0);
}

ghost bytes32 ghostHead;

invariant inListIffExists()
    forall bytes32 key. key != to_bytes32(0) => ghostExists[key] == reach(ghostHead, key)
    {
        preserved insertAfter(bytes32 newKey, bytes32 keyAfter) {
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
        preserved insertAfter(bytes32 newKey, bytes32 keyAfter) {
            requireInvariant inListIffExists();
        }
    }

definition isSucc(bytes32 a, bytes32 b) returns bool = reach(a, b) && a != b && (forall bytes32 X. reach(a, X) && reach(X, b) => (a == X || b == X));

invariant reach_succ(bytes32 key, bytes32 next)
    (key == to_bytes32(0) && ghostSucc[key] == to_bytes32(0))
    || (key != to_bytes32(0) && ((ghostSucc[key] == next) => isSucc(key, next)))
    {
        preserved insertAfter(bytes32 newKey, bytes32 keyAfter) {
            requireInvariant inListIffExists();
            requireInvariant reach_invariant();
        }
    }

definition updateSucc(bytes32 a, bytes32 b) returns bool = forall bytes32 X. forall bytes32 Y. reach@new(X, Y) == 
            (X == Y ||
            (reach@old(X, Y) && !(reach@old(X, a) && a != Y && reach@old(a, Y))) ||
            (reach@old(X, a) && reach@old(b, Y)));

hook Sstore (slot 0).(offset 32)[KEY bytes32 key].(offset 0) bytes32 newNextKey STORAGE {
    ghostSucc[key] = newNextKey;
    havoc reach assuming updateSucc(key, newNextKey);
}

hook Sstore (slot 0).(offset 32)[KEY bytes32 key].(offset 32) bytes32 value STORAGE {
    ghostExists[key] = value != to_bytes32(0);
}

hook Sstore currentContract.list.head bytes32 newHead STORAGE {
    ghostHead = newHead;
}

hook Sload bytes32 nextKey (slot 0).(offset 32)[KEY bytes32 key].(offset 0) STORAGE {
    require ghostSucc[key] == nextKey;
    requireInvariant reach_succ(key, nextKey);
    //require (key == 0 && ghostSucc[key] == 0)
    //        || (key != 0 && isSucc(key, nextKey));

}

hook Sload bytes32 head currentContract.list.head STORAGE {
    require ghostHead == head;
}

hook Sload uint256 valueExists (slot 0).(offset 32)[KEY bytes32 key].(offset 32) STORAGE {
    require valueExists != 0 <=> ghostExists[key];
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
    requireInvariant inListIffExists();
    requireInvariant reach_invariant();

    // inserts at head
    require afterKey == to_bytes32(0);
    insertAfter@norevert(key, afterKey);

    assert reach(key, headKey);
    assert reach(ghostHead, headKey);
}

rule checkInsertSuccessor {
    bytes32 key;
    bytes32 afterKey;
    requireInvariant reach_invariant();
    requireInvariant inListIffExists();
    require !reach(afterKey, key);
    // do not insert at head
    require afterKey != to_bytes32(0);
    insertAfter@norevert(key, afterKey);
    assert reach(afterKey, key);
}

rule checkInsert {
    bytes32 key;
    bytes32 afterKey;
    bytes32 randoBoi;
    requireInvariant reach_invariant();
    requireInvariant inListIffExists();

    require reach(ghostHead, randoBoi);
    insertAfter@norevert(key, afterKey);
    assert reach(ghostHead, randoBoi);
}
