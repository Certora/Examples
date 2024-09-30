contract Extension2 {
    uint __reserved; // to keep the storage layout in agreement with the base contracts
    uint inExtension2;

    // Function that the base contract will delegate to
    function setInExtension2(uint n) public {
        inExtension2 = n;
    }

    function getInExtension2() public view returns (uint) {
        return inExtension2;
    }
}