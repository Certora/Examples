contract ERC7201Example {
    uint existing;

    struct Beep {
        uint mask;
        uint[256] words;
        mapping(uint => uint) map;
    }
    
    /** @custom:storage-location erc7201:test.book1 */
    struct Book1 {
        Beep field1;
        Beep field2;
    }

    /** @custom:storage-location erc7201:test.book2 */
    struct Book2 {
        Beep field1;
        Beep field2;
    }

    bytes32 private constant BOOK_LOCATION_1 = 0xa98021c2457156ef41a513acb530a8c9fe169e1e82e9bfb99c54208adb859000;
    bytes32 private constant BOOK_LOCATION_2 = 0x6fb9e6acca90d1fee0e954f0b1a7784617ba7258c0755057dc177b774fb42e00;

    function getBook1() internal returns (Book1 storage) {
        Book1 storage b;
        assembly ("memory-safe") {
            b.slot := BOOK_LOCATION_1
        }
        return b;
    }

    function getBook2() internal returns (Book2 storage) {
        Book2 storage b;
        assembly ("memory-safe") {
            b.slot := BOOK_LOCATION_2
        }
        return b;
    }

    function doThing(uint256 x, bool which) external returns (uint256) {
        Book1 storage b = getBook1();
        Beep storage theBeep = which ? b.field1 : b.field2;
        uint8 pos = uint8(x & 255);
        return theBeep.words[pos];
    }

    function doOtherThing(uint256 x, bool which) external returns (uint256) {
        Book2 storage b = getBook2();
        Beep storage theBeep = which ? b.field1 : b.field2;
        uint8 pos = uint8(x & 255);
        return theBeep.words[pos];
    }
}
