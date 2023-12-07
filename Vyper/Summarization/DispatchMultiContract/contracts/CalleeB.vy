interface CalleeB:
    x: public(uint256)
    value: public(uint256)

    @external
    def setX(_x: uint256) -> uint256:
        self.x = _x
        return self.x

    @external
    @view
    def getX() -> uint256:
        return self.x

    @external
    @view
    def getValue() -> uint256:
        return self.value

    @external
    def setValue(_value: uint256) -> uint256:
        self.value = _value
        return self.value

    @external
    @payable
    def setXandSendEther(_x: uint256) -> (uint256, uint256):
        self.x = _x
        self.value = msg.value
        return (self.x, self.value)

    @external
    @view
    def dummyB() -> uint256:
        return 222
