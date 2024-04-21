/**
 * Identifying illegally encoded strings
 * =====================================
 * We use a hook and a persistent ghost to identify an illegally encoded string, and
 * add it to the revert conditions. The hook is called every time the slot for the
 * field `y` in the struct `structArray[index]` is read. This gives us an opportunity
 * to examine the encoded `bytes32` value.
 *
 * We use the hook to update the persistent ghost `legalStr` - changing the ghost's value
 * to false if the encoding is illegal. Since the ghost is persistent, it is unaffected
 * by reverts and we can use it in our revert condition rules.
 */


/// @title Checks that `encoded` is a valid encoding of the first 32 bytes of a string
function isLegalEncoding(uint256 encoded) returns bool {
    mathint strLen = (encoded % 256) / 2;  // The string length for short strings only
    bool isOdd = encoded % 2 == 1;
    return (encoded > 64 && isOdd) || (strLen <= 31 && !isOdd);
}


/// Persistent ghost denoting legality of string encoding
persistent ghost bool legalStr;


/// @title Hook activated when the string in field `y` is read
hook Sload bytes32 str structArray[INDEX uint256 index].(offset 32) {
    uint256 encoded;
    require to_bytes32(encoded) == str;
    legalStr = isLegalEncoding(encoded) && legalStr;
}


/// @title Checks when the `push` function reverts
rule VerifyPush(uint256 xx, string yy) {
    // When a revert occurs, `legalStr` will not revert because it is `persistent`.
    legalStr = true;

    env e;

    push@withrevert(e, xx, yy);
    bool isReverted = lastReverted;

    // Note that transferring funds to non-payable function can also cause revert.
    assert isReverted <=> (!legalStr || e.msg.value != 0);
}


/// @title An example of reverting due to bad string
rule VerifyGetDataExample(uint256 index) {
    legalStr = true;

    env e;
    // This require prevents a revert unrelated to the string encoding
    require e.msg.value == 0;

    getData@withrevert(e, index);

    satisfy !legalStr;  // The example must have reverted
}
