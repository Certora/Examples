contract C {
    mapping(address => int) _n;
    bool internal _b;

    function ghostUpdater(address a, int n) external {
        _n[a] = n;
    }

    function ghostUpdaterReverts(address a, int n) external {
        _n[a] = n;
        if (!_b) {
            revert();
        }
    }
}
