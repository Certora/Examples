ghost mapping(uint256 => uint256) userArray;

rule returnTuple(env e, uint256 y) {
    userArray[y], _ = tuple(e);
    assert userArray[y] == 2;
}
