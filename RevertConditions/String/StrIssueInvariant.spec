/* An invariant verifying all string writes are legal
 * ==================================================
 * This spec has invariant verifying we cannot write an illegally encoded string
 * to storage. This invariant fails, because of the `dirty` function.
 */


/// @title Checks that `encoded` is a valid encoding of the first 32 bytes of a string
function isLegalEncoding(uint256 encoded) returns bool {
    mathint doubleStrLen = (encoded % 256);  // Double string length for short strings
    bool isOdd = encoded % 2 == 1;
    return (encoded > 64 && isOdd) || (doubleStrLen <= 62 && !isOdd);
}


/// @title Ghost updated by legality of string encoding is legal
ghost bool isLegalStr {
    init_state axiom isLegalStr;
}


/// @title Hook activated when the string in field `y` is written
hook Sstore structArray[INDEX uint256 index].(offset 32) bytes32 str {
    uint256 encoded;
    require to_bytes32(encoded) == str;
    isLegalStr = isLegalStr && isLegalEncoding(encoded);
}


/** @title All reads and writes to string `y` are legal
 *  @notice This invariant is violated by the function `dirty`.
 *  @notice In `solc` versions higher than 0.8.10 the Prover will have
 *  a violation also for `push`.
 */
invariant alwaysLegalStorage()
    isLegalStr;
