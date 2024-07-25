contract RootStruct {
    struct Simple {
        uint x;
        address y;
        uint8 z1;
        uint8 z2;
        bool b1;
        uint x2;
        bool b2;
    }

    Simple s;

    function workOnSExt(uint x) external {
        this.workOnS(x, s);
    }

    function workOnS(uint x, Simple memory s) external {
        s.x = x;
        s.b2 = true;
        s.b1 = x > 3;
    }
}
