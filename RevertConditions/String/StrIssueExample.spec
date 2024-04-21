/* Example of reverts caused by string encoding
 * ============================================
 * The rules here assert that a revert in `push` and `getData` can only occur due to
 * eth being sent, or bad index in the case of `getData`. Both rules fail because
 * the string issue, described below, is another cause for revert.
 *
 * In general, storage variables are stored in particular slots, where each slot
 * has 32 bytes. You can learn more about this in (1) below.
 * Strings have a particular encoding in storage, meant to avoid wasting storage.
 * You can find the details in (2) below. In short:
 * 
 * - If the length of the string l is 31 bytes or less, the entire string will be
 *   stored in the relevant slot, and the lowest-order byte
 *   will hold 2*l (twice the length of the string).
 * - If the length of the string l is 32 bytes or more, the value of the slot
 *    will be 2*l+1.
 * 
 * So values like 3, or 100 cannot be stored in the slot of a string. When reading
 * a string, Solidity reverts if the value in the slot is invalid. Note that solidity
 * also reads the existing value before writing a new string. So a write could also
 * potentially result in a revert.
 *
 * Links:
 * ------
 * (1) Layout of State Variables in Storage:
 *     https://docs.soliditylang.org/en/stable/internals/layout_in_storage.html
 * (2) Bytes and String Layout in Storage:
 *     https://docs.soliditylang.org/en/stable/internals/layout_in_storage.html#bytes-and-string
 */
 methods {
     function arrayLength() external returns (uint256) envfree;
 }


/// @title Verifies the `push` function reverts only if value is sent
rule verifyPush(uint256 xx, string yy) {
    env e;
    push@withrevert(e, xx, yy);
    bool isReverted = lastReverted;
    assert isReverted <=> (e.msg.value != 0);
}


/// @title Verifies `getData` reverts only if value is sent or bad index
rule verifyGetData(uint256 index) {
    env e;
    getData@withrevert(e, index);
    bool isReverted = lastReverted;
    assert isReverted <=> (
        (e.msg.value != 0) ||
        (index >= arrayLength())
    );
}
